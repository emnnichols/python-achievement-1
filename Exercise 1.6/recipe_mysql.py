import mysql.connector

conn = mysql.connector.connect(
  host='localhost',
  user='cf-python',
  passwd='password')
cursor = conn.cursor()

## Create MySQL database for task
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

## Create table to store recipe information
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
              id INT PRIMARY KEY AUTO_INCREMENT,
              name VARCHAR(50),
              ingredients VARCHAR(255),
              cooking_time INT,
              difficulty VARCHAR(20))''')

## Main menu that has the user choose what they would like to do
## User can create, update, or delete a recipe; or search recipes by ingredient
def main_menu(conn, cursor):
  while True:
    print('\n' + 30*'=')
    print('\n\tMain Menu\n')
    print(30*'=')
    print('\nWhat would you like to do?\n')
    print('1. Create a recipe')
    print('2. Search by ingredient')
    print('3. Update a recipe')
    print('4. Delete a recipe')
    print('5. Exit')
    choice = input('\nYour choice: ').lower()

    if choice == '1':
      create_recipe(conn, cursor)

    elif choice == '2':
      search_recipe(conn, cursor)

    elif choice == '3':
      update_recipe(conn, cursor)

    elif choice == '4':
      delete_recipe(conn, cursor)

    elif choice == '5':
      print('\n' + 30*'=')
      print('\nThank you for using the Recipe app!\n')
      print(30*'=')
      break

    else:
      print('\n*** Something went wrong ***\n*** Please enter 1, 2, 3, 4, or 5 ***')

## Defines function for creating recipes
## Prompts users for recipe name, cooking time, and ingredients
def create_recipe(conn, cursor):
  print(30*'=')
  print('\nRecipe Creation\n')
  print(30*'=')
  name = str(input('\nEnter recipe name: ')).title()
  cooking_time = int(input('\nCooking time in minutes: '))
  ingredient_input = input('\nList the ingredients, separated by commas: ')
  ingredients = ingredient_input.split(", ")
  ingredients_str = ", ".join(ingredients)

  difficulty = calculate_difficulty(cooking_time, ingredients)

  try:
    insert_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (name, ingredients_str, cooking_time, difficulty))
    conn.commit()
    print('\nRecipe successfully added!\n')
  except mysql.connector.Error as err:
    print('\nUnexpected error occured!\n' + str(err))

  print("... now returning to the main menu!\n")

## Defines function that calculates a recipes difficulty
## Is called in create_recipe() and update_recipe
def calculate_difficulty(time, ingredients):
  num_ingredients = len(ingredients)
  if (time < 10 and num_ingredients < 4):
      return 'Easy'
  elif (time < 10 and num_ingredients >= 4):
      return 'Medium'
  elif (time >= 10 and num_ingredients < 4):
      return 'Intermediate'
  elif (time >= 10 and num_ingredients >= 4):
      return 'Hard'

## Defines function that gathers all ingredients from recipes
## then prompts user to choose ingredient to search
def search_recipe(conn, cursor):
  cursor.execute('SELECT ingredients FROM Recipes')
  results = cursor.fetchall()

  if not results:
    print("\nNo Recipes Found!\n\n *** returning to main menu ***")
  else:
    ## Set of all the ingredients to avoid duplicates
    all_ingredients = set()

    for recipe in results:
      recipe_ingredients = recipe[0].split(", ")
      for ingredient in recipe_ingredients:
        all_ingredients.add(ingredient.strip().title())

    print('\n' + 30*'=')
    print('\nSearchable Ingredients\n')
    print(30*'=' + '\n')
    
    ## Numbered list of all the ingredients found
    for i, ingredient in enumerate(sorted(all_ingredients)):
      print(f'{i+1}. {ingredient}')

    while True:
      ## Prompts user to enter a number or exit
      ## Empty or invalid inputs will kick back a warning
      ## Typing exit will take user back to main menu
      try:
        choice = input('\nEnter ingredient number to search or type exit: ')
        if choice == '':
          print('\n*** Cannot be empty, please enter a number ***')
        elif choice == 'exit':
          print('\n*** returning to main menu ***')
          break
        elif 1<= int(choice) <= len(all_ingredients):
          search_ingredient = sorted(all_ingredients)[int(choice)-1]
          if search_ingredient:
            try:
              search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
              cursor.execute(search_query, ("%" + search_ingredient + "%",))
              search_results = cursor.fetchall()
              
              if search_results:
                recipe_count = len(search_results)
                print(f'\n*** {recipe_count} Recipe(s) Found Containing {search_ingredient} ***\n')
                for recipe in search_results:
                  print(30*'=' + '\n')
                  print(f"*** {recipe[1]} ***")
                  print("Ingredients: " + recipe[2].title())
                  print("Cooking Time: " + str(recipe[3]) + " minutes")
                  print("Difficulty: " + recipe[4])
              else:
                print('No recipes found with ' + search_ingredient)
            except:
              print('*** Unexpected error ***')
          break
        else:
          print('\n*** Please enter a valid number ***')
      except mysql.connector.Error as err:
        print('\nUnexpected error occured!\n' + str(err))

## Defines function that updates a single column value at a time
## Prompts user for recipe ID and which field they would like to update
def update_recipe(conn, cursor):
  cursor.execute("SELECT * FROM Recipes")
  results = cursor.fetchall()

  if not results:
    print("\nNo Recipes Found!\n... returning to main menu")
  else:
    print(30*'=')
    print('\n Recipes Available to Update \n')
    print(30*'=')

    for recipe in results:
      print("\n*** " + recipe[1] + " ***")
      print("\nID: " + str(recipe[0]))
      print("Ingredients: " + recipe[2].title())
      print("Time: " + str(recipe[3]) + " minutes")
      print("Difficulty: " + str(recipe[4]))
    
    while True:
      ## Prompts user to enter an ID or exit
      ## Empty inputs will kick back a warning
      ## Typing exit will take user back to main menu
      ## Checks ID entered by user to check if it exists 
      try:
        choice = input('\nPlease enter recipe ID or type exit: ')
        if choice == '':
          print('\n*** Cannot be empty, please enter an ID or exit ***')
        elif choice == 'exit':
          print('\n*** returning to main menu ***')
          break
        else:
          cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (choice,))
          if cursor.fetchone()[0] == 0:
            print("\n*** ID entered was not found ***\n*** Please enter valid ID ***")
          else:
            print('\n 1. Name\n 2. Cooking time\n 3. Ingredients\n')
            column_input = input(' Which field would you like to update? ')

            if column_input == '1':
              value = str(input(f'\n Enter new name: '))
              cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (value, choice,))
            elif column_input == '2':
              value = int(input(f'\n Enter new cooking time: '))
              cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (value, choice,))
            elif column_input == '3':
              value = str(input(f'\n Enter new ingredients: '))
              cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (value, choice,))

            ## Recalculates the recipes difficulty if num of ingredients or cooking time is changed
            if column_input in ['2', '3']:
              cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (choice,))
              recipe = cursor.fetchone()

              new_difficulty = calculate_difficulty(int(recipe[0]), recipe[1].split(", "))

              cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (new_difficulty, choice,))
              print(f'\nDifficulty has been updated to {new_difficulty}!')

            conn.commit()
            print('\nRecipe updated successfully!\n...now returning to the main menu')
            break
      except mysql.connector.Error as err:
        print("\nUnexected error, please try again." + str(err))

## Defines function that deletes a single row / recipe
## Prompts user for recipe ID
def delete_recipe(conn, cursor):
  cursor.execute("SELECT * FROM Recipes")
  results = cursor.fetchall()

  if not results:
    print("\nNo Recipes Found!\n... returning to main menu")
  else:
    print(30*'=')
    print('\n Recipes Available to Delete \n')
    print(30*'=')

    for recipe in results:
      print("\n*** " + recipe[1] + " ***")
      print("ID: " + str(recipe[0]))
      print("Ingredients: " + recipe[2])
      print("Cooking Time: " + str(recipe[3]))
    
    while True:
      ## Prompts user to enter an ID or exit
      ## Empty inputs will kick back a warning
      ## Typing exit will take user back to main menu
      ## Checks ID entered by user to check if it exists 
      try:
        choice = input('\nPlease enter the recipe ID to delete or type exit: ')
        if choice == '':
          print('\n*** Cannot be empty, please enter an ID or exit ***')
        elif choice == 'exit':
          print('\n*** returning to main menu ***')
          break
        else:
          cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (choice,))
          if cursor.fetchone()[0] == 0:
            print("\n*** ID entered was not found ***\n*** Please enter valid ID ***")
          else:
            cursor.execute("DELETE FROM Recipes WHERE id = %s", (choice,))        
            conn.commit()
            print('\n*** Recipe deleted successfully! ***')
            break
      except mysql.connector.Error as err:
        print("\nUnexected error, please try again." + str(err))

## Main code

main_menu(conn, cursor)