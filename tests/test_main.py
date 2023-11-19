import unittest
from flask import Flask
from routes.main import main_bp


class MainBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        """Test Flask application, register the blueprint, set up templates folder and test client"""
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(main_bp)
        self.app.template_folder = '../templates'

        # Flaks test client for making requests
        self.client = self.app.test_client()

    def test_main_route(self):
        # Test that the main route returns a 200 status code
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_route_content(self):
        # Test the content of the main route response
        response = self.client.get('/')
        self.assertIn(b"<p>Test</p>", response.data)


if __name__ == '__main__':
    unittest.main()