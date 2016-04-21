from django.test import TestCase
from django.test import Client

class AnimalTestCase(TestCase):
    def test_polls_page_appears(self):
        client = Client()
        r = client.get('/polls/')
        
        self.assertEqual(200,r.status_code)

