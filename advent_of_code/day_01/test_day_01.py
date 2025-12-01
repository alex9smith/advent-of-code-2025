from day_01 import (
    Dial,
    Direction,
    Rotation,
    count_times_passed_zero,
    count_times_pointed_zero,
)
from pytest import fixture

INSTRUCTIONS = [
    Rotation.parse(line)
    for line in [
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
]


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

    def test_rotating_right_counts_passing_0(self, dial):
        dial.rotate(Rotation(Direction.RIGHT, 50))
        assert dial.times_passed_0 == 1

    def test_rotating_left_counts_passing_0(self, dial):
        dial.rotate(Rotation(Direction.LEFT, 60))
        assert dial.times_passed_0 == 1

    def test_rotating_left_from_0_doesnt_count_passing(self):
        dial = Dial(initial_position=0)
        dial.rotate(Rotation(Direction.LEFT, 1))
        assert dial.times_passed_0 == 0

    def test_rotating_right_from_0_doesnt_count_passing(self):
        dial = Dial(initial_position=0)
        dial.rotate(Rotation(Direction.RIGHT, 1))
        assert dial.times_passed_0 == 0

    def test_rotating_right_more_than_once_counts_all(self, dial: Dial):
        dial.rotate(Rotation(Direction.RIGHT, 300))
        assert dial.times_passed_0 == 3

    def test_rotating_right_more_than_once_starting_from_0_counts_all(self):
        dial = Dial(initial_position=0)
        dial.rotate(Rotation(Direction.RIGHT, 350))
        assert dial.times_passed_0 == 3

    def test_rotating_left_more_than_once_starting_from_0_counts_all(self):
        dial = Dial(initial_position=0)
        dial.rotate(Rotation(Direction.LEFT, 350))
        assert dial.times_passed_0 == 3

    def test_rotating_left_more_than_once_counts_all(self, dial: Dial):
        dial.rotate(Rotation(Direction.LEFT, 300))
        assert dial.times_passed_0 == 3

    def test_rotating_right_to_and_past_0_only_counts_once(self):
        dial = Dial(initial_position=99)
        dial.rotate(Rotation(Direction.RIGHT, 1))
        assert dial.current_position == 0
        dial.rotate(Rotation(Direction.RIGHT, 1))
        assert dial.current_position == 1
        assert dial.times_passed_0 == 1

    def test_rotating_left_to_and_past_0_only_counts_once(self):
        dial = Dial(initial_position=1)
        dial.rotate(Rotation(Direction.LEFT, 1))
        assert dial.current_position == 0
        dial.rotate(Rotation(Direction.LEFT, 1))
        assert dial.current_position == 99
        assert dial.times_passed_0 == 1


def test_count_times_pointed_zero():
    assert count_times_pointed_zero(INSTRUCTIONS) == 3


def test_count_times_passed_zero():
    assert count_times_passed_zero(INSTRUCTIONS) == 6
