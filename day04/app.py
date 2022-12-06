#!/usr/bin/env python

def pair_in_other(section_1, section_2, method):
    range_1_split = [int(i) for i in section_1.split('-')]
    range_1_set = set(i for i in range(
        range_1_split[0], range_1_split[1] + 1))

    range_2_split = [int(i) for i in section_2.split('-')]
    range_2_set = set(i for i in range(
        range_2_split[0], range_2_split[1] + 1))

    if method == 'issubset':
        result = range_1_set.issubset(
            range_2_set) or range_2_set.issubset(range_1_set)
        print(result)
    elif method == 'intersection':
        if range_1_set.intersection(
                range_2_set) or range_2_set.intersection(range_1_set) == True:
            result = True
        else:
            result = False

    return result


def main(method):
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        number_of_subsets = 0

        for line in file:
            section_1 = line.split(',')[0]
            section_2 = line.split(',')[1]
            if pair_in_other(section_1, section_2, method=method) == True:
                number_of_subsets += 1

        print(number_of_subsets)
        return number_of_subsets


def test_main():
    assert main(method='issubset') == 2
    assert main(method='intersection') == 4


def test_pair_in_other():
    assert pair_in_other('2-4', '6-8', 'issubset') == False
    assert pair_in_other('2-8', '3-7', 'issubset') == True
    assert pair_in_other('2-6', '4-8', 'issubset') == False


if __name__ == "__main__":
    main(method='intersection')
