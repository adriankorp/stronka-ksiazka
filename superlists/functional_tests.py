from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        #Zwrocila uwage ze tytul strony i naglowek zawiera slowo listy
        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Listy', header_text)

        #Od razu zostaje zachecona aby wpisac rzeczy do zrobeina
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Wpisz rzeczy do zrobienia'
        )

        # W polu tekstowym wpisala "Kupic pawie piora"

        input_box.send_keys('Kupic pawie piora')

        # Po nacisnieciu klawisza Enter strona zostanie uaktualniona i wyswietla
        #1. Kupic pawie piora

        input_box.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Kupic pawie piora' for row in rows)
        )

        #Na stronie nadal znajduje sie pole tekstowe zachecajace do podania kolejnego zadania
        self.fail('Zakonczenie testu')


if __name__ == '__main__':
    unittest.main(warnings='ignore')





