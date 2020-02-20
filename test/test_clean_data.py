import unittest
from cleanning.input import Reader
from cleanning.copy import Copy

class TestImportData(unittest.TestCase):

    def test_be_able_to_import_data_from_file(self):
        obj = Reader()
        actual = obj.read('test/test_file.csv')
        with open('test/test_file.csv', 'r') as reader:
            expect = reader.read()
        self.assertEqual(actual, expect)

class TestCopyData(unittest.TestCase):

    def test_be_able_to_create_right_list_from_invalid_format_csv(self):
        obj = Reader()
        obj = Copy(Reader)
        obj.construct()
        actual = obj.data

if __name__ == '__main__':
    unittest.main()
