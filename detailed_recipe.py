import json
import requests
from bs4 import BeautifulSoup


class DetailedRecipe:
    def __init__(self, recipe_url):
        self.recpie_url = recipe_url
        self.setAllData()

    def setAllData(self):
        html_text = requests.get(self.recpie_url).text
        soup = BeautifulSoup(html_text, 'lxml')
        steps_body = soup.findAll("div", class_="paragraph")
        ingredients = soup.findAll('li', class_='ingredients-item')
        recipe_head = soup.findAll(
            "div", class_="recipe-meta-item-header")
        recipe_body = soup.findAll(
            "div", class_="recipe-meta-item-body")
        recipe_image = soup.find("div", class_="lazy-image").get("data-src")

        recipe_info_dict = {}
        recipe_info_dict["recipe_info"] = {i[:-1]: "{}{}".format(i, j) for i, j in dict(zip([x.text.strip() for x in recipe_head],
                                                                                            [x.text.strip() for x in recipe_body])).items()}
        recipe_info_dict["recipe_ingredients"] = dict(zip([
            "ingredient-item-{}".format(x) for x in range(0, len(ingredients))], [x.text.strip() for x in ingredients]))
        recipe_info_dict["recipe_steps"] = dict(zip(["step-{}".format(x) for x in range(0, len(steps_body))],
                                                    [x.text.strip() for x in steps_body]))
        self.moreInfo = recipe_info_dict
        del self.recpie_url

    def getData(self):
        return self.moreInfo
