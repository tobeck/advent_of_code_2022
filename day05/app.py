#!/usr/bin/env python


def read_input():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        return file.readlines()


def create_stacks(input_data):
    result = []

    list_of_stacks = []
    for line in input_data:
        if line != '\n':
            list_of_stacks.append([x for x in list(line[1::4])])
        else:
            break

    rows_to_columns = [list(x) for x in zip(*list_of_stacks)]
    for row in rows_to_columns:
        result.append([x for x in row if x != ' '])

    return result


def parse_rearrangement_procedures(input_data):
    procedures = []
    for line in input_data:
        if line[0].isalpha():
            procedures.append([int(x) for x in line.split() if x.isdigit()])

    return procedures


def move_crates(stacks, procedures):

    for procedure in procedures:
        crate_index = stacks[procedure[1]].index(
            stacks[procedure[1]][procedure[0] - 1])
        print(crate_index)

        stacks[procedure[2] - 1].insert(
            0, stacks[procedure[1] - 1].pop(crate_index))

        print(stacks)


def main():
    input_data = read_input()

    stacks = create_stacks(
        input_data)

    procedures = parse_rearrangement_procedures(input_data)

    move_crates(stacks, procedures)


if __name__ == "__main__":
    main()
