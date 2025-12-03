from pathlib import Path


def maximum_joltage(bank: str) -> int:
    largest_not_last = max(bank[:-1])
    search_start = bank.find(largest_not_last)

    largest_second_digit = "0"
    for battery in bank[(search_start + 1) :]:
        if battery > largest_second_digit:
            largest_second_digit = battery

    return int(largest_not_last + largest_second_digit)


def largest_12_digits(bank: str) -> str:
    n = len(bank)
    result = []

    for i, battery in enumerate(bank):
        while result and len(result) + (n - i) > 12 and result[-1] < battery:
            result.pop()
        if len(result) < 12:
            result.append(battery)

    return "".join(result)


if __name__ == "__main__":
    file = Path(__file__).with_name("input.txt")
    with file.open() as f:
        banks = [line.strip() for line in f.readlines()]

    print("Part 1")
    print(sum(maximum_joltage(bank) for bank in banks))

    print("Part 2")
    print(sum(int(largest_12_digits(bank)) for bank in banks))
