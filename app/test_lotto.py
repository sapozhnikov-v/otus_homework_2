from lotto import Card, check_answer_is_integer, check_field_is_not_empty, check_choose_is_valid
from pytest import fixture, mark, param


def test_generate_card():
    card = Card.generate_card()
    card_without_spaces = []
    card_numbers = []
    for row in card:
        new_row = []
        for item in row:
            if isinstance(item, int):
                card_numbers.append(item)
                new_row.append(item)
        card_without_spaces.append(new_row)

    for row in card_without_spaces:
        assert len(card_numbers) == len(set(card_numbers))
        assert row == sorted(row)


@fixture
def card():
    card = Card('Alice')
    card.card = [[' ', 5, 13, 50, ' ', 61, ' ', 73, ' '],
                 [19, ' ', 28, 43, ' ', 57, ' ', ' ', 63],
                 [' ', ' ', ' ', 11, ' ', 24, 32, 56, 78]]
    return card


@mark.parametrize("barrel, expected_index", [
    param(
        5, (0, 1),
        id="has barrel"
    ),
    param(
        6, None,
        id="has not barrel"
    )])
def test_get_index_number(card, barrel, expected_index):
    index = card.get_index_number(barrel)
    assert index == expected_index


def test_cross_out(card):
    barrel = 11
    card.cross_out(barrel)
    assert card.card == [[' ', 5, 13, 50, ' ', 61, ' ', 73, ' '],
                         [19, ' ', 28, 43, ' ', 57, ' ', ' ', 63],
                         [' ', ' ', ' ', '-', ' ', 24, 32, 56, 78]]


@mark.parametrize("answer, expected_result", [
    param(
        '', False,
        id="field empty"
    ),
    param(
        ' ', False,
        id="field empty with whitespace"
    ),
    param(
        'Bob', True,
        id="correct answer"
    )])
def test_check_field_is_not_empty(answer, expected_result):
    result = check_field_is_not_empty(answer)
    assert result == expected_result


@mark.parametrize("args, expected_result", [
    param(
        ('y', 'n', ''), False,
        id="empty field"
    ),
    param(
        ('y', 'n', 'd'), False,
        id="incorrect answer"
    ),
    param(
        ('y', 'n', 'y'), True,
        id="correct answer"
    ),
    param(
        ('человек', 'компьютер', 'ЧелоВек'), True,
        id="correct answer, higher case"
    )])
def test_check_choose_is_valid(args, expected_result):
    result = check_choose_is_valid(*args)
    assert result == expected_result


@mark.parametrize("answer, expected_result", [
    param(
        '', False,
        id="empty field"
    ),
    param(
        'd', False,
        id="not number"
    ),
    param(
        '-3', False,
        id="not positive number"
    ),
    param(
        '4', True,
        id="correct answer"
    )])
def test_check_answer_is_integer(answer, expected_result):
    result = check_answer_is_integer(answer)
    assert result == expected_result
