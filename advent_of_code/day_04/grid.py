from typing import Generic, TypeVar

T = TypeVar("T")


class Grid(Generic[T]):
    def __init__(self, data: list[list[T]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def get(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def set(self, row: int, col: int, value: T):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise ValueError("Index out of range")

    def get_surrounding(self, row: int, col: int, wrap=False):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        surrounding: list[T] = []

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if wrap:
                r = r % self.rows
                c = c % self.cols
                surrounding.append(self.data[r][c])
            else:
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    surrounding.append(self.data[r][c])

        return surrounding
