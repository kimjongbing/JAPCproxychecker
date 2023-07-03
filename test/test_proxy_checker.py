import unittest
from unittest.mock import patch, Mock
from src.proxy_checker import ProxyChecker


class TestProxyChecker(unittest.TestCase):
    def setUp(self):
        self.proxies = ["proxy1", "proxy2", "proxy3"]
        self.checker = ProxyChecker(self.proxies)

    @patch("src.proxy_checker.requests.get")
    def test_check_proxy(self, mock_get):
        mock_response_200 = Mock()
        mock_response_200.status_code = 200
        mock_response_404 = Mock()
        mock_response_404.status_code = 404
        mock_response_500 = Mock()
        mock_response_500.status_code = 500
        mock_get.side_effect = [mock_response_200, mock_response_404, mock_response_500]

        expected_results = {200: "proxy1", 404: "proxy2", 500: "proxy3"}
        for status_code, proxy in expected_results.items():
            result = self.checker.check_proxy(proxy)
            if status_code == 200:
                self.assertEqual(result, proxy)
            else:
                self.assertIsNone(result)
            mock_get.assert_called_with(
                "http://google.com", proxies={"http": proxy, "https": proxy}, timeout=5
            )

    @patch("src.proxy_checker.requests.get")
    def test_filter_proxies(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        valid_proxies = self.checker.filter_proxies()
        self.assertEqual(valid_proxies, self.proxies)


if __name__ == "__main__":
    unittest.main()
