from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        # Edyta dowiedziala sie o nowej, wspanialej  aplikacji w postaci listy rzeczy do zrobienia
        # Postawnowila wiec przejsc dna strone glowna tej aplikacji

        self.assertIn('Listy', self.browser.title)
        self.fail('Zakonczenie testu')


if __name__ == '__main__':
    unittest.main(warnings='ignore')





