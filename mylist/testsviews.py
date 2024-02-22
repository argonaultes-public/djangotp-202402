from django.test import TestCase, Client
from bs4 import BeautifulSoup

class ViewsTest(TestCase):
    fixtures = ['init']

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(b'Index of my list', response.content)

    def test_shoplist(self):
        # create ShopListItem and link to
        response = self.client.get('/shoplist/1')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(1, len(soup.find_all('li')))
