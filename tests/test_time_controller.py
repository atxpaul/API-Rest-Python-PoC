import unittest
from flask import Flask
from app.controllers.time_controller import time_bp


class TimeControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(time_bp)
        self.client = self.app.test_client()

    def test_get_time(self):
        response = self.client.get('/time')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('time_string', data)
        self.assertIsNotNone(data['time_string'])


if __name__ == '__main__':
    unittest.main()
