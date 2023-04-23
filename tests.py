import unittest
from unittest.mock import patch
from app import app
import requests

class TestCurrencyApi(unittest.TestCase):

    def test_major_diff():
        currency = 'USD'
        quotations = 30
        response = requests.get(f'http://localhost:80/major_difference?currency={currency}&quotations={quotations}')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data['major_difference'], float)
if __name__ == '__main__':
    unittest.main()
