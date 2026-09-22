def count_days(days):
    if (days == 0):
        return
    else:
        count_days(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(days)
    print("Harvest time!")
