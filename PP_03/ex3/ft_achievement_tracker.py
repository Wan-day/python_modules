#!/usr/bin/env python3

import random

ach_list: tuple[str, ...] = (
    "First Steps",
    "Beginner's Luck",
    "Quick Learner",
    "Getting Warmed Up",
    "Hello, World",
    "On a Roll",
    "Hot Streak",
    "Unstoppable",
    "Close Call",
    "Against All Odds",
    "Perfectionist",
    "Speed Demon",
    "Slow and Steady",
    "Night Owl",
    "Early Bird",
    "Treasure Hunter",
    "Coin Collector",
    "Pocket Full of Coins",
    "Big Spender",
    "Penny Pincher",
    "Explorer",
    "Pathfinder",
    "Lost and Found",
    "Dead End",
    "Back from the Brink",
    "Survivor",
    "Untouchable",
    "Glass Cannon",
    "Heavy Hitter",
    "Sharpshooter",
    "Combo Master",
    "Chain Reaction",
    "Overkill",
    "Pacifist",
    "Bug Squasher",
    "Easter Egg Hunter",
    "Secret Keeper",
    "Curious Mind",
    "Trial and Error",
    "Persistent",
    "Never Give Up",
    "Comeback Kid",
    "Lucky Seven",
    "Double Trouble",
    "Triple Threat",
    "Marathon Runner",
    "Sprinter",
    "High Roller",
    "Legend",
    "Completionist"
)

players: tuple[str, ...] = (
        "Aria",
        "Blaze",
        "Cipher",
        "Dusk",
        "Echo"
        )


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.achievements: set[str] = set()
        self.not_earned: set[str] = set()
        self.gen_achievements()
        self.unique_ach: set[str] = set(self.achievements)

    def gen_achievements(self) -> None:
        amount: int = random.randrange(0, int(len(ach_list) / 3))
        for _ in range(amount):
            temp: str = ach_list[random.randrange(0, len(ach_list))]
            self.achievements = self.achievements.union({temp})
        self.not_earned = set(ach_list).difference(self.achievements)

    def update_unique(self, ach: set[str]) -> None:
        self.unique_ach = self.unique_ach.difference(ach)

    def get_ach(self) -> set[str]:
        return self.achievements

    def get_not_earned(self) -> set[str]:
        return self.not_earned

    def get_unique(self) -> set[str]:
        return self.unique_ach

    def get_name(self) -> str:
        return self.name


def generate_stats(players: set[Player]) -> None:
    common_ach: set[str] = set(ach_list)
    for p in players:
        for temp in players:
            if (p.get_name() != temp.get_name()):
                p.update_unique(temp.get_ach())
        common_ach = common_ach.intersection(p.get_ach())
        print(
                f"Player {p.name} has these achievements:\n"
                f"{p.get_ach()}\n{len(p.get_ach())}\n"
                # "The player is missing these achievements: 'n"
                # f"{i.get_not_earned()}\n"
                # f"{len(i.get_not_earned())}"
                f"Unique achievements: "
                f"{p.get_unique()}"
                )
    print(f"Common achievements shared by everyone: {common_ach}")


def gen_player_achievements() -> set[Player]:
    player_list: set[Player] = set()
    for name in players:
        temp = Player(name)
        player_list = player_list.union({temp})
    generate_stats(player_list)
    return player_list


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()


if __name__ == "__main__":
    main()
