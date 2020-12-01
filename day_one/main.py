'''
--- Day 1: Report Repair ---

--- Part One ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''
def add_numbers(first_number, second_number, third_number = None):
    '''
    Add numbers together
    '''
    if third_number is not None:
        return first_number + second_number + third_number
    return first_number + second_number

def check_numbers(first_number, second_number, third_number = None):
    '''
    Check if numbers add up to 2020
    '''
    return add_numbers(first_number, second_number, third_number) == 2020

def get_list_subset(numbers, number, max_index):
    '''
    Get subset of the list of numbers
    '''
    count = numbers.index(number)
    return numbers[count:max_index]

def multiply_numbers(number, second_number, third_number = None):
    '''
    Multiply numbers together
    '''
    if third_number is not None:
        return number * second_number * third_number
    return number * second_number

def report_repair_part_one(numbers):
    '''
    '''
    max_index = len(numbers) - 1
    for number in numbers:
        for second_number in get_list_subset(numbers, number, max_index):
            if check_numbers(number, second_number):
                return multiply_numbers(number, second_number)

def report_repair_part_two(numbers):
    '''
    '''
    max_index = len(numbers) - 1
    for number in numbers:
        for second_number in get_list_subset(numbers, number, max_index):
            for third_number in get_list_subset(numbers, second_number, max_index):
                if check_numbers(number, second_number, third_number):
                    return multiply_numbers(number, second_number, third_number)