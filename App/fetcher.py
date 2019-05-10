#!/usr/bin/env python3
"""THis script will handle the calla to the API"""
from os import getenv
from datetime import datetime
import shutil

import requests

import models
from models.recipe import Recipe

storage = models.storage


class Fetcher:
    __api: str = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
    __status_code: int
    __json = None
    __text = None
    __last_query: datetime
    __error: str = None
    __cache_count : int = 0

    def __init__(self):
        pass

    def get_recipe(self, endpoint="random", **kwargs):
        """
        This method condenses the get request to the API back-end,
        it is default the random endpoint.

        :param endpoint: endpoint i.e. random, search, searchcomplex
        :param kwargs: parameters to search with, this is based on the API docs
        :return: a Response object
        """

        # TODO: tags will have to concatenated into a string delimited each
        #  tag by a comma
        options = {}
        if kwargs:
            [options.update({k: v}) for k, v in kwargs.items()]
        else:
            options = {"number": 100}

        header = {
            "X-RapidAPI-Host": getenv("X-RAPIDAPI-HOST"),
            "X-RapidAPI-Key": getenv("X-RAPIDAPI-KEY")
        }
        print(self.__api + endpoint)
        print(header)
        endpoint = endpoint + '?number=20'
        print(self.__api + endpoint)
        req = requests.get(self.__api + "recipes/" + endpoint, params=options,
                           headers=header)
        self.status_code = req.status_code
        if req.status_code not in range(400 - 512):
            try:
                self.json = req.json()
            except ValueError:
                self.text = req.text

            self.ok()
        else:
            self.err(req.text)

        return req

    def create_recipe(self, query=None):
        if query is None:
            query = self.json
        if query is not None:
            for r in query.get('recipes', None):
                self.__cache_count += 1
                img_url = r.get('image', None)
                try:
                    if img_url:
                        req = requests.get(img_url, stream=True, timeout=5)
                        if req.status_code == 200:
                            img_name = img_url.split('/')[-1]
                            with open('img/' + img_name, 'wb') as img:
                                req.raw.decode_content = True
                                shutil.copyfileobj(req.raw, img)
                except Exception as e:
                    print(e)
                    exit(-1)

                attrs = dict(
                    title=r.get('title'),
                    image_url= 'img/' + img_name,
                    source_url=r.get('sourceUrl'),
                    cook_in_min=r.get("cookingMinutes"),
                    prep_in_min=r.get("preparationMinutes"),
                    dish_type=r.get("dishTypes"),
                    ingredients=r.get("extendedIngredients"),
                    servings=r.get("servings"),
                    description=r.get("instructions"),
                    api_id=r.get("id"),
                    api_url=r.get("spoonacularSourceUrl")
                )

                recipe = Recipe(**attrs)
                recipe.save()

    def main(self):
        if self.__cache_count == 0:
            self.get_recipe()
            self.create_recipe()

    @property
    def status_code(self):
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, value: dict):
        self.__json = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value

    @property
    def last_query(self):
        return self.__last_query

    @property
    def error(self):
        time = self.last_query.strftime("%Y-%m-%dT%H:%M:%S")
        msg = self.__error
        error_msg = f"{time}: Error - {msg}"
        return error_msg

    @error.setter
    def error(self, value):
        self.set_time()
        self.__error = value

    def ok(self):
        self.set_time()

    def set_time(self):
        self.__last_query = datetime.utcnow()
