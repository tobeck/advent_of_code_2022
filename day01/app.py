#!/usr/bin/env python

def calculate_elf_inventory(inventory_lines):
    """calculate_max_calories sums up the amount of calories each elf is carrying
    and return the sum of the one who carries the most, max_calories"""

    # List of how many calories each elf is carrying.
    sum_calories_list = []
    # The sum of calories that an elf is carrying.
    sum = 0

    for line in inventory_lines:
        # If there is a newline, a new elf needs to be summed up.
        if line.strip() == "":
            sum_calories_list.append(sum)
            sum = 0
        else:
            sum += int(line)

    return sum_calories_list


def main():
    """Main function"""

    with open('elf_inventory.txt', mode='r', encoding='utf-8') as file:
        inventory_lines = file.readlines()

    sum_calories_list = calculate_elf_inventory(
        inventory_lines=inventory_lines)

    sum_calories_list.sort()

    print("The most calories carried is:", max(sum_calories_list))
    print("Top three elfs carry:", sum(sum_calories_list[-3:]))


if __name__ == "__main__":
    main()
