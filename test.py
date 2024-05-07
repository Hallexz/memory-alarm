import unittest
from unittest.mock import patch, Mock
import alarm 

class TestMemoryUsage(unittest.TestCase):
    @patch('psutil.Process')
    @patch('psutil.virtual_memory')
    def test_memory_usage(self, mock_virtual_memory, mock_process):
        mock_process.return_value.memory_info.return_value.rss = 1024
        mock_virtual_memory.return_value.total = 2048
        self.assertEqual(alarm.memory_usage(), 50)

class TestSendAlert(unittest.TestCase):
    @patch('requests.post')
    def test_send_alert(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        self.assertEqual(alarm.send_alert(1024), 200)

class TestMain(unittest.TestCase):
    @patch('your_module.memory_usage')
    @patch('your_module.send_alert')
    def test_main(self, mock_send_alert, mock_memory_usage):
        mock_memory_usage.return_value = 95
        your_module.main()
        mock_send_alert.assert_called_once_with(95)

if __name__ == '__main__':
    unittest.main()
