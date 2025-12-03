from day_03 import largest_12_digits, maximum_joltage

INPUT = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

EXPECTED_JOLTAGE = [98, 89, 78, 92]
EXPECTED_12_LARGEST = ["987654321111", "811111111119", "434234234278", "888911112111"]


def test_largest_12_digits():
    for input, expected in zip(INPUT, EXPECTED_12_LARGEST):
        assert largest_12_digits(input) == expected


def test_maximum_joltage():
    for input, expected in zip(INPUT, EXPECTED_JOLTAGE):
        assert maximum_joltage(input) == expected
