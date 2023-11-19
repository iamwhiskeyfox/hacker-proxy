import unittest
from proxy_server import app


class ProxyServerTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_proxy_response_status(self):
        response = self.app.get('/item?id=13713480')
        self.assertEqual(response.status_code, 200)

    def test_proxy_content_modification(self):
        response = self.app.get('/item?id=13713480')
        self.assertEqual(response.status_code, 200)
        self.assertIn("The visual™ description", response.get_data(as_text=True))

    def test_proxy_error_handling(self):
        response = self.app.get('/item?id=nonexistent_id')
        self.assertEqual(response.status_code, 200)
        self.assertIn("No such item.", response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
