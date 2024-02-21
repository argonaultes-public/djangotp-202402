from django.test import TestCase
from .models import ShopList, ShopListItem
from django.db.utils import DataError
from parameterized import parameterized

# Create your tests here.


# tests Models ShoppingList

class ShoppingListTest(TestCase):
    fixtures = ['init']

    def test_init_fixture(self):
        actual = ShopList.objects.all()
        self.assertEqual(2, len(actual))

# essayer de creer un shoppinglist avec un nom court, vérifier que l'élément a bien été créé en base

    def test_with_valid_name(self):
        expected_name = 'valid'
        actual = ShopList.objects.create(name = expected_name)
        from_db = ShopList.objects.get(name = actual.name)
        self.assertEqual(expected_name, from_db.name)


# essayer de creer un shoppinglist avec un nom trop long, vérifier que l élément n a pas été créé en base

    def test_with_too_long_name(self):
        invalid_name = 'invalid' * 30
        with self.assertRaises(DataError):
            ShopList.objects.create(name = invalid_name)

# TDD
# tester la fonctionnalite du compte du nombre d'items presents dans une liste
# test 0 item in ShopList instance

    def test_0_item(self):
        actual = ShopList.objects.create(name = 'list with 0 item')
        self.assertEqual(0, actual.nb_items)

# test n items in ShopList instance
    @parameterized.expand([
        (0,),
        (2,),
        (130,),
        (4,),
    ])
    def test_n_items_in_shoplist(self, nb_items):
        actual = ShopList.objects.create(name = f'list with {nb_items} items')
        for idx in range(nb_items):
            ShopListItem.objects.create(name = f'item{idx}', quantity = 0, shop_list = actual)
        self.assertEqual(nb_items, actual.nb_items)

    # def test_n_items_0(self):
    #     self.test_n_items(0)

    # def test_n_items_1(self):
    #     self.test_n_items(2)

    # def test_n_items_2(self):
    #     self.test_n_items(130)


    def test_n_subtest(self):
        for nb_items, expected_nb_items in [(0,0), (2,2), (130,130),(4,4),]:
            with self.subTest(i=nb_items):
                actual = ShopList.objects.create(name = f'list with {nb_items} items')
                for idx in range(nb_items):
                    ShopListItem.objects.create(name = f'item{idx}', quantity = 0, shop_list = actual)
                self.assertEqual(expected_nb_items, actual.nb_items)
                