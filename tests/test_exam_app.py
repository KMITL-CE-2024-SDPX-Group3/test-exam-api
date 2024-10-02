import unittest

from app.exam_app import api_app


class ExamAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = api_app.test_client()
        self.app.testing = True

    def test_x_is_3dot7(self):
        response = self.app.get('/is2honor/3.7')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], False)

    def test_x_is_3dot4(self):
        response = self.app.get('/is2honor/3.4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], True)

    def test_x_is_3dot1(self):
        response = self.app.get('/is2honor/3.1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], False)


if __name__ == "__main__":
    unittest.main()
