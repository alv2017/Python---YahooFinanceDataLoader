import unittest
import os
import csv
from YahooFinanceDataLoader import get_assets_from_csv

class Test_GetAssetsFromCSV(unittest.TestCase):
    def setUp(self):        
        data = [{"Symbol":"AAPL", "Company":"Apple"},                
                {"Symbol":"IBM", "Company":"IBM"},
                {"Symbol":"MSFT", "Company":"Microsoft"},
            ]   
        # we will create a test file: assets.csv
        data_directory = os.path.dirname(__file__)
        file_name = "assets.csv"
        self.test_file = os.path.join(data_directory, file_name)
        self.field_list = ['Symbol', 'Company']
        
        with open(self.test_file, 'w', newline='') as csvfile:
            fieldnames = self.field_list
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)     
        
    def tearDown(self):
        # we will remove a test file: assets.csv
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
         
    def test_returns_list_of_assets(self):  
        """Description: the function reads the assets from the existing csv file. 
           In case of succes we expect to get the assets from the file: ['AAPL', 'IBM', 'MSFT']
        """
        actual_assets_list = get_assets_from_csv(self.test_file, self.field_list)
        expected_assests_list = ['AAPL', 'IBM', 'MSFT']
        self.assertEqual(actual_assets_list, expected_assests_list)
        
class Test_CSVFileNotExists(unittest.TestCase):
    def setUp(self):   
        pass
        
    def test_raise_error_if_file_not_exists(self):
        """Description: if we try to read the assets from nonexistent file, error is raised
        """
        field_list = ['Symbol', 'Company']
        self.assertRaises(FileNotFoundError, get_assets_from_csv, 'nonexistant_file', field_list)
  
    