from pathlib import Path

from grid import Grid


def contains_fewer_than_four_rolls(surrounding: list[str]) -> bool:
    return surrounding.count("@") < 4


def find_number_of_accessible_rolls(grid: Grid[str]) -> int:
    accessible_rolls = 0
    for row in range(grid.rows):
        for col in range(grid.cols):
            if grid.get(row, col) == "@":
                surrounding = grid.get_surrounding(row, col, wrap=False)
                if contains_fewer_than_four_rolls(surrounding):
                    accessible_rolls += 1
    return accessible_rolls


if __name__ == "__main__":
    file = Path(__file__).with_name("input.txt")
    with file.open("r") as f:
        data = [[c for c in line.strip()] for line in f.readlines()]

    grid = Grid(data)

    print("Part 1")
    print(find_number_of_accessible_rolls(grid))
