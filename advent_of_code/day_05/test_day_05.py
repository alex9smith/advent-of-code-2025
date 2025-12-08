from day_05 import Database

TEST_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


class TestDatabase:
    def test_parse(self):
        db = Database.parse(TEST_INPUT)
        assert db.valid_ranges == [(3, 5), (10, 14), (16, 20), (12, 18)]
        assert db.available_ingredients == [1, 5, 8, 11, 17, 32]

    def test_count_fresh_ingredients(self):
        db = Database.parse(TEST_INPUT)
        assert db.count_fresh_ingredients() == 3
