#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataError(Exception):
    pass


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return False

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise DataError("No data left to process")
        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            if not data:
                return False
            for num in data:
                if self._isnum(num):
                    pass
                else:
                    return False
            return True
        else:
            return self._isnum(data)

    def _isnum(self, data: Any) -> bool:
        if not isinstance(data, bool) and isinstance(data, int | float):
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise DataError("Improper numeric data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self.data.append((self._next_rank, str(value)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            if not data:
                return False
            for text in data:
                if self._istext(text):
                    pass
                else:
                    return False
            return True
        else:
            return self._istext(data)

    def _istext(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise DataError("Improper text data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self.data.append((self._next_rank, str(value)))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            if not data:
                return False
            for log in data:
                if self._islog(log):
                    pass
                else:
                    return False
            return True
        else:
            return self._islog(data)

    def _islog(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        if not data:
            return False
        return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
                )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise DataError("Improper log data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            text = ": ".join(value.values())
            self.data.append((self._next_rank, text))
            self._next_rank += 1


def show_validation(processor: DataProcessor, data: Any) -> None:
    print(f"Trying to validate input '{data}': {processor.validate(data)}")


def extract(processor: DataProcessor, count: int, label: str) -> None:
    suffix = "s" if count != 1 else ""
    print(f"Extracting {count} value{suffix}...")
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    show_validation(numeric, 42)
    show_validation(numeric, "Hello")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except DataError as error:
        print(f"Got exception: {error}")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    extract(numeric, 3, "Numeric value")

    print("Testing Text Processor...")
    text = TextProcessor()
    show_validation(text, 42)
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text.ingest(text_data)
    extract(text, 1, "Text value")

    print("Testing Log Processor...")
    log = LogProcessor()
    show_validation(log, "Hello")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    extract(log, 2, "Log entry")


if __name__ == "__main__":
    main()
