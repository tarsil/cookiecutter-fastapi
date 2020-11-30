from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest import TestCase
import unittest
from src.main import create_app


class TestApp(TestCase):

    def create_app(self):
        app = create_app('src.configs.testing.settings')
        return app

    def setUp(self):
        self.client = TestClient(self.create_app())

    def test_return_404(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
