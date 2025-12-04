from advent_of_code.day_04.grid import Grid


def test_grid_init():
    data = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
    grid = Grid(data)
    assert grid.rows == 3
    assert grid.cols == 5


def test_get():
    data = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
    grid = Grid(data)
    assert grid.get(0, 0) == 0
    assert grid.get(1, 2) == 7
    assert grid.get(2, 4) == 14
    assert grid.get(-1, 0) is None
    assert grid.get(3, 0) is None
    assert grid.get(0, 5) is None


def test_get_surrounding_no_wrap():
    data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    grid = Grid(data)

    # Center
    assert grid.get_surrounding(1, 1, wrap=False) == [0, 1, 2, 3, 5, 6, 7, 8]

    # Corner
    assert grid.get_surrounding(0, 0, wrap=False) == [1, 3, 4]

    # Edge
    assert grid.get_surrounding(0, 1, wrap=False) == [0, 2, 3, 4, 5]


def test_get_surrounding_with_wrap():
    data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    grid = Grid(data)

    # Corner with wrap
    assert grid.get_surrounding(0, 0, wrap=True) == [8, 6, 7, 2, 1, 5, 3, 4]

    # Center with wrap (same as no wrap)
    assert grid.get_surrounding(1, 1, wrap=True) == [0, 1, 2, 3, 5, 6, 7, 8]
