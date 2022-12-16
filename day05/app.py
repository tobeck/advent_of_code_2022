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

    rows_to_columns = [list(x) for x in zip(*list_of_stacks[:-1])]
    for row in rows_to_columns:
        result.append([x for x in row if x != ' '])

    return result


def parse_rearrangement_procedures(input_data):
    procedures = []
    for line in input_data:
        if line[0].isalpha():
            procedures.append([int(x) for x in line.split() if x.isdigit()])

    return procedures


def crate_mover_9000(stacks, procedures):

    for procedure in procedures:
        for i in range(procedure[0]):
            box_index = stacks[procedure[1] -
                               1].index(stacks[procedure[1] - 1][0])
            stacks[procedure[2] -
                   1].insert(0, stacks[procedure[1] - 1].pop(box_index))

    return stacks


def crate_mover_9001(stacks, procedures):

    for procedure in procedures:
        number_of_crates_to_move = procedure[0]
        # print(number_of_crates_to_move)

        crates_to_move = stacks[procedure[1] - 1][:number_of_crates_to_move]
        # crates_to_move.reverse()

        stacks[procedure[2] - 1].reverse()
        stacks[procedure[2] - 1].extend(crates_to_move)
        stacks[procedure[1] - 1] = stacks[procedure[1] -
                                          1][number_of_crates_to_move:]

    return stacks


def top_crate(stacks):
    return ''.join([x[0 - 1] for x in stacks])


def main():
    input_data = read_input()

    stacks = create_stacks(
        input_data)

    procedures = parse_rearrangement_procedures(input_data)

    stacks = crate_mover_9001(stacks, procedures)
    print(top_crate(stacks))

    # wrong TLMJSGGWH


if __name__ == "__main__":
    main()
