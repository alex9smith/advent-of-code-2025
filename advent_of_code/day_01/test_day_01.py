from day_01 import Dial, Direction, Rotation, count_times_pointed_zero
from pytest import fixture


@fixture
def dial():
    return Dial()


class TestDial:
    def test_rotating_right_adds(self, dial):
        dial.rotate(Rotation(Direction.RIGHT, 1))
        assert dial.current_position == 51

    def test_rotating_left_subtracts(self, dial):
        dial.rotate(Rotation(Direction.LEFT, 1))
        assert dial.current_position == 49

    def test_rotating_right_rolls_over(self, dial):
        dial.rotate(Rotation(Direction.RIGHT, 50))
        assert dial.current_position == 0

    def test_rotating_left_rolls_over(self, dial):
        dial.rotate(Rotation(Direction.LEFT, 51))
        assert dial.current_position == 99


def test_count_times_pointed_zero():
    instructions = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    assert (
        count_times_pointed_zero([Rotation.parse(line) for line in instructions]) == 3
    )
