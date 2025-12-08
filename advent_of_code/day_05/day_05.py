import re
from dataclasses import dataclass
from pathlib import Path

ID_RANGE = re.compile(r"^(\d+)-(\d+)$")


@dataclass
class Database:
    valid_ranges: list[tuple[int, int]]
    available_ingredients: list[int]

    @classmethod
    def parse(cls, raw: str) -> "Database":
        valid_ranges = []
        available_ingredients = []
        for line in raw.split("\n"):
            if match := ID_RANGE.search(line):
                start, end = int(match.group(1)), int(match.group(2))
                valid_ranges.append((start, end))
            elif line:
                available_ingredients.append(int(line))

        return Database(
            valid_ranges=valid_ranges, available_ingredients=available_ingredients
        )

    def count_fresh_ingredients(self):
        return sum(1 for ingredient in self.available_ingredients 
                  if any(start <= ingredient <= end for start, end in self.valid_ranges))


if __name__ == "__main__":
    file = Path(__file__).with_name("input.txt")
    with file.open("r") as f:
        INPUT = f.read()

    print("starting")

    db = Database.parse(INPUT)
    print("Part 1")
    print(db.count_fresh_ingredients())
