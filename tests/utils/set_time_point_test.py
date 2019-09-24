import unittest
import datetime
from YahooFinanceDataLoader.utils import set_time_point

class Test_SetTimePoint(unittest.TestCase):
    
    def setUp(self):
        # current date
        self.current_date = datetime.date.today()    
                    
        current_year = int(self.current_date.year)
        current_month = int(self.current_date.month)
        current_day = int(self.current_date.day)
        strYear = str(current_year).zfill(2)
        strMonth = str(current_month).zfill(2)
        strDay = str(current_day).zfill(2)    
        
        # current date string 
        self.current_date_string = "-".join([strYear, strMonth, strDay])
        # current date timestamp
        self.current_timestamp = datetime.datetime(current_year, 
                                           current_month, 
                                           current_day).timestamp()
        
        # date that is greater than current
        self.greater_than_current_date = self.current_date + datetime.timedelta(days=1)
        gtcd_year = str( self.greater_than_current_date.year ).zfill(2)
        gtcd_month = str( self.greater_than_current_date.month ).zfill(2) 
        gtcd_day = str( self.greater_than_current_date.day ).zfill(2) 
        self.greater_than_current_date_string = "-".join([gtcd_year, gtcd_month, gtcd_day])
        
    def test_return_timestamp_correct_date_1(self):
        test_date = '2017-05-12'
        test_timestamp =  1494543600
        self.assertEqual(test_timestamp, set_time_point(test_date))
        
    def test_return_timestamp_correct_date_2(self):
        test_date = '2018-02-01'
        test_timestamp =  1517443200
        self.assertEqual(test_timestamp, set_time_point(test_date))
      
    def test_raise_timestamp_incorrect_currentdate(self):
        test_date = self.current_date_string
        
        self.assertRaises(ValueError, set_time_point, test_date)

    def test_raise_error_incorrect_date_before_min(self):
        test_date = '1999-04-25'
        self.assertRaises(ValueError, set_time_point, test_date)
        
    def test_raise_error_incorrect_date_nonexistent_1(self):
        test_date = '2010-02-31'
        self.assertRaises(ValueError, set_time_point, test_date)
        
    def test_raise_error_incorrect_date_nonexistent_2(self):
        test_date = '2015-15-03'
        self.assertRaises(ValueError, set_time_point, test_date)
        
    def test_raise_error_incorrect_date_greater_than_current(self):
        test_date = self.greater_than_current_date_string
        self.assertRaises(ValueError, set_time_point, test_date)
          
if __name__ == '__main__':
    unittest.main()

        
        
        