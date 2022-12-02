#!/usr/bin/env python

from typing import ChainMap


def parse_input(line):
    challenger = line.split()[0]
    user = line.split()[1]

    translation_map = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    user_translated = translation_map[user]

    return user_translated, challenger


def round(user, challenger):

    winner_condition = {
        'A': ['C', 1],
        'B': ['A', 2],
        'C': ['B', 3]
    }

    challenger_loss = winner_condition[user]

    points = 0

    if user == challenger:
        result = 'Draw'
        points = 3 + winner_condition[user][1]
        return result, points
    elif challenger in challenger_loss:
        result = 'Win'
        points = 6 + winner_condition[user][1]
        return result, points
    else:
        result = 'Loss'
        points = winner_condition[user][1]
        return result, points


def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        score = 0
        for line in file:
            user, challenger = parse_input(line)
            result, points = round(user, challenger)
            score += points

    print(score)
    return score


def test_result():
    assert main() == 15


def test_round():
    assert round("B", "A") == ('Win', 8)
    assert round("A", "A") == ('Draw', 4)
    assert round("C", "A") == ('Loss', 3)
    assert round("C", "B") == ('Win', 9)
    assert round("B", "B") == ('Draw', 5)
    assert round("A", "B") == ('Loss', 1)


if __name__ == "__main__":
    main()
