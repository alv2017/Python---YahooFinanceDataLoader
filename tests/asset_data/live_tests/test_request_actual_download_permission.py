import unittest
from YahooFinanceDataLoader.asset_data.assetDataRequest import AssetDataRequest

class TestClass_AssetDataRequest_ActualDownloadPermissionRequest(unittest.TestCase):
    """AssetDataRequest, actual request_download_permission
    """
    def setUp(self):
        print("\n[Label: Live. AssetDataRequest, actual request_download_permission]")
        self.start_date = "2018-01-01"
        self.end_date = "2018-01-31"
        self.interval = "1d"
    
    def test_request_download_permission_1(self):
        """Description: We will send a request for preliminary data
           needed to form a data download request
        """
        aSymbol = "MSFT"
        sdate = self.start_date
        edate = self.end_date
        interval = self.interval
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_download_permission()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["cookies"], 
                         "In case of successful download the cookies object is not None")
        self.assertIsNotNone(response_data["crumb"], 
                         "In case of successful download the crumb object is not None")       
        
    def test_request_download_permission_2(self):
        """Description: We will send a request for preliminary data
           needed to form a data download request
        """
        aSymbol = "IBM"
        sdate = self.start_date
        edate = self.end_date
        interval = self.interval
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_download_permission()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["cookies"], 
                         "In case of successful download the cookies object is not None")
        self.assertIsNotNone(response_data["crumb"], 
                         "In case of successful download the crumb object is not None") 
        
    def test_request_download_permission_3(self):
        """Description: We will send a request for preliminary data
           needed to form a data download request
        """
        aSymbol = "AAPL"
        sdate = self.start_date
        edate = self.end_date
        interval = self.interval
        
        ADR = AssetDataRequest(aSymbol, sdate, edate, interval)    
        response_data = ADR.request_download_permission()
        
        self.assertEqual(response_data["error"], 0, 
                         "In case of successful data download error should be equal to 0")
        self.assertEqual(response_data["status_code"], 200, 
                         "In case of successful data download status code should be equal to 200")
        self.assertIsNotNone(response_data["cookies"], 
                         "In case of successful download the cookies object is not None")
        self.assertIsNotNone(response_data["crumb"], 
                         "In case of successful download the crumb object is not None") 
        
        