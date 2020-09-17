from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_home_page_can_save_POST_request(self):
        response = self.client.post('/', data={'new_item_text': "Nowy element listy"})

        self.assertIn('Nowy element listy', response.content.decode(),"Elementu nie ma w liscie")
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.p
