import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        # Set up a test client before each test runs
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page_status_code(self):
        # Simulates a user visiting the root URL
        response = self.client.get('/')
        # Asserts that the server responds with a 200 OK status
        self.assertEqual(response.status_code, 200)

    def test_home_page_title(self):
        # Asserts that the specific title tag exists in the HTML response
        response = self.client.get('/')
        self.assertIn(b'<title>Jenkins CI/CD Pipeline Demo</title>', response.data)

if __name__ == '__main__':
    unittest.main()