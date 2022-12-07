#!/usr/bin/env python

import pytest


def read_input():
    file_data = open('test_data.txt', mode='r', encoding='utf-8')
    return file_data


def parse_stack_headers(input_data):
    for line in input_data:
        if line != '\n':
            previous_line = line.strip()
        elif line == '\n':
            break

    stack_headers = list(
        filter(None, [x.strip(' ') for x in previous_line]))

    result = [int(x) for x in stack_headers]

    return result


def main():
    input_data = read_input()
    parse_stack_headers(input_data=input_data)


if __name__ == "__main__":
    main()


@pytest.fixture
def test_data():
    return read_input()


def test_parse_stack_headers(test_data):
    assert parse_stack_headers(test_data) == ([1, 2, 3])
