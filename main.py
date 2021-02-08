from bs4 import BeautifulSoup
import requests
import json
from recipe import Recipe
from datetime import datetime
all_recipes = []
categories = ['indian']  # , 'chicken', 'paneer', 'mushroom',
# 'baby corn', 'dinner', 'breakfast', 'lunch', 'snacks', 'bread', 'rice', 'cake', 'chinese', 'sea food', 'fish', 'vegitarian']
start_time = datetime.now()
f = open('data4.json', 'w')
f.write('[')
for category in categories:
    page = 1
    while True:
        url = 'https://www.allrecipes.com/search/results/?wt={}&page={}'.format(
            category, page)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        recipes = soup.find_all('article', class_='fixed-recipe-card')
        before_count = len(all_recipes)
        for recipe in recipes:
            new_recipe = Recipe(recipe, category)
            all_recipes.append(new_recipe.__dict__)
        after_count = len(all_recipes)

        if after_count - before_count == 0:
            break
        else:
            page += 1
        if page > 1:
            break
    print(category, " : done")
    f.write(json.dumps(all_recipes, indent=2))
    all_recipes = []
    f.write(',')

f.write('{"status" : "OK"}]')
f.close()

end_time = datetime.now()
print(end_time - start_time)
