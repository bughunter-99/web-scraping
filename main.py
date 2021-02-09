from bs4 import BeautifulSoup
import requests
import json
from recipe import Recipe
from datetime import datetime
all_recipes = []
categories = ['Appetizers and Snacks', 'Asian', 'BBQ and Grilling', 'Bread', 'Breakfast and Brunch', 'Cake', 'Chicken', 'Cookie',
              'Dessert', 'Dinner', 'Drinks', 'Healthy', 'Indian', 'Italian', 'Mexican', 'Pasta and Noodle', 'Sea Food', 'Salad', 'Vegetarian', 'Vegan']
start_time = datetime.now()
f = open('finalData.json', 'w')
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
    print(category, " : done")
    f.write(json.dumps(all_recipes, indent=2))
    all_recipes = []
f.close()

end_time = datetime.now()
print(end_time - start_time)
