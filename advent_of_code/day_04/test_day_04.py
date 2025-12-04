from day_04 import find_number_of_accessible_rolls
from grid import Grid

DATA = [
    [c for c in r]
    for r in """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")
]


def test_find_number_of_accessible_rolls():
    grid = Grid(DATA)
    assert find_number_of_accessible_rolls(grid) == 13
