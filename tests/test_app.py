import json
import unittest
import models
from os import environ
from datetime import datetime


from App.fetcher import Fetcher


class test_app(unittest.TestCase):

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

    def test_create_recipe(self):
        fetch = Fetcher()
        with open('test_data.json', 'r') as f:
            j = json.load(f)
            print(j)
            fetch.create_recipe(j)
            print(models.storage.all())
