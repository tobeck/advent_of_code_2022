#!/usr/bin/env python

import string


def rucksack(rucksack):
    rucksack_size = len(rucksack)
    compartment_1 = rucksack[slice(0, rucksack_size // 2)]
    compartment_2 = rucksack[slice(rucksack_size // 2, rucksack_size)]

    return compartment_1, compartment_2


def item_arrangement_duplicate(compartment_1, compartment_2):
    duplicates = ', '.join(set(compartment_1).intersection(compartment_2))
    return duplicates


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

    print(
        f"{compartment_duplicate} priority: {priority_map[compartment_duplicate]}")

    return priority_map[compartment_duplicate]


def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        sum_priorities = 0

        for line in file:
            compartment_1, compartment_2 = rucksack(line)
            compartment_duplicate = item_arrangement_duplicate(
                compartment_1, compartment_2)
            sum_priorities += prioritize_item_arrangement(
                compartment_duplicate)

        print(sum_priorities)
        return sum_priorities


if __name__ == "__main__":
    main()


def test_main():
    assert main() == 157


def test_rucksack():
    assert rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == (
        'vJrwpWtwJgWr', 'hcsFMMfFFhFp')


def test_item_arrangement_duplicate():
    assert item_arrangement_duplicate(
        'vJrwpWtwJgWr', 'hcsFMMfFFhFp') == ('p')
    assert item_arrangement_duplicate(
        'jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL') == ('L')
    assert item_arrangement_duplicate(
        'PmmdzqPrV', 'vPwwTWBwg') == ('P')
    assert item_arrangement_duplicate(
        'wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn') == ('v')
    assert item_arrangement_duplicate(
        'ttgJtRGJ', 'QctTZtZT') == ('t')
    assert item_arrangement_duplicate(
        'CrZsJsPPZsGz', 'wwsLwLmpwMDw') == ('s')


def test_prioritize_item_arrangement():
    assert prioritize_item_arrangement('p') == 16
    assert prioritize_item_arrangement('L') == 38
    assert prioritize_item_arrangement('P') == 42
    assert prioritize_item_arrangement('v') == 22
    assert prioritize_item_arrangement('t') == 20
    assert prioritize_item_arrangement('s') == 19
