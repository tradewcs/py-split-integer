from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(15, 4)) == 15


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert all(num == 5 for num in split_integer(25, 5))


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    splited = split_integer(57, 1)
    assert len(splited) == 1
    assert splited[0] == 57


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    splited = split_integer(19, 4)
    assert sorted(splited) == splited


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    splited = split_integer(5, 7)
    assert splited.count(0) == 2
