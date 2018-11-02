from service import Service
from mock import patch
from unittest.mock import mock_open
from unittest import mock
import unittest

class TestService(unittest.TestCase):

    def setUp(self):
        self.service = Service()
    
    @patch('service.Service.bad_random', return_value=9)
    def test_bad_random(self, bad_random):
        self.assertEqual(bad_random(), 9)
        
    def test_divide(self):
        self.service.bad_random = mock.Mock(return_value = 4)
        return_val = self.service.divide(2)
        assert return_val == 2

        self.service.bad_random = mock.Mock(return_value = 5)
        return_val = self.service.divide(2)
        assert return_val == 2.5


    def test_abs_plus(self):
        assert self.service.abs_plus(-1) == 2
        assert self.service.abs_plus(0) == 1
        assert self.service.abs_plus(1) == 2

    def test_complicated_function(self):
        self.service.divide = mock.Mock(return_value = 15)   
        self.service.bad_random = mock.Mock(return_value = 6)
        assert self.service.complicated_function(5) == (15, 0)

if __name__ == '__main__':
    unittest.main()
