#!/usr/bin/env python3

import sys


class InvalidInput(Exception):
    template: str = "Invalid parameter: '{}'"

    def __init__(self, arg: str) -> None:
        self.message = self.template.format(arg)
        super().__init__(self.message)


class KeyExists(InvalidInput):
    template: str = "Item already exists: {}"


class InvalidValue(InvalidInput):
    template: str = "Invalid item quantity: {}"


class Inventory():
    def __init__(self, items: dict[str, int]) -> None:
        self.items: dict[str, int] = items
        self.item_count: int = sum(self.items.values())

    def add_item(self, item: dict[str, int]) -> None:
        try:
            key: str = ""
            for k in item.keys():
                key = str(k)
            if key in self.items.keys():
                raise KeyExists(key)
            self.items.update(item)
            self.item_count = sum(self.items.values())
            print(f"Item has been added to the inventory: {key}")
        except KeyExists as e:
            print(e)

    def generate_stats(self) -> None:
        print(f"Total amount of items in the inventory: {self.item_count}")
        biggest: int = max(self.items.values())
        lowest: int = min(self.items.values())
        b_item: str = ""
        l_item: str = ""
        for item in self.items:
            percentage: float = (self.items[item] / self.item_count) * 100
            percentage = round(percentage, 2)
            print(f"Item: '{item}' takes {percentage}% of the inventory'")
            if self.items[item] == biggest and b_item == "":
                b_item = item
            if self.items[item] == lowest and l_item == "":
                l_item = item
        print(
                f"Most abundant item: {b_item}\n"
                f"Least abundant item: {l_item}"
                )

    def get_items(self) -> dict[str, int]:
        return self.items

    def get_item_count(self) -> int:
        return self.item_count


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    temp: dict[str, int] = dict()
    args: list[str] = sys.argv[1:]
    for data in args:
        data = data.split(":", 1)
        key: str = str(data[0])
        try:
            if key in temp.keys():
                raise KeyExists(data[0])
            if (data[1].isdigit()):
                value: int = int(data[1])
                temp.update({key: value})
            else:
                raise InvalidValue(str(data))
        except InvalidInput as e:
            print(e)

    items = Inventory(temp)
    print(f"Items in the inventory: {items.get_items()}")
    items.generate_stats()
    items.add_item({"key": 2})


if __name__ == "__main__":
    main()
