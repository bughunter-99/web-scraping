from random import randint, choice
from detailed_recipe import *


class Recipe:
    def __init__(self, recipe, category):
        self.recipe = recipe
        self.category = category
        self.setAlldata()

    def setUid(self, length=10):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        numbers = list('0123456789')
        randomlist = alphabet + numbers
        uuid = ''
        for i in range(length):
            uuid += str(choice(randomlist))

        self.u_id = uuid

    def getUID(self):
        return self.u_id

    def setTitle(self):
        self.title = self.recipe.find(
            'span', class_="fixed-recipe-card__title-link").text

    def getTitle(self):
        return self.title

    def setDescription(self):
        self.description = self.recipe.find(
            'div', class_="fixed-recipe-card__description").text

    def getDescription(self):
        return self.description

    def setImageUrl(self):
        self.image_url = self.recipe.find(
            'img', class_="fixed-recipe-card__img").get('data-original-src')

    def getImageUrl(self):
        return self.image_url

    def setRecipeUrl(self):
        self.recipe_url = self.recipe.find(
            'a', class_="fixed-recipe-card__title-link").get('href')
        self.moreInfo = DetailedRecipe(self.recipe_url).getData()

    def getRecipeUrl(self):
        return self.recipe_url

    def setAlldata(self):
        try:
            self.setUid()
            self.setTitle()
            self.setDescription()
            self.setImageUrl()
            self.setRecipeUrl()
            del self.recipe

        except AttributeError as err:
            print("error:", err)
