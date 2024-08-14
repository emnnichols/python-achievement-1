import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.types import Integer, String

load_dotenv()
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_name = os.environ.get('DB_NAME')

engine = create_engine(f"mysql://{db_user}:{db_pass}@localhost/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

### Reusable divider for app messages
divide = f"\n{32*'-'}\n"

# Declarative Base Class for Database Table
class Recipe(Base):
  __tablename__ = "final_recipes"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  def __repr__(self):
    return "<Recipe ID: " + str(self.id) + " - " + self.name + "( " + self.difficulty + " )" + ">"
  
  def __str__(self):
    return (f"{4*' '}{self.id} - {self.name.upper()}\n"
            + f"\n{4*' '}Time: {self.cooking_time} minutes\n"
            + f"{4*' '}Difficulty: " + self.difficulty + "\n"
            + f"{4*' '}Ingredients: " + self.ingredients
            )
  
  def calculate_difficulty(self):
    time = self.cooking_time
    num_ingredients = len(self.return_ingredients_as_list())

    if (time < 10 and num_ingredients < 4):
        self.difficulty = 'Easy'
    elif (time < 10 and num_ingredients >= 4):
        self.difficulty = 'Medium'
    elif (time >= 10 and num_ingredients < 4):
        self.difficulty = 'Intermediate'
    elif (time >= 10 and num_ingredients >= 4):
        self.difficulty = 'Hard'
  
  def return_ingredients_as_list(self):
    if self.ingredients == "":
      return []
    else:
      return self.ingredients.split(', ')

Base.metadata.create_all(engine)

# Main Operations

## Recipe creation
def create_recipe():
  ### Alerts user to which operation they are doing
  print(divide + f"\n{8*' '}RECIPE  CREATION\n" + divide)

  ### Prompts user for recipe name
  ### Checks to make sure name is not empty or more than 50 chars
  name = str(input("Enter Recipe Name: ")).title()

  while name == '':
    print(divide + f"\n{2*' '}*** name cannot be empty ***\n" + divide)
    name = str(input("\nEnter Recipe Name: ")).title()
  
  while len(name) > 50:
    print(f"\n{52*'-'}\n\n{3*' '}oops! try something shorter than 50 characters\n\n{52*'-'}\n")
    name = str(input("\nEnter Recipe Name: ")).title()

  ### Prompts user for recipes cooking time
  ### Checks if input is empty or not numerical
  cooking_time = input("\nEnter cooking time (minutes): ")

  while cooking_time == '':
    print(divide + f"\n{3*' '}please enter cooking time!\n" + divide)
    cooking_time = input("\nEnter cooking time (minutes): ")

  while not cooking_time.isnumeric() or int(cooking_time) == 0:
    print(divide + f"\n{5*' '}input must be a number\n" + divide)
    cooking_time = input("\nEnter cooking time (minutes): ")

  ### Prompts user to enter how many ingredients to enter
  ### User will enter each ingredient separately, each getting appended to list
  ### List will then be joined into a string
  num_of_ingredients = input("\nHow many ingredients would you like to enter? ")

  while num_of_ingredients == '' or not num_of_ingredients.isnumeric():
    print(divide + f"\n{2*' '}** input # of ingredients **\n" + divide)
    num_of_ingredients = input("\nHow many ingredients would you like to enter? ")

  while int(num_of_ingredients) == 0:
    print(divide + f"\n{2*' '}You must enter an ingredient\n" + divide)
    num_of_ingredients = input("\nHow many ingredients would you like to enter? ")

  ingredients = []

  try:
    for i in range(int(num_of_ingredients)):
      ingredient = input(f"\n\tEnter ingredient #{i+1}: ")
      while ingredient == '' or not ingredient.replace(" ", "").isalpha():
        print(divide + f"\n{1*' '}*** enter valid ingredient ***\n" + divide)
        ingredient = input(f"\tEnter ingredient #{i+1}: ")
      ingredients.append(ingredient.title())

    ingredient_str = ', '.join(ingredients)
  except:
    print(divide + 4*' ' + "*** unexpected error ***")
    print(5*' ' + "returning to Main Menu" + divide)
    return None
  
  ### Create Recipe object from inputs
  recipe_entry = Recipe(
    name = name,
    cooking_time = int(cooking_time),
    ingredients = ingredient_str
  )
  ### Calculate recipes difficulty level
  recipe_entry.calculate_difficulty()

  ### Add recipe to table and commit changes
  try:
    session.add(recipe_entry)
    session.commit()
    print(divide + "\n** recipe added successfully! **\n" + divide)
    print(recipe_entry)
  except:
    print(divide + 4*' ' + "*** unexpected error ***")
    print(5*' ' + "returning to Main Menu" + divide)
    return None

## View all recipes in db
def view_all_recipes():
  num_of_recipes = session.query(Recipe).count()

  if num_of_recipes == 0:
    print(divide + f"\n{4*' '}*** No Recipes Found ***\n" + 1*' ' + "press enter to return to start\n" + divide)
    input()
    return None
  elif num_of_recipes == 1:
    print(divide + f"\n{6*' '}Viewing Recipe List" + f"\n{7*' '}* {num_of_recipes} Recipe Found *\n" + divide)
  else:
    print(divide + f"\n{6*' '}Viewing Recipes List" + f"\n{6*' '}* {num_of_recipes} Recipes Found *\n" + divide)

  recipes = session.query(Recipe).all()

  for recipe in recipes:
    print(f"{recipe}\n\n")

  print(f"{4*' '}(end of list)" + divide)

## Search recipes by ingredient
def search_by_ingredients():
  ### Checks if there are recipes
  if session.query(Recipe).count() == 0:
    print(divide + f"\n{4*' '}*** No Recipes Found ***\n" + 1*' ' + "press enter to return to start\n" + divide)
    input()
    return None
  
  print(divide + f"\n{4*' '}*** Ingredients List ***\n" + divide)
  
  ### Retrieves ingredients found in all recipes
  results = session.query(Recipe.ingredients).all()

  ### Initialize empty set - to avoid duplicates
  all_ingredients = set()

  ### For loop that goes through each recipe
  ### Adds ingredients from each recipe to temporary list
  ### Temp list then gets added to all_ingredients set
  for tup in results:
    temp_list = ','.join(list(tup)).split(', ')
    for ing in temp_list:
      all_ingredients.add(ing)

  ingredient_str = ', '.join(all_ingredients)
  ing_list = sorted(ingredient_str.split(', '))

  ### Creates list of all_ingredients
  options = []

  ### For loop that runs through each ingredient
  ### Prints each ingredient in a numbered list
  for i, ingredient in enumerate(ing_list):
    print(f"{i+1}. {ingredient}")
    options.append(i+1)

  ### Instructions printed to user to type ingredient number
  ### and to separate each number with a space if searching for > 1 ingredient
  print(f"\n{4*' '}Type the # next to the ingredient or type exit")
  print(f"{4*' '}To search for more than one ingredient, separate #'s by spaces\n")

  ### Prompt user to enter ingredient number(s) to search for
  ### Or type exit to return to main menu
  choice_input = input(f"\n{4*' '}Which ingredient(s) would you like to search? ")

  if choice_input == 'exit':
    print(divide + '\n *** returning to main menu ***\n' + divide)
    return None
  
  while choice_input == '' or not choice_input.replace(" ", "").isnumeric():
    print(f"\n{40*'-'}\n\n*** please enter at least one number ***\n\n{40*'-'}\n")
    choice_input = input(f"\n{4*' '}Which ingredient(s) would you like to search? ")
  
  choice = choice_input.split(' ')
  search_for = []

  #### For loop that checks if number(s) entered are valid
  for num in choice:
    while int(num) not in options:
      print(divide + f"\n{1*' '}*** {num} is not a valid input ***\n" + divide)
      if choice_input == 'exit':
        return None
      choice_input = input(f"\n{4*' '}Which ingredient(s) would you like to search? ")

    try:
      for i in options:
        if int(num) == i:
          ing = ing_list[i-1]
          search_for.append(ing)
        else:
          continue
    except:
      print(divide + f"\n{1*' '}*** {num} is not a valid input ***")
      print(f"{1*' '}*** returning to Main Menu ***\n" + divide)
      return None

  conditions = []

  #### For each ingredient found, runs for loop to create a like() condition 
  #### Appends each condition to conditions list
  for ingredient in search_for:
    like_term = f"%{ingredient}%"
    conditions.append(Recipe.ingredients.like(f"{like_term}"))

  #### Queries table to filter results using conditions
  #### Then prints each recipe returned
  search_results = session.query(Recipe).filter(*conditions).all()

  if not search_results:
    print(divide + f"\n{2*' '}no recipes found containing \n{4*' '}{', '.join(search_for).replace(',', ' +')}\n" + f"\n{1*' '}press enter to return to start\n" + divide)
    input()
    return None
  else:
    num_of_recipes = len(search_results)
    print(f"\n\n{7*'*'} {num_of_recipes} Recipe(s) Found {7*'*'}\n")
    for recipe in search_results:
      print(f"\n{recipe}\n")
    print(f"\n{10*'*'} end of list {10*'*'}\n")

## Edit existing recipes
def edit_recipe():  
  ### Checks if there are recipes
  num_of_recipes = session.query(Recipe).count()

  if num_of_recipes == 0:
    print(divide + f"\n{4*' '}*** No Recipes Found ***\n" + 1*' ' + "press enter to return to start\n" + divide)
    input()
    return None
  elif num_of_recipes == 1:
    print(divide + f"\n{6*' '}Viewing Recipes List" + f"\n{2*' '}* {num_of_recipes} Recipe can be Modified *\n" + divide)
  else:
    print(divide + f"\n{6*' '}Viewing Recipes List" + f"\n{1*' '}* {num_of_recipes} Recipes can be Modified *\n" + divide)

  recipes = session.query(Recipe.id, Recipe.name).all()
  options = []

  for recipe in recipes:
    print(f"\n{4*' '}{recipe[0]}. {recipe[1]} \n")
    options.append(recipe[0])

  user_input = input(f"\n{4*' '}Which recipe would you like to modify? ")

  if user_input == 'exit':
    print(divide + f"\n{1*' '}*** returning to Main Menu ***\n" + divide)
    return None
  
  while not user_input.isnumeric():
    print(divide + f"\n*** input should be a number ***\n" + divide)
    user_input = input(f"\n{4*' '}Which recipe would you like to modify? ")

  while int(user_input) not in options:
    print(divide + f"\n** {user_input} not an option, try again **\n" + divide)
    user_input = input(f"\n{4*' '}Which recipe would you like to modify? ")

  recipe_to_edit = session.query(Recipe).filter(Recipe.id == user_input).one()

  print(f"\n\t1. Name ({recipe_to_edit.name})")
  print(f"\t2. Ingredients ({recipe_to_edit.ingredients})")
  print(f"\t3. Cooking time ({recipe_to_edit.cooking_time} minutes)")

  choice = input(f"\n{4*' '}What would you like to update? ")

  ### Prompts user for a new input if input is not a number or valid option
  if not choice == 'exit':
    while not choice.isnumeric() or not (1 <= int(choice) <= 3):
      print(divide + f"** {choice} not an option, try again **" + divide)
      choice = input(f"\n\n{4*' '}What would you like to update? ")
  
  if choice == 'exit':
    print(divide + f"\n{1*' '}*** returning to Main Menu ***\n" + divide)
    return None
  
  ### Editing recipe name
  elif int(choice) == 1:
    update_name = input(f"\n{4*' '}Enter new recipe name: ").title()
    while len(update_name) > 50 or len(update_name) == 0:
      print(f"{divide}\n{4*' '}*** Name entered is too long ***\n{divide}")
      update_name = input("\nEnter new recipe name: ").title()
    try:
      recipe_to_edit.name = update_name
      session.query(Recipe).filter(Recipe.id == user_input).update({Recipe.name: recipe_to_edit.name})
      print(f"\n{4*' '}*** Recipe name updated to: {recipe_to_edit.name}")
    except:
      print(divide + 2*' ' + "** oops, something broke! **\n" + 5*' ' + "returning to Main Menu" + divide)
      return None
  ### Editing recipe ingredients
  elif int(choice) == 2:
    num_of_ingredients = input(f"\n{4*' '}How many ingredients would you like to enter? ")

    while num_of_ingredients == '' or not num_of_ingredients.isnumeric():
      print(divide + f"\n{2*' '}** input # of ingredients **\n" + divide)
      num_of_ingredients = input("\nHow many ingredients would you like to enter? ")

    while int(num_of_ingredients) == 0:
      print(divide + f"\n{2*' '}You must enter an ingredient\n" + divide)
      num_of_ingredients = input("\nHow many ingredients would you like to enter? ")

    ingredients = []

    try:
      for i in range(int(num_of_ingredients)):
        ingredient = input(f"\n\tEnter ingredient #{i+1}: ")
        while ingredient == '' or not ingredient.replace(" ", "").isalpha():
          print(divide + f"\n{1*' '}*** enter valid ingredient ***\n" + divide)
          ingredient = input(f"\tEnter ingredient #{i+1}: ")
        ingredients.append(ingredient.title())

      ingredient_str = ', '.join(ingredients)
      recipe_to_edit.ingredients = ingredient_str

      session.query(Recipe).filter(Recipe.id == user_input).update({Recipe.ingredients: recipe_to_edit.ingredients})
      print(f"\n{4*' '}*** Ingredients updated to: {recipe_to_edit.ingredients}")
    except:
      print(divide + 4*' ' + "*** unexpected error ***")
      print(5*' ' + "returning to Main Menu" + divide)
      return None

  ### Editing recipe cooking time
  elif int(choice) == 3:
    update_time = input(f"\n{4*' '}Enter new cooking time (minutes): ")
    while not update_time.isnumeric() or int(update_time) == 0:
      print(f"\n\n{50*'-'}\n\n*** input needs to be a number and cannot be 0 ***\n\n{50*'-'}\n\n")
      update_time = input("\nEnter new cooking time (minutes): ")
    try:
      recipe_to_edit.cooking_time = int(update_time)
      session.query(Recipe).filter(Recipe.id == user_input).update({Recipe.cooking_time: recipe_to_edit.cooking_time})
      print(f"\n{4*' '}*** Cooking time updated to: {recipe_to_edit.cooking_time} minutes")
    except:
      print(divide + 2*' ' + "** oops, something broke! **\n" + 5*' ' + "returning to main menu" + divide)
      return None
  else:
    print(divide + f"\n{2*' '}** oops, something broke! **\n{5*' '}returning to main menu\n" + divide)
    return None    

  #### Recalculate recipes difficulty level before commiting changes
  recipe_to_edit.calculate_difficulty()
  session.commit()
  print(f"{divide}\nUpdated Recipe:\n\n{recipe_to_edit}")

## Delete recipe from database
def delete_recipe():
  ### Checks if there are recipes
  if session.query(Recipe).count() == 0:
    print(divide + f"\n{4*' '}*** No Recipes Found ***\n" + 1*' ' + "press enter to return to start\n" + divide)
    input()
    return None
  
  print(divide + f"\n{6*' '}Viewing Recipes List\n" + divide)
  options = []

  ### Retrieves recipe id and name
  results = session.query(Recipe.id, Recipe.name).all()
  for recipe in results:
    print(f"{4*' '}{recipe[0]}. {recipe[1]}\n")
    options.append(recipe[0])

  user_input = input(f"{4*' '}Which recipe would you like to delete? ")

  if user_input == 'exit':
    print(divide + f"\n{1*' '}*** returning to Main Menu ***\n" + divide)
    return None
  
  while user_input == '' or not user_input.isnumeric():
    print(divide + f"\n{3*' '}*** valid input needed ***")
    print(f"{4*' '}please enter a # or exit\n" + divide)
    user_input = input(f"{4*' '}Which recipe would you like to delete? ")

  while int(user_input) not in options:
    print(divide + f"\n{2*' '}*** number was not found ***\n" + divide)
    user_input = input(f"{4*' '}Which recipe would you like to delete? ")

  recipe_to_delete = session.query(Recipe).filter(Recipe.id == user_input).one()
  print(divide + f'\n{recipe_to_delete}' + divide)
  confirm = input(f"\n{4*' '}Delete this recipe? Type Y/N: ").lower()
  if confirm == 'y' or confirm == 'yes':
    try:
      session.delete(recipe_to_delete)
      session.commit()
      print(divide + f"\n{5*' '}*** recipe deleted ***")
      print(5*' ' + "returning to Main Menu\n" + divide)
    except:
      print(divide + f"\n{4*' '}*** unexpected error ***")
      print(5*' ' + "returning to Main Menu\n" + divide)
  elif confirm == 'n' or confirm == 'no':
    print(divide + f"\n{1*' '}*** recipe was not deleted ***")
    print(5*' ' + "returning to Main Menu\n" + divide)
    return None
  else:
    print(divide + f"\n{4*' '}*** unexpected error ***")
    print(5*' ' + "returning to Main Menu\n" + divide)
    return None

# Main Menu
def main_menu():
  while True:
    try:
      print(divide + f"\n{9*' '}WELCOME TO THE\n{9*' '}* Recipe App *\n" + divide)
      print("What would you like to do? Choose from below!\n")
      options = ["Create a Recipe", "View All Recipes", "Search by Ingredient(s)", "Update a Recipe", "Delete a Recipe", "Exit"]

      option_num = enumerate(options)

      for i, option in option_num:
        print(f"{4*' '}{i+1}. {option}")

      choice = input("\nEnter your choice: ")

      while choice == '' or not choice.isnumeric():
        print(divide + f"\n{2*' '}*** please choose a task ***\n" + divide)
        choice = input("\nEnter your choice: ")

      num = int(choice)

      while num < 1 or num > len(options):
        print(divide + f"\n{1*' '}*** enter number from list ***\n" + divide)
        choice = input("\nEnter your choice: ")
        num = int(choice)

      if 1 <= num <= len(options):
        if num == 1:
          create_recipe()
        elif num == 2:
          view_all_recipes()
        elif num == 3:
          search_by_ingredients()
        elif num == 4:
          edit_recipe()
        elif num == 5:
          delete_recipe()
        elif num == 6:
          print(divide + f"\n{3*' '}*** exiting recipe app ***\n" + divide)
          return None
    except Exception as e:
      print(e)
      print(divide + f"\n{4*' '}*** unexpected error ***")
      print(4*' ' + "** exiting recipe app **\n" + divide)
      return None

# Main Code
main_menu()
session.close()
engine.dispose()