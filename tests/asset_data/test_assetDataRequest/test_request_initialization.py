import unittest
from YahooFinanceDataLoader.asset_data.assetDataRequest import AssetDataRequest

class TestClass_AssetDataRequest_Initialization(unittest.TestCase):
    def setUp(self):
        self.start_date = {
            "date":"2018-01-01",
            "ts": 1514764800
            }
        self.end_date = {
            "date":"2018-01-31",
            "ts": 1517356800
            }
           
    def test_initialize_with_correct_parameters_1(self):
        """ Description: initialization of AssetDataRequest object when parameters are correct
        """
        aSymbol = "MSFT"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        sdate_timestamp = self.start_date["ts"]
        edate_timestamp = self.end_date["ts"]
        interval = "1d"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)
        self.assertEqual(ADR.symbol, aSymbol, "Expected symbol is {0}".format(aSymbol))
        self.assertEqual(ADR.interval, interval, "Expected interval is {0}".format(interval))
        self.assertEqual(ADR.start_date, sdate_timestamp, 
                         "Start date is expected to be equal {0}".format(sdate_timestamp))
        self.assertEqual(ADR.end_date, edate_timestamp, 
                         "End date is expected to be equal {0}".format(edate_timestamp))
        
    def test_initialize_with_correct_parameters_2(self):
        """ Description: initialization of AssetDataRequest object when parameters are correct
        """
        aSymbol = "IBM"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        sdate_timestamp = self.start_date["ts"]
        edate_timestamp = self.end_date["ts"]
        interval = "1wk"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)
        self.assertEqual(ADR.symbol, aSymbol, "Expected symbol is {0}".format(aSymbol))
        self.assertEqual(ADR.interval, interval, "Expected interval is {0}".format(interval))
        self.assertEqual(ADR.start_date, sdate_timestamp, 
                         "Start date is expected to be equal {0}".format(sdate_timestamp))
        self.assertEqual(ADR.end_date, edate_timestamp, 
                         "End date is expected to be equal {0}".format(edate_timestamp))
        
    def test_initialize_with_correct_parameters_3(self):
        """ Description: initialization of AssetDataRequest object when parameters are correct
        """
        aSymbol = "AAPL"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        sdate_timestamp = self.start_date["ts"]
        edate_timestamp = self.end_date["ts"]
        interval = "1mo"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)
        self.assertEqual(ADR.symbol, aSymbol, "Expected symbol is {0}".format(aSymbol))
        self.assertEqual(ADR.interval, interval, "Expected interval is {0}".format(interval))
        self.assertEqual(ADR.start_date, sdate_timestamp, 
                         "Start date is expected to be equal {0}".format(sdate_timestamp))
        self.assertEqual(ADR.end_date, edate_timestamp, 
                         "End date is expected to be equal {0}".format(edate_timestamp)) 

               
    def test_initialize_with_invalid_dates(self):
        """Description: ValueError is raised when start date is greater or equal to the end date
        """
        aSymbol = "MSFT"
        sdate  = self.end_date['date']
        edate = self.start_date['date']
        interval = "1d"
        self.assertRaises(ValueError, AssetDataRequest, aSymbol, sdate, edate, interval)
        
        
    def test_initialize_with_invalid_interval(self):
        """Description: Value error is raised if interval is not in ['1d', '1wk', '1mo']
        """
        aSymbol = "MSFT"
        sdate  = self.end_date['date']
        edate = self.start_date['date']
        interval = "1y"
        self.assertRaises(ValueError, AssetDataRequest, aSymbol, sdate, edate, interval)       
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        