from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class Direction(StrEnum):
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Rotation:
    direction: Direction
    distance: int

    @staticmethod
    def parse(line: str) -> "Rotation":
        return Rotation(direction=Direction(line[0]), distance=int(line[1:]))


INITIAL_POSITION = 50


class Dial:
    def __init__(self, initial_position: int = INITIAL_POSITION, size: int = 100):
        self.size = size
        self.current_position = initial_position
        self.times_touched_0 = 0

    def rotate(self, rotation: Rotation):
        match rotation.direction:
            case Direction.RIGHT:
                self.current_position = (
                    self.current_position + rotation.distance
                ) % self.size
            case Direction.LEFT:
                self.current_position = (
                    self.current_position - rotation.distance
                ) % self.size
            case _:
                raise ValueError(f"Unknown direction {rotation.direction}")

        if self.current_position == 0:
            self.times_touched_0 += 1


def count_times_pointed_zero(instructions: list[Rotation], dial: Dial = Dial()) -> int:
    for rotation in instructions:
        dial.rotate(rotation)

    return dial.times_touched_0


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    with p.open() as f:
        dial = Dial()
        while line := f.readline():
            dial.rotate(Rotation.parse(line))

    print(dial.times_touched_0)
