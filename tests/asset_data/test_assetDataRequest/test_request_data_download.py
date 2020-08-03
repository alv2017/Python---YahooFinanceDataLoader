import unittest
import requests
from unittest.mock import Mock, patch

from YahooFinanceDataLoader.asset_data.assetDataRequest import AssetDataRequest

class TestClass_AssetDataRequest_request_data_download(unittest.TestCase):
    def setUp(self):         
        self.symbol = 'MSFT'
        self.sdate = '2018-01-01'
        self.edate = '2018-01-31'
        self.interval = '1d'
        
    @patch.object(AssetDataRequest, 'request_download_permission')
    def test_return_value_on_download_permission_error_1(self, request_download_permission):
        """Description: Response error on request_download_permission response['error']=1
        """
        # mocking a response from request_download_permission
        permission_response = {
            "error": 1
        }
        request_download_permission.return_value = permission_response
                
        expected_response_error = -permission_response['error']
            
        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_data_download()  
        
        # assertion 
        self.assertEqual(resp["error"], expected_response_error, 
            "The response error should be equal to {0}".format(expected_response_error)) 
        
    @patch.object(AssetDataRequest, 'request_download_permission')
    def test_return_value_on_download_permission_error_2(self, 
        request_download_permission):
        """Description: Response error when request_download_permission response['error']=2
        """
        # mocking a response from requests_download_permission
        permission_response = {
            "error": 2
        }
        request_download_permission.return_value = permission_response
                
        expected_response_error = -permission_response['error']

        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_data_download()  
        
        # assertion
        self.assertEqual(resp["error"], expected_response_error, 
            "The response error should be equal to {0}".format(expected_response_error)) 
        
    @patch.object(AssetDataRequest, 'request_download_permission')    
    @patch.object(requests, 'get', side_effect=requests.exceptions.ConnectionError)
    def test_return_value_on_connection_error(self, requests_get, request_download_permission):
        """ Description: Response error on ConnectionError
        """
        expected_response_error = 1
        # mocking a response from requests_download_permission
        permission_response = {   
            "cookies": "cookies_placeholder",
            "crumb": "crumb_placeholder",
            "status_code": 200,
            "error": 0
            }
        request_download_permission.return_value = permission_response

        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_data_download()      
        # assertion   
        self.assertEqual(resp["error"], expected_response_error, 
            "The response error should be equal to {0}".format(expected_response_error))
        
    @patch.object(AssetDataRequest, 'request_download_permission')    
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_return_value_on_timeout_error(self, requests_get, request_download_permission):
        """Description: Response error on Timeout
        """
        expected_response_error = 1        
        # mocking a response from requests_download_permission
        permission_response = {   
            "cookies": "cookies_placeholder",
            "crumb": "crumb_placeholder",
            "status_code": 200,
            "error": 0
            }
        request_download_permission.return_value = permission_response

        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_data_download()      
        # assertion   
        self.assertEqual(resp["error"], expected_response_error, 
            "The response error should be equal to {0}".format(expected_response_error))  
        
    @patch.object(AssetDataRequest, 'request_download_permission')    
    @patch.object(requests, 'get')
    def test_return_value_on_http_error(self, mock_requests_get, request_download_permission):
        """Description: Response error on HTTPError, i.e. response status code is not equal to 200
        """
        status_code = 404        
        expected_response_error = 2        
        # mocking response from requests_download_permission
        permission_response = {   
            "cookies": "cookies_placeholder",
            "crumb": "crumb_placeholder",
            "status_code": 200,
            "error": 0
        }
        request_download_permission.return_value = permission_response
        
        # mocking response from requests
        response = Mock()
        response.status_code = status_code
        response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_requests_get.return_value = response

        # action
        asset_data_request = AssetDataRequest(self.symbol, self.sdate, 
                                              self.edate, self.interval)        
        resp = asset_data_request.request_data_download()      

        # assertion   
        self.assertEqual(resp["error"], expected_response_error, 
            "The response error should be equal to {0}".format(expected_response_error))  
        
        
        