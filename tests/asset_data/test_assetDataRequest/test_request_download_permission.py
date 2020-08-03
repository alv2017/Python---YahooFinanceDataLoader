import unittest
import requests
from unittest.mock import Mock, patch
from YahooFinanceDataLoader.asset_data.assetDataRequest import AssetDataRequest

class TestClass_AssetDataRequest_request_download_permission(unittest.TestCase):
    def setUp(self):   
        print("\n[Label: Unit. AssetDataRequest.request_download_permission]")         
        self.symbol = 'MSFT'
        self.sdate = '2018-01-01'
        self.edate = '2018-01-31'
        self.interval = '1d'
    
    @patch.object(requests, 'get', side_effect=requests.exceptions.ConnectionError)
    def test_return_on_connection_error(self, requests):
        """ Description: Response on ConnectionError
        """
        expected_resp = {
            "cookies": None,
            "crumb": None,
            "status_code": -1,
            "error": 1
            }

        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_download_permission()    
        # assertion 1  
        self.assertEqual(resp['error'], expected_resp['error'], 
            "Response error is expected to be {}.".format(expected_resp['error']))
        # assertion 2
        self.assertDictEqual(resp, expected_resp, 
            "The response is expected to be {}".format(expected_resp))
        
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_return_on_timeout_error(self, requests):
        """ Description: Response on Timeout error
        """
    
        expected_resp = {
            "cookies": None,
            "crumb": None,
            "status_code": -1,
            "error": 1
            }
        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_download_permission()     
        # assertion 1
        self.assertEqual(resp['error'], expected_resp['error'], 
            "Response error is expected to be {}.".format(expected_resp['error']))
        # assertion 2
        self.assertDictEqual(resp, expected_resp, 
            "The response is expected to be {}".format(expected_resp)) 
        
    @patch.object(requests, 'get')    
    def test_return_on_no_crumb_received(self, mock_requests_get):
        """ Description: Response when no crumb received (no download permission received)
        """
        empty_cookie_jar = requests.cookies.RequestsCookieJar()
        # expected response
        expected_resp = {
            "cookies": empty_cookie_jar,
            "crumb": None,
            "status_code": 200,
            "error": 2
            }
        
        # mocking a response from requests.get
        response = Mock()
        response.status_code = 200
        response.cookies = requests.cookies.RequestsCookieJar()
        response.content = bytes("There is no crumb!", "unicode-escape")
        mock_requests_get.return_value = response
        
        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_download_permission()     
        
        # assertion 1
        self.assertEqual(resp['error'], expected_resp['error'], 
            "Response error is expected to be {}.".format(expected_resp['error']))  
        # assertion 2
        self.assertIsNone(resp['crumb'], "Crumb should be equal to None")   
        # assertion 3
        self.assertDictEqual(resp, expected_resp, 
            "The response is expected to be {}".format(expected_resp)) 
        
    
