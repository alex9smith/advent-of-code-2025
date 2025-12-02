from day_02 import find_all_invalid_ids, parse_input, part_1_is_valid_id

INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
TEST_IDS = [
    (11, False),
    (22, False),
    (99, False),
    (1188511885, False),
    (222222, False),
    (446446, False),
    (38593859, False),
    (12, True),
    (13, True),
    (1024, True),
    (938475690, True),
    (340570234975345, True),
    (3459078987986345, True),
]


def test_parse_input():
    parsed = parse_input(INPUT)
    assert parsed[0] == (11, 22)
    assert parsed[-1] == (2121212118, 2121212124)


def test_part_1_is_valid_id():
    for id, is_valid in TEST_IDS:
        assert part_1_is_valid_id(id) == is_valid


def test_find_all_invalid_ids_part_1():
    assert find_all_invalid_ids(INPUT) == [
        11,
        22,
        99,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
    ]


def test_find_all_invalid_ids_part_2():
    assert find_all_invalid_ids(INPUT, part_1=False) == [
        11,
        22,
        99,
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121,
    ]
