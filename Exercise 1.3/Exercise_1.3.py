# Initialized empty lists that will hold the recipes
# and the ingredients from each recipe

recipes_list = []
ingredients_list = []

# The function that is called in response to how many recipes the user wants to create
# Gathers user input to create dictionary that will be added to recipes_list

def take_recipe():

  name = str(input("Enter recipe name: "))

  while True:
    try:
      cooking_time = int(input("Enter cook time (in minutes): "))
      if cooking_time <= 0:
        print('---------------------------------------')
        print('--- Please enter valid cooking time ---')
        print('---------------------------------------')
      else:
        break
    except ValueError:
      print('---------------------------------------')
      print('--- Please input whole numbers only ---')
      print('---------------------------------------')

  ingredients = set(input("Enter the ingredients, separated by a comma: ").lower().split(", "))

  recipe = {
    'Name': name, 
    'Cooking Time (min)': cooking_time, 
    'Ingredients': ingredients
    }
  
  return recipe

# When the script is ran, the user is asked how many recipes to create
# If the user inputs anything but a whole number,
# they are prompted to enter a whole number or something greater than 0

while True:
  try:
    n = int(input("How many recipes would you like to add? "))
    if n <= 0:
      print('----------------------------------------')
      print('--- Please enter at least one recipe ---')
      print('----------------------------------------')
    else:
      break
  except ValueError:
    print('---------------------------------------')
    print('--- Please input whole numbers only ---')
    print('---------------------------------------')

# Creates for loop to be ran 'n' amount of times
# Calls take_recipe() 'n' times
# Checks ingredients_list for the ingredients entered by the user

for i in range(n):
  recipe = take_recipe()

  for ingredient in recipe['Ingredients']:
    if not ingredient in ingredients_list:
      ingredients_list.append(ingredient)

  recipes_list.append(recipe)

# for loop that iterates through each recipe created to determine difficulty
# Calculates difficulty based on cooking time and ingredient list length

for recipe in recipes_list:

  if recipe['Cooking Time (min)'] < 10 and len(recipe['Ingredients']) < 4:
    recipe['Difficulty'] = 'Easy'

  elif recipe['Cooking Time (min)'] < 10 and len(recipe['Ingredients']) >= 4:
    recipe['Difficulty'] = 'Medium'
  
  elif recipe['Cooking Time (min)'] >= 10 and len(recipe['Ingredients']) < 4:
    recipe['Difficulty'] = 'Intermediate'
  
  elif recipe['Cooking Time (min)'] >= 10 and len(recipe['Ingredients']) >= 4:
    recipe['Difficulty'] = 'Hard'

# Once user is done entering recipes and difficulty is calculated,
# each recipe is printed

  print('----------------------------------------')
  print('')
  print('Recipe: ', recipe['Name'].capitalize())
  print('Cooking Time (min): ', recipe['Cooking Time (min)'])
  print('Ingredients: ')
  for ingredient in recipe['Ingredients']:
    print(ingredient.capitalize())
  print('Difficulty: ', recipe['Difficulty'])
  print('')

# Function that is called at the end 
# to print all ingredients added to ingredients_list

def show_ingredients():
  print('Ingredients Available Across All Recipes')
  print('----------------------------------------')
  ingredients_list.sort()
  for ingredient in ingredients_list:
    print(ingredient.capitalize())

show_ingredients()