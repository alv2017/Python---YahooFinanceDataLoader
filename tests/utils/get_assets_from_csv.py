import unittest
import os
from YahooFinanceDataLoader import get_assets_from_csv

class Test_GetAssetsFromCSV(unittest.TestCase):
    def setUp(self):         
        # test data
        data_directory = os.path.dirname(__file__)
        self.test_file = os.path.join(data_directory, '../fixtures/assets.csv')
        self.field_list = ['Symbol', 'Company']
         
    def test_returns_list_of_assets(self):  
        actual_assets_list = get_assets_from_csv(self.test_file, self.field_list)
        expected_assests_list = ['AAPL', 'IBM', 'MSFT']
        self.assertEqual(actual_assets_list, expected_assests_list)

    def test_raise_error_if_file_not_exists(self):
        self.assertRaises(FileNotFoundError, get_assets_from_csv, 'nonexistant_file')

    
if __name__ == '__main__':
    unittest.main()       