import pickle

def take_recipe():
  name = str(input("\nEnter recipe name: "))

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
    'Ingredients': ingredients,
    'Difficulty': calc_difficulty(cooking_time, len(ingredients))
    }
  
  return recipe

def calc_difficulty(time, ingredients):
  if time < 10 and ingredients < 4:
    return 'Easy'
  
  elif time < 10 and ingredients >= 4:
    return 'Medium'
  
  elif time >= 10 and ingredients < 4:
    return 'Intermediate'
  
  elif time >= 10 and ingredients >= 4:
    return 'Hard'

# main code
# Prompt user for filename

filename = input("What file would you like to open? ")

# Load existing file or create new dictionary 

try:
  with open(filename, 'rb') as file:
    data = pickle.load(file)
except FileNotFoundError:
  print("No file found! Creating new recipe dictionary.")
  data = {'recipes_list': [], 'all_ingredients': []}
except:
  print("Unexpected error occurred!")
  data = {'recipes_list': [], 'all_ingredients': []}
finally:
  recipes_list, all_ingredients = data['recipes_list'], data['all_ingredients']

# Prompts user for how many recipes to create
# Must be greater than 0 and a whole number

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

  recipes_list.append(recipe)

  for ingredient in recipe['Ingredients']:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)

# Save updated lists and write the updated data to <filename>

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

with open(filename, 'wb') as file:
  pickle.dump(data, file)

print('\nRecipes successfully saved!')