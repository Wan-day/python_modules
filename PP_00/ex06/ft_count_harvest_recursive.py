def count_days(days: int) -> None:
    if (days == 0):
        return
    else:
        count_days(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    count_days(days)
    print("Harvest time!")
