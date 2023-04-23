import unittest
from app import app, date


class TestClient(unittest.TestCase):

    def test_avg_rate_status(self):
        with app.test_client() as client:

            response = client.get('/avg_rate')
            self.assertEqual(response.status_code, 200)

    def test_avg_rate(self):
        with app.test_client() as client:

            response = client.get('/avg_rate')
            self.assertEqual(response.json['date'], date)
            self.assertIsNotNone(response.json['avg'])

    def test_min_max(self):
        with app.test_client() as client:

            response = client.get('/min_max')
            self.assertIsNotNone(response.json['max_avg_value'])
            self.assertIsNotNone(response.json['max_avg_date'])
            self.assertIsNotNone(response.json['min_avg_value'])
            self.assertIsNotNone(response.json['min_avg_date'])


if __name__ == '__main__':
    unittest.main()