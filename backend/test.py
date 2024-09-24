import requests
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")


def get_recipes(ingredients):
    url = f"https://api.edamam.com/search?q={
        ingredients}&app_id=b34f1964&app_key=f4009c6d60357ea09afa290064b25842"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['hits']  # This contains the list of recipes
    else:
        return None


# Example usage
ingredients = "tomato,chicken"
recipes = get_recipes(ingredients)
print(recipes)

# for recipe in recipes:
#     print(recipe['recipe']['label'])  # Prints the name of the recipe
