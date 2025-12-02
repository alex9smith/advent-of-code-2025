import re

MATCH_PATTERN = re.compile(r"^(\d+)\1$")


def parse_input(input: str) -> list[tuple[int, int]]:
    ranges = input.strip().split(",")
    output = []
    for range in ranges:
        split = range.split("-")
        output.append((int(split[0]), int(split[1])))
    return output


def is_valid_id(id: int) -> bool:
    return not MATCH_PATTERN.search(str(id))


def find_all_invalid_ids(input: str) -> list[int]:
    parsed = parse_input(input)
    invalid_ids = []

    for start, finish in parsed:
        for id in range(start, finish + 1):
            if not is_valid_id(id):
                invalid_ids.append(id)

    return invalid_ids


if __name__ == "__main__":
    INPUT = "1-14,46452718-46482242,16-35,92506028-92574540,1515128146-1515174322,56453-79759,74-94,798-971,49-66,601-752,3428-4981,511505-565011,421819-510058,877942-901121,39978-50500,9494916094-9494978970,7432846301-7432888696,204-252,908772-990423,21425-25165,1030-1285,7685-9644,419-568,474396757-474518094,5252506279-5252546898,4399342-4505058,311262290-311393585,1895-2772,110695-150992,567521-773338,277531-375437,284-364,217936-270837,3365257-3426031,29828-36350"
    print("Part 1:")
    print(sum(find_all_invalid_ids(INPUT)))
