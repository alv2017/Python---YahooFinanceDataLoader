import unittest
from YahooFinanceDataLoader.asset_data.assetDataRequest import AssetDataRequest

class TestClass_AssetDataRequest_ActualDataDownloadRequest(unittest.TestCase):
    """Comment: this test suit contains tests for actual data downloads
    """
    def setUp(self):
        self.start_date = {
            "date":"2018-01-01",
            "ts": 1514764800
            }
        self.end_date = {
            "date":"2018-01-31",
            "ts": 1517356800
            }
    
    def test_valid_download_request_1(self):
        """Description: Sending a valid data download request"""
        aSymbol = "MSFT"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        interval = "1d"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_data_download()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["response_object"], 
                         "In case of successful download the response objec is not None")
        
    def test_valid_download_request_2(self):
        """Description: Sending a valid data download request"""
        aSymbol = "IBM"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        interval = "1wk"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_data_download()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["response_object"], 
                         "In case of successful download the response objec is not None")
        
    def test_valid_download_request_3(self):
        """Description: Sending a valid data download request"""
        aSymbol = "AAPL"
        sdate  = self.start_date["date"]
        edate = self.end_date["date"]
        interval = "1mo"
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_data_download()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["response_object"], 
                         "In case of successful download the response objec is not None")
            
    
    