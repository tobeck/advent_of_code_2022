#!/usr/bin/env python

def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        number_of_subsets = 0

        for line in file:
            section_1 = line.split(',')[0]
            section_2 = line.split(',')[1]
            if pair_in_other(section_1, section_2) == True:
                number_of_subsets += 1

        print(number_of_subsets)
        return number_of_subsets


def pair_in_other(section_1, section_2):
    range_1_split = [int(i) for i in section_1.split('-')]
    range_1_set = set(i for i in range(
        range_1_split[0], range_1_split[1] + 1))

    range_2_split = [int(i) for i in section_2.split('-')]
    range_2_set = set(i for i in range(
        range_2_split[0], range_2_split[1] + 1))

    return range_1_set.issubset(range_2_set) or range_2_set.issubset(range_1_set)


def test_main():
    assert main() == 2


def test_pair_in_other():
    assert pair_in_other('2-4', '6-8') == False
    assert pair_in_other('2-8', '3-7') == True
    assert pair_in_other('2-6', '4-8') == False


if __name__ == "__main__":
    main()
