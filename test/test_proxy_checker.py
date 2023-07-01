import unittest
from unittest.mock import patch, Mock
from src.proxy_checker import ProxyChecker

class TestProxyChecker(unittest.TestCase):
    def setUp(self):
        self.proxies = ["proxy1", "proxy2", "proxy3"]
        self.checker = ProxyChecker(self.proxies)

    @patch('src.proxy_checker.requests.get')
    def test_check_proxy(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        for proxy in self.proxies:
            result = self.checker.check_proxy(proxy)
            self.assertEqual(result, proxy)
            mock_get.assert_called_with("http://google.com", proxies={"http": proxy, 'https':proxy}, timeout=5)
    
    @patch('src.proxy_checker.requests.get')
    def test_filter_proxies(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        valid_proxies = self.checker.filter_proxies()
        self.assertEqual(valid_proxies, self.proxies)

if __name__ == '__main__':
    unittest.main()
    