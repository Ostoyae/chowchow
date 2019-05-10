import json
import unittest
import models
from models.recipe import Recipe
from os import environ
from datetime import datetime


from App.fetcher import Fetcher


class test_app_backend(unittest.TestCase):

    def test_dotenv_rapidAPI_host(self):
        self.assertIsNotNone(environ.get("X-RAPIDAPI-HOST", None))

    def test_dotenv_rapidAPI_key(self):
        self.assertIsNotNone(environ.get("X-RAPIDAPI-KEY", None))

    @unittest.skip("Saving requests")
    def test_fetcher_get_recipe(self):
        fetch = Fetcher()
        fetch.get_recipe(**{'number': 20, 'tags': "vegetarian,dessert"})
        self.assertEqual(fetch.status_code, 200)
        self.assertEqual(type(fetch.data), dict)
        with open('test_data.json', 'w+') as j:
            json.dump(fetch.json, j)

    @unittest.skip("not test this now")
    def test_create_recipe_cache(self):
        fetch = Fetcher()
        with open('test_data_0.json', 'r') as f:
            j = json.load(f)
            print(j)
            fetch.create_recipe(j)
            models.storage.reload("objects")
            print(models.storage.all())

    @unittest.skip("not test this now")
    def test_create_recipe_fav(self):
        fetch = Fetcher()
        with open('test_data_0.json', 'r') as f:
            j = json.load(f)
            print(j)
            fetch.create_recipe(j)
            models.storage.save("favorites")
            models.storage.reload("favorites")

    def test_like_recipe(self):
        new_r = dict(
            id="abcd",
            title="a new recipe"
        )
        r = Recipe(**new_r)
        r.save()
        r.like()
        self.assertIsNotNone(models.storage.get("Recipe", "abcd", "fav"))
    def test_Dislike_recipe(self):
        new_r = dict(
            id="xyz",
            title="I don't like you!"
        )
        r = Recipe(**new_r)
        r.save()
        r.dislike()
        self.assertIsNone(models.storage.get("Recipe", "xzy"))
        self.assertIsNone(models.storage.get("Recipe", "xzy", "fav"))

    def test_delete_from_like_recipe(self):
        new_r = dict(
            id="acbeasyas123",
            title="a new recipe"
        )
        r = Recipe(**new_r)
        r.save()
        r.like()
        self.assertIsNotNone(models.storage.get("Recipe", "acbeasyas123", "fav"))
        r.delete_from_fav()
        self.assertIsNone(models.storage.get("Recipe", "acbeasyas123", "fav"))

