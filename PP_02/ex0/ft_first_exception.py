#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "10"]
    for i in tests:
        try:
            print(f"Input data is: '{i}'")
            print(f"Temperature is now {input_temperature(i)}°C\n")
        except:
            print("Caught input_temperature error: "
                  f"invalid literal for int() with base 10: '{i}'\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
