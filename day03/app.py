#!/usr/bin/env python

import string


def rucksack(rucksack):
    rucksack_size = len(rucksack)
    compartment_1 = rucksack[slice(0, rucksack_size // 2)]
    compartment_2 = rucksack[slice(rucksack_size // 2, rucksack_size)]

    return compartment_1, compartment_2


def item_duplicate(*args):
    list_of_sets = []
    for i in args:
        list_of_sets.append(set(i))

    return " ".join(set.intersection(*list_of_sets))


def prioritize_item_arrangement(compartment_duplicate):

    if compartment_duplicate.islower():
        alphabet = list(string.ascii_lowercase)
        letter_priority = 0
    elif compartment_duplicate.isupper():
        alphabet = list(string.ascii_uppercase)
        letter_priority = 26

    priority_map = {key: None for key in alphabet}

    for key in alphabet:
        letter_priority += 1
        priority_map[key] = letter_priority

    return priority_map[compartment_duplicate]


def group_badge(list_chunks):
    group_duplicates = item_duplicate(*list_chunks)

    return group_duplicates


def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        # Part 1
        sum_priorities = 0
        all_lines_list = []

        for line in file:
            all_lines_list.append(line.strip())

            compartment_1, compartment_2 = rucksack(line)
            compartment_duplicate = item_duplicate(
                compartment_1.strip(), compartment_2.strip())
            sum_priorities += prioritize_item_arrangement(
                compartment_duplicate)

        # Part 2
        sum_group_priorities = 0
        chunks = 3

        list_chunks = [all_lines_list[i * chunks:(i + 1) * chunks]
                       for i in range((len(all_lines_list) + chunks - 1) // chunks)]

        for chunk in list_chunks:
            group_badge_letter = group_badge(chunk)
            sum_group_priorities += prioritize_item_arrangement(
                group_badge_letter)

        print(f'Part One, sum of priorities is: {sum_priorities}')
        print(f'Part Two, sum of group priorities is: {sum_group_priorities}')
        return sum_priorities, sum_group_priorities


if __name__ == "__main__":
    main()


def test_main():
    assert main() == (157, 70)


def test_rucksack():
    assert rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == (
        'vJrwpWtwJgWr', 'hcsFMMfFFhFp')


def test_item_duplicate():
    assert item_duplicate(
        'vJrwpWtwJgWr', 'hcsFMMfFFhFp') == ('p')
    assert item_duplicate(
        'jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL') == ('L')
    assert item_duplicate(
        'PmmdzqPrV', 'vPwwTWBwg') == ('P')
    assert item_duplicate(
        'wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn') == ('v')
    assert item_duplicate(
        'ttgJtRGJ', 'QctTZtZT') == ('t')
    assert item_duplicate(
        'CrZsJsPPZsGz', 'wwsLwLmpwMDw') == ('s')


def test_prioritize_item_arrangement():
    assert prioritize_item_arrangement('p') == 16
    assert prioritize_item_arrangement('L') == 38
    assert prioritize_item_arrangement('P') == 42
    assert prioritize_item_arrangement('v') == 22
    assert prioritize_item_arrangement('t') == 20
    assert prioritize_item_arrangement('s') == 19


def test_group_badge():
    assert group_badge(['vJrwpWtwJgWrhcsFMMfFFhFp',
                       'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']) == 'r'
    assert group_badge(['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                       'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']) == 'Z'
