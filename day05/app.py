#!/usr/bin/env python

import csv


def parse_stack_headers():
    with open('test_data.txt', mode='r', encoding='utf-8') as file_data:
        for line in file_data:
            if line != '\n':
                previous_line = line.strip()
            elif line == '\n':
                break

        stack_headers = list(
            filter(None, [x.strip(' ') for x in previous_line]))

        result = [int(x) for x in stack_headers]

        return result


def main():
    parse_stack_headers()


if __name__ == "__main__":
    main()


def test_parse_stack_headers():
    assert parse_stack_headers() == ([1, 2, 3])
