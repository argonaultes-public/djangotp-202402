from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from parameterized import parameterized

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["init.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        cls.selenium = WebDriver(options = options)
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

# test index

    def test_index(self):
        self.selenium.get(f'{self.live_server_url}/')
        response = self.selenium.find_element(By.XPATH, '/html/body')
        self.assertEqual('Index of my list', response.text)


    def test_shopping_list_direct(self):
        self.selenium.get(f'{self.live_server_url}/shoplist/1')
        shoplistitems = self.selenium.find_elements(By.TAG_NAME, 'li')
        self.assertEqual(1, len(shoplistitems))

    # list with id : 1, 1 item
    # list with id : 2, 0 item
    @parameterized.expand([
        (0, 1),
        (1, 0)
    ])
    def test_click_on_first_list(self, list_position, nb_items):
        self.selenium.get(f'{self.live_server_url}/shoplist')
        links = self.selenium.find_elements(By.TAG_NAME, 'a')
        links[list_position].click()
        shoplistitems = self.selenium.find_elements(By.TAG_NAME, 'li')
        self.assertEqual(nb_items, len(shoplistitems))



# test click on hyperlink list to check items in list

# record test with IDE