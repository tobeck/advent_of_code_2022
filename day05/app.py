#!/usr/bin/env python

import csv


def parse_stack_headers():
    with open('test_data.txt', mode='r', encoding='utf-8') as file_data:
        for line in file_data:
            if line != '\n':
                previous_line = line
            elif line == '\n':
                break

        stack_headers = [x for x in previous_line.strip()]


def main():
    parse_stack_headers()


if __name__ == "__main__":
    main()


def test_parse_stack_headers():
    assert parse_stack_headers() == ([1, 2, 3])
