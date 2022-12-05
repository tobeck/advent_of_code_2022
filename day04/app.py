#!/usr/bin/env python

def main():
    with open('test_data.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            print(line)


if __name__ is "__main__":
    main()
