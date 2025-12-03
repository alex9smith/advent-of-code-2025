from day_03 import maximum_joltage

INPUT = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

EXPECTED_JOLTAGE = [98, 89, 78, 92]


def test_maximum_joltage():
    for input, expected in zip(INPUT, EXPECTED_JOLTAGE):
        assert maximum_joltage(input) == expected
