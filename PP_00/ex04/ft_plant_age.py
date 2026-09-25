def ft_plant_age() -> None:
    age: int = int(input("Enter plange age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")
