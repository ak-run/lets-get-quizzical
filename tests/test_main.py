import unittest
from flask import Flask
from routes.main import main_bp


class TestMainBlueprint(unittest.TestCase):

    def setUp(self):
        """Test Flask application, register the blueprint, set up templates folder and test client"""
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(main_bp, url_prefix="/")
        self.app.template_folder = '../templates'
        # Flaks test client for making requests
        self.client = self.app.test_client()

    def test_valid_main_route(self):
        # Test that the main route returns a 200 status code
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_valid_main_route_content(self):
        # Test the key elements of the content of the main route response
        response = self.client.get('/')
        self.assertIn(b"<!DOCTYPE html>", response.data)
        self.assertIn(b"<h3>Pub quiz</h3>", response.data)

    def test_valid_how_to_play_route(self):
        # Test that how to play route returns a 200 status code
        response = self.client.get('/how_to_play')
        self.assertEqual(response.status_code, 200)

    def test_valid_how_to_play_route_content(self):
        # Test the key elements of the content of the how to play route response
        self.assertIn(b"<!DOCTYPE html>", response.data)
        self.assertIn(b"<h2>How to Play></h2>", response.data)

    def test_valid_leaderboard_route(self):
        # Test that Leaderboard route returns a 200 status code
        response = self.client.get('/leaderboard_main')
        self.assertEqual(response.status_code, 200)

    def test_valid_leaderboard_route_content(self):
        # Test the key elements of the content of the leaderboard route response
        self.assertIn(b"<!DOCTYPE html>", response.data)
        self.assertIn(b"<h3>Leaderboard</h3>", response.data)

    def test_valid_setup_route(self):
        # Test that setup route returns a 200 status code
        response = self.client.get('/setup')
        self.assertEqual(response.status_code, 200)

    def test_valid_setup_route_content(self):
        # Test the key elements of the content of the setup route response
        self.assertIn(b"<!DOCTYPE html>", response.data)
        self.assertIn(b"<h3>Select category</h3>", response.data)

        



if __name__ == '__main__':
    unittest.main()
