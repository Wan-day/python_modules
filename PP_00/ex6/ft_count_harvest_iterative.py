def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    i: int = 1
    while (days):
        print(f"Day {i}")
        i += 1
        days -= 1
    print("Harvest time!")
