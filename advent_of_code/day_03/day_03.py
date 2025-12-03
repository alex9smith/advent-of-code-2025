from pathlib import Path


def largest_n_digits(bank: str, n: int) -> str:
    bank_length = len(bank)
    result = []

    for i, battery in enumerate(bank):
        while result and len(result) + (bank_length - i) > n and result[-1] < battery:
            result.pop()
        if len(result) < n:
            result.append(battery)

    return "".join(result)


if __name__ == "__main__":
    file = Path(__file__).with_name("input.txt")
    with file.open() as f:
        banks = [line.strip() for line in f.readlines()]

    print("Part 1")
    print(sum(int(largest_n_digits(bank, 2)) for bank in banks))

    print("Part 2")
    print(sum(int(largest_n_digits(bank, 12)) for bank in banks))
