import unittest

from app.exam_app import api_app


class ExamAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = api_app.test_client()
        self.app.testing = True

    def test_when_x_is_17(self):
        response = self.app.get('/is_prime/17')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], True)

    def test_when_x_is_36(self):
        response = self.app.get('/is_prime/36')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], False)

    def test_when_x_is_13219(self):
        response = self.app.get('/is_prime/13219')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], True)


if __name__ == "__main__":
    unittest.main()
