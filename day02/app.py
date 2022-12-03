#!/usr/bin/env python

from typing import ChainMap


def parse_input(line):
    challenger_input = line.split()[0]
    user_input = line.split()[1]

    desired_outcome_map = {
        'X': 'Loss',
        'Y': 'Draw',
        'Z': 'Win'
    }

    desired_outcome = desired_outcome_map[user_input]

    return desired_outcome, challenger_input


def round(desired_outcome, challenger):

    winner_condition = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    strategy_points = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    points = 0

    if desired_outcome == 'Draw':
        points = 3 + strategy_points[challenger]
        return desired_outcome, points

    elif desired_outcome == 'Win':
        winner_strategy = winner_condition[challenger]
        points = 6 + strategy_points[winner_strategy]
        return desired_outcome, points

    else:
        losing_strategy = [
            k for k, v in winner_condition.items() if v == challenger][0]
        points = strategy_points[losing_strategy]
        return desired_outcome, points


def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        score = 0
        for line in file:
            desired_outcome, challenger = parse_input(line)
            result, points = round(desired_outcome, challenger)
            print(result, points)
            score += points

    print(score)
    return score


def test_result():
    assert main() == 12


def test_parse_input():
    assert parse_input('A Y') == ('Draw', 'A')


def test_round():
    assert round('Draw', 'A') == ('Draw', 4)
    assert round('Loss', 'B') == ('Loss', 1)
    assert round('Win', 'C') == ('Win', 7)


if __name__ == "__main__":
    main()
