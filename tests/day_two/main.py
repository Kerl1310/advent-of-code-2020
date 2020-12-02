import unittest

from helpers.inputs import read_file
from day_two.main import *

TEST_DATA = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc' ]

class TestCountOccurrences(unittest.TestCase):
    '''
    '''

    def test_count_occurrences_one(self):
        '''
        '''
        outcome = count_occurrences('a', 'abcde')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 1)

    def test_count_occurrences_nine(self):
        '''
        '''
        outcome = count_occurrences('c', 'ccccccccc')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 9)

    def test_count_occurrences_using_invalid_type(self):
        '''
        '''
        outcome = count_occurrences(1, 'cdefg')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 0)

    def test_count_occurrences_using_empty_char(self):
        '''
        '''
        outcome = count_occurrences('', 'cdefg')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 0)

    def test_count_occurrences_using_empty_password_string(self):
        '''
        '''
        outcome = count_occurrences('c', '')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 0)


class TestCheckPassword(unittest.TestCase):
    '''
    '''

    def test_password_is_valid(self):
        '''
        '''
        outcome = check_password(1, 3, 'a', 'abcde')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 1)

    def test_password_is_invalid(self):
        '''
        '''
        outcome = check_password(1, 3, 'b', 'cdefg')
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 0)


class TestParseData(unittest.TestCase):
    '''
    '''

    def test_using_mock_data(self):
        '''
        '''
        outcome = parse_data(TEST_DATA)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 2)

    def test_using_input(self):
        '''
        '''
        data = read_file("tests\day_two\input.txt")
        outcome = parse_data(data)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 416)
        

class TestParseDataPartTwo(unittest.TestCase):
    '''
    '''

    def test_using_mock_data(self):
        '''
        '''
        outcome = parse_data_part_two(TEST_DATA)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 1)

    def test_using_input(self):
        '''
        '''
        data = read_file("tests\day_two\input.txt")
        outcome = parse_data_part_two(data)
        self.assertIs(type(outcome), int)
        self.assertEqual(outcome, 688)