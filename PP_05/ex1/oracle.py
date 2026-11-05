#!/usr/bin/env python3
"""The Oracle: load configuration from the environment, safely."""

from __future__ import annotations

import logging
import os
import sys
from dataclasses import dataclass, field
from typing import Final, Literal

Mode = Literal["development", "production"]

VALID_LOG_LEVELS: Final[tuple[str, ...]] = (
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
)
REQUIRED_VARS: Final[tuple[str, ...]] = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")

# Fallbacks that are only allowed in development
DEV_DEFAULTS: Final[dict[str, str]] = {
    "DATABASE_URL": "sqlite:///dev.db",
    "ZION_ENDPOINT": "http://localhost:8080",
}
DEV_LOG_LEVEL: Final[str] = "DEBUG"
PROD_LOG_LEVEL: Final[str] = "WARNING"


@dataclass
class Config:
    mode: Mode
    database_url: str
    api_key: str
    log_level: str
    zion_endpoint: str
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def is_production(self) -> bool:
        return self.mode == "production"


def try_load_dotenv(path: str) -> bool:
    """Load a .env file if python-dotenv is available. Real env vars win."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return False
    return load_dotenv(path, override=False)


def load_env_file() -> str:
    """Look for .env next to this script, then in the current directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = (
        os.path.join(script_dir, ".env"),
        os.path.join(os.getcwd(), ".env"),
    )
    for path in candidates:
        if os.path.isfile(path):
            if try_load_dotenv(path):
                return f".env loaded from {path}"
            return "python-dotenv not installed or .env empty, file ignored"
    return "no .env file found, using process environment only"


def get_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def parse_mode(raw: str) -> tuple[Mode, str | None]:
    """Return the mode plus an optional warning about the raw value."""
    value = raw.lower()
    if value == "development":
        return "development", None
    if value == "production":
        return "production", None
    if not value:
        return "development", "MATRIX_MODE is not set, assuming 'development'"
    return (
        "development",
        f"MATRIX_MODE '{value}' is invalid "
        "(expected 'development' or 'production'), assuming 'development'",
    )


def read_config() -> Config:
    """Build a Config from environment variables, recording problems."""
    warnings: list[str] = []
    errors: list[str] = []

    mode, mode_warning = parse_mode(get_env("MATRIX_MODE"))
    if mode_warning is not None:
        warnings.append(mode_warning)
    production = mode == "production"

    def resolve(name: str) -> str:
        """Missing values fall back in development and fail in production."""
        value = get_env(name)
        if value:
            return value
        if production:
            errors.append(f"{name} is required in production")
            return ""
        default = DEV_DEFAULTS.get(name)
        if default is not None:
            warnings.append(f"{name} is not set, using dev default")
            return default
        warnings.append(f"{name} is not set, external services disabled")
        return ""

    database_url = resolve("DATABASE_URL")
    api_key = resolve("API_KEY")
    zion_endpoint = resolve("ZION_ENDPOINT")

    # LOG_LEVEL
    fallback_level = PROD_LOG_LEVEL if production else DEV_LOG_LEVEL
    log_level = get_env("LOG_LEVEL").upper()
    if not log_level:
        log_level = fallback_level
        warnings.append(f"LOG_LEVEL is not set, using {log_level}")
    elif log_level not in VALID_LOG_LEVELS:
        warnings.append(f"LOG_LEVEL '{log_level}' is invalid, using {fallback_level}")
        log_level = fallback_level

    # ZION_ENDPOINT format
    if zion_endpoint and not zion_endpoint.startswith(("http://", "https://")):
        message = f"ZION_ENDPOINT '{zion_endpoint}' must start with http:// or https://"
        (errors if production else warnings).append(message)

    # Production should not use plain http or a throwaway sqlite file
    if production:
        if zion_endpoint.startswith("http://"):
            warnings.append("ZION_ENDPOINT uses insecure http in production")
        if database_url.startswith("sqlite"):
            warnings.append("DATABASE_URL points to sqlite in production")

    return Config(
        mode=mode,
        database_url=database_url,
        api_key=api_key,
        log_level=log_level,
        zion_endpoint=zion_endpoint,
        warnings=warnings,
        errors=errors,
    )


def mask_secret(secret: str, production: bool) -> str:
    """Never print a secret in full. Production reveals nothing."""
    if not secret:
        return "(not set)"
    if production:
        return "*" * 8
    return secret[:4] + "*" * max(len(secret) - 4, 4)


def mask_url(url: str) -> str:
    """Hide credentials embedded in a connection string (user:pass@host)."""
    if not url:
        return "(not set)"
    if "@" in url and "://" in url:
        scheme, rest = url.split("://", 1)
        return f"{scheme}://***:***@{rest.rsplit('@', 1)[1]}"
    return url


def setup_logging(level: str) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="  [%(levelname)s] %(message)s",
        force=True,
    )
    return logging.getLogger("oracle")


def report(cfg: Config, env_source: str) -> None:
    production = cfg.is_production
    database_url = mask_url(cfg.database_url) if production else cfg.database_url

    print("ORACLE STATUS: Reading the Matrix...")
    print(f"\nConfig source: {env_source}")

    print("\nConfiguration loaded:")
    print(f"  MATRIX_MODE   : {cfg.mode}")
    print(f"  DATABASE_URL  : {database_url or '(not set)'}")
    print(f"  API_KEY       : {mask_secret(cfg.api_key, production)}")
    print(f"  LOG_LEVEL     : {cfg.log_level}")
    print(f"  ZION_ENDPOINT : {cfg.zion_endpoint or '(not set)'}")

    log = setup_logging(cfg.log_level)

    print("\nMode behavior:")
    if production:
        print("  Production: strict validation, secrets hidden, minimal logging")
        print("  Debug features: DISABLED")
        print("  Missing required settings: refuse to start")
    else:
        print("  Development: lenient defaults, secrets partially visible, verbose logs")
        print("  Debug features: ENABLED")
        print("  Missing required settings: fall back to safe defaults")

    print("\nLog output at this level:")
    log.debug("debug: connecting to %s", database_url)
    log.info("info: contacting Zion at %s", cfg.zion_endpoint)
    log.warning("warning: this is what production would still show")

    if cfg.warnings:
        print("\nWarnings:")
        for item in cfg.warnings:
            print(f"  - {item}")


def main() -> int:
    env_source = load_env_file()
    cfg = read_config()
    report(cfg, env_source)

    if cfg.errors:
        print("\nConfiguration errors (cannot continue):")
        for item in cfg.errors:
            print(f"  - {item}")
        print("\nSet the variables in the environment or in ex1/.env and retry.")
        return 1

    print("\nThe Oracle sees clearly. Configuration is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
