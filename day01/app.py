#!/usr/bin/env python

def most_calories_carried(inventory_lines):
    """most_calories_carried sums up the amount of calories each elf is carrying
    and return the sum of the one who carries the most, most_calories_carried"""

    # List of how many calories each elf is carrying.
    elf_calories = []
    # The sum of calories that an elf is carrying.
    elf_sum = 0

    for line in inventory_lines:
        # If there is a newline, a new elf needs to be summed up.
        if line.strip() == "":
            elf_calories.append(elf_sum)
            elf_sum = 0
        else:
            elf_sum += int(line)

    most_calories_carried = max(elf_calories)

    return most_calories_carried


def main():
    """Main function"""

    with open('elf_inventory.txt', mode='r', encoding='utf-8') as file:
        inventory_lines = file.readlines()

    print(most_calories_carried(inventory_lines=inventory_lines))


if __name__ == "__main__":
    main()
