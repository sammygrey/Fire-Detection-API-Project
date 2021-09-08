import unittest

from fastapi.testclient import TestClient
import tensorflow as tf

from app.main import app

client = TestClient(app)


class ClassifierAPITest(unittest.TestCase):

    TEST_COLOR_IMG_URL = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"

    def test_make_prediction_normal(self):
        """Client submits a RGB image and gets a valid response."""
        pass
