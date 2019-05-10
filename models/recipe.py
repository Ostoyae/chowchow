#!/usr/bin/env python3
"""This File defines the Recipe model"""
from models.base_model import BaseModel


class Recipe(BaseModel):
    """Recipe class that declares the attribute involving a recipe"""
    title = ""  # api: title
    image_url = ""  # api: image
    source_url = ""  # api: sourceUrl
    cook_in_min = 0  # api: cookingMinutes
    prep_in_min = 0  # api: preparationMinutes
    dish_type = []  # api: dishTypes
    ingredients = []  # api: ingredients
    servings = 0  # api: servings
    description = ""  # api: description

    api_id = 0  # api: id
    api_url = ""  # api: spoonacularSourceUrl

    def like(self):
        self.save("favorites")
        self.delete()

    def dislike(self):
        self.delete()

    def delete_from_fav(self):
        self.delete('favorites')
