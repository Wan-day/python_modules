#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        a: int = int("abc")
        print(a)
    elif operation_number == 1:
        b: float = 1 / 0
        print(b)
    elif operation_number == 2:
        with open("words.txt") as f:
            text: str = f.read()
            print(text)
    elif operation_number == 3:
        text: str = "test"
        num: int = 5
        full: str = text + num
        print(full)
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()


if __name__ == "__main__":
    main()
