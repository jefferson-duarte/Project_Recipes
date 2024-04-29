from django.test import TestCase
from django.urls import reverse


class RecipeURLSsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
