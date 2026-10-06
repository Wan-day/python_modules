#!/usr/bin/env python3

def secure_archive(fn: str, opt: str = "", data: str = "") -> tuple[bool, str]:
    if opt != 'r' and opt != 'w':
        return (False, f"[Error]: Incorrect option '{opt}'")
    try:
        with open(fn, opt) as file:
            if opt == "r":
                read_data: str = file.read()
                return (True, read_data)
            else:
                file.write(data)
                return (True, data)
    except (OSError, ValueError) as e:
        return (False, f"[Error]: {e}\n")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Test 1: reading ancient_fragment.txt")
    success, content = secure_archive("ancient_fragment.txt", "r")
    print(f"Success: {success}")
    print(f"Content: {content}\n")

    print("Test 2: writing to test.txt")
    success, content = secure_archive("test.txt", "w", "Archive entry #1")
    print(f"Success: {success}")
    print(f"Content: {content}\n")

    print("Test 3: reading nonexistent file")
    success, content = secure_archive("does_not_exist.txt", "r")
    print(f"Success: {success}")
    print(f"Content: {content}")


if __name__ == "__main__":
    main()
