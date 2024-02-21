from django.test import TestCase, Client
from bs4 import BeautifulSoup

class ViewsTest(TestCase):
    fixtures = ['init']

    def setUp(self):
        self.client = Client()

    def test_shoplist(self):
        response = self.client.get('/shoplist/1')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(1, len(soup.find_all('li')))

# test index
# a la tentative d acces de la racine du site s'assurer que toutes les listes d'achats sont affichees
# premier assert sur le code reponse 200
# second assert sur le contenu de la reponse


# test shopping_list_details_v2
# pour un id de liste donnee, s assurer que les elements affiches sont bien ceux rattaches a la liste

