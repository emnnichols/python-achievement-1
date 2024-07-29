import pickle

# Function that is called for recipes matching ingredient search
# Determines the format of how each recipe is printed

def display_recipe(recipe):
  print(recipe['Name'].title())
  print(" Time: " + str(recipe['Cooking Time (min)']) + " mins")
  print(" Difficulty: " + recipe['Difficulty'])
  print(" Ingredients: ")
  for ingredient in recipe['Ingredients']:
    print(' - ' + ingredient.title())
  print('\n------------------------------\n')

def search_ingredient(data):
  all_ingredients = data['all_ingredients']
  all_ingredients.sort()

  print('\n-------- Ingredients List --------\n')

  # Enumerates all_ingredients to get index and adds 1
  # Prints each ingredient in numbered list

  for i, ingredient in enumerate(all_ingredients):
    print(str(i+1) + ".) " + ingredient.title())
  
  # Prompts user to enter which ingredient they want to search
  # Uses associated number in list then subtracts 1 to find ingredient index

  try:
    while True:
      selection = int(input("\nWhich ingredient will you like to search? "))
      if 1 <= selection <= len(all_ingredients):
        ingredient_searched = all_ingredients[selection-1]
        break
  except:
    print("Incorrect input, please try again.")
  else:
    recipes_with_ingredient = [recipe for recipe in data['recipes_list'] if ingredient_searched in recipe['Ingredients']]     

    recipes_found = len(recipes_with_ingredient)
    print('\n' + str(recipes_found) + ' recipe(s) found containing ' + ingredient_searched.title())
    print('------------------------------\n')
    for recipe in recipes_with_ingredient:
      display_recipe(recipe)

# Main code starts here

# Prompt user to enter name of file with recipe data

filename = input('\n  What file would you like to search for recipes? ')

# Attempts to open specified folder
# Loads content into data and then passes it to search_ingredient()

while True:

  try:
    with open(filename, 'rb') as file:
      data = pickle.load(file)
  except FileNotFoundError:
    print('\n   ------------------------------')
    print('  File not found! Please try again.')
    print('   ------------------------------')
  except:
    print('Unexpected error occured!')
  else:
    search_ingredient(data)
    break