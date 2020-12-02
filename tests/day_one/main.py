import unittest

from helpers.input_helper import read_number_input_as_list
from day_one.main import *

TEST_DATA = [1721,
979,
366,
299,
675,
1456]

class TestReportRepairPartOne(unittest.TestCase):
    '''
    '''

    def test_report_repair_part_one_using_test_data(self):
        '''
        '''
        outcome = report_repair_part_one(TEST_DATA)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 514579)

    def test_report_repair_part_one(self):
        '''
        '''
        inputs = read_number_input_as_list("tests\day_one\input.txt")
        outcome = report_repair_part_one(inputs)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 956091)
    

class TestAddNumbers(unittest.TestCase):
    '''
    '''
    
    def test_add_numbers_three_numbers(self):
        '''
        '''
        outcome = add_numbers(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2])
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 3066)

    def test_add_numbers_using_two_numbers(self):
        '''
        '''
        outcome = add_numbers(TEST_DATA[0], TEST_DATA[1])
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 2700)


class TestCheckNumbers(unittest.TestCase):
    '''
    '''
    
    def test_check_numbers_using_two_numbers(self):
        '''
        '''
        outcome = check_numbers(TEST_DATA[0], TEST_DATA[1])
        self.assertIs(type(outcome), bool)
        self.assertFalse(outcome)
    
    def test_check_numbers_using_two_numbers_positive(self):
        '''
        '''
        outcome = check_numbers(TEST_DATA[0], TEST_DATA[3])
        self.assertIs(type(outcome), bool)
        self.assertTrue(outcome)

    def test_check_numbers_using_three_numbers(self):
        '''
        '''
        outcome = check_numbers(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2])
        self.assertIs(type(outcome), bool)
        self.assertFalse(outcome)


class TestMultiplyNumbers(unittest.TestCase):
    '''
    '''
    
    def test_multiply_numbers_using_two_numbers(self):
        '''
        '''
        outcome = multiply_numbers(TEST_DATA[0], TEST_DATA[1])
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 1684859)

    def test_multiply_numbers_using_three_numbers(self):
        '''
        '''
        outcome = multiply_numbers(TEST_DATA[0], TEST_DATA[1], TEST_DATA[2])
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 616658394)


class TestGetListSubset(unittest.TestCase):
    '''
    '''
    
    def test_get_list_subset(self):
        '''
        '''
        outcome = get_list_subset(TEST_DATA, TEST_DATA[0], len(TEST_DATA) - 1)
        self.assertIs(type(outcome), list)
        self.assertEqual(len(outcome), len(TEST_DATA) - 1)

    def test_get_list_subset(self):
        '''
        '''
        outcome = get_list_subset(TEST_DATA, TEST_DATA[1], len(TEST_DATA) - 1)
        self.assertIs(type(outcome), list)
        self.assertEqual(len(outcome), len(TEST_DATA) - 2)

        
class TestReportRepairPartTwo(unittest.TestCase):
    '''
    '''
    
    def test_report_repair_part_two_using_test_data(self):
        '''
        '''
        outcome = report_repair_part_two(TEST_DATA)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 241861950)

    def test_report_repair_part_two(self):
        '''
        '''
        inputs = read_number_input_as_list("tests\day_one\input.txt")
        outcome = report_repair_part_two(inputs)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 79734368)