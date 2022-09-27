import unittest
from utils.FileUtils import FileUtils


class test_file_utils(unittest.TestCase):
    """test cases for test file utils"""

    def test_file_extension(self):
        with self.assertRaises(SystemExit):
            FileUtils.load_txt_file_from_path('/Data/test.jpeg')

    def test_file_not_exist(self):
        with self.assertRaises(SystemExit):
            FileUtils.load_txt_file_from_path('/Data/test.txt')


    def test_read_file(self):
        text_data = FileUtils.load_txt_file_from_path(
            './Data/customers.txt')
        input_len = 32

        self.assertEqual(len(text_data), input_len)
