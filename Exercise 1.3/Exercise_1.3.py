recipes_list = []
ingredients_list = []

def take_recipe():
  name = str(input("Enter recipe name: "))
  cooking_time = int(input("Enter cook time (in minutes): "))
  ingredients = list(input("Enter the ingredients, separated by a comma: ").split(", "))

  recipe = {
    'Name': name, 
    'Cooking Time (min)': cooking_time, 
    'Ingredients': ingredients
    }
  
  return recipe


n = int(input("How many recipes would you like to add? "))

for i in range(n):
  recipe = take_recipe()

  for ingredient in recipe['Ingredients']:
    if not ingredient in ingredients_list:
      ingredients_list.append(ingredient.capitalize())

  recipes_list.append(recipe)

for recipe in recipes_list:

  if recipe['Cooking Time (min)'] < 10 and len(recipe['Ingredients']) < 4:
    recipe['Difficulty'] = 'Easy'

  elif recipe['Cooking Time (min)'] < 10 and len(recipe['Ingredients']) >= 4:
    recipe['Difficulty'] = 'Medium'
  
  elif recipe['Cooking Time (min)'] >= 10 and len(recipe['Ingredients']) < 4:
    recipe['Difficulty'] = 'Intermediate'
  
  elif recipe['Cooking Time (min)'] >= 10 and len(recipe['Ingredients']) >= 4:
    recipe['Difficulty'] = 'Hard'

  print('----------------------------------------')
  print('')
  print('Recipe: ', recipe['Name'])
  print('Cooking Time (min): ', recipe['Cooking Time (min)'])
  print('Ingredients: ')
  for ingredient in recipe['Ingredients']:
    print(ingredient)
  print('Difficulty: ', recipe['Difficulty'])
  print('')

def show_ingredients():
  print('Ingredients Available Across All Recipes')
  print('----------------------------------------')
  ingredients_list.sort()
  for ingredient in ingredients_list:
    print(ingredient)

show_ingredients()