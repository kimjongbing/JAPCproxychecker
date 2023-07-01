import unittest
from unittest.mock import patch
from src.file_handler import read_proxies_from_file, write_proxies_to_file

class TestFileHandler(unittest.TestCase):
    @patch('builtins.open')
    def test_read_proxies_from_file(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.__enter__.return_value.readlines.return_value = ['proxy1\n', 'proxy2\n']
        proxies = read_proxies_from_file('test_file.txt')
        self.assertEqual(proxies, ['proxy1', 'proxy2'])
        mock_open.assert_called_once_with('test_file.txt', 'r')

    @patch('builtins.open')
    def test_write_proxies_to_file(self, mock_open):
        mock_file = mock_open.return_value
        write_proxies_to_file('test_file.txt', ['proxy1', 'proxy2'])
        mock_open.assert_called_once_with('test_file.txt', 'w')
        mock_file.__enter__.return_value.write.assert_any_call('proxy1\n')
        mock_file.__enter__.return_value.write.assert_any_call('proxy2\n')

if __name__ == '__main__':
    unittest.main()
