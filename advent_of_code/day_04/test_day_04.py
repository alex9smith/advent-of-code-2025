from day_04 import (
    find_number_of_accessible_rolls,
    remove_accessible_rolls,
    remove_all_possible_accessible_rolls,
)
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


def test_remove_accessible_rolls():
    grid = Grid(DATA)
    grid, removed = remove_accessible_rolls(grid)
    assert removed == 13


def test_remove_all_possible_accessible_rolls():
    grid = Grid(DATA)
    assert remove_all_possible_accessible_rolls(grid) == 43
