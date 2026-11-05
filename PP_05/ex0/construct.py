#!/usr/bin/env python3

import sys
import os
import site


def main():
    curr_env: str = sys.prefix
    global_env: str = sys.base_prefix
    venv_name: str = os.path.basename(curr_env)
    packages: list[str] = site.getsitepackages()

    if curr_env == global_env:
        print(
                "Be careful, you're running an unsealed lab\n"
                "Please reseal\n"
                "Guide on how to reseal the lab:\n"
                "1. Create a virtual environment: `python3 -m venv venv`\n"
                "2. Activate the virtual environment:\n"
                " `source venv/bin/activate`"
                )
    else:
        print(
                "Lab is sealed\n"
                f"Current environment: {curr_env}\n"
                f"Venv name: {venv_name}\n"
                f"Python install: {global_env}\n"
                f"Package install path: {packages[0]}"
                )


if __name__ == "__main__":
    main()
