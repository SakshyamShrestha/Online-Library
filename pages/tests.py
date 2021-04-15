from django.test import TestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
