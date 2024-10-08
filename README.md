# Recipe app (CLI version)

This project is a precursor to building a web app counterpart with the Django web framework. The focus of this project is to learn Python fundamentals, data structures, and object-oriented programming. This project will also show how Python interacts with databases.

## Key Features

* Create and manage the user's recipes on a locally hosted MySQL database
* Option to search for recipes by ingredients
* Automatically rate each recipe by their difficulty level
* Display more details on each recipe if the user prompts it (e.g. ingredients, cooking time, and difficulty)

## User Goals

Users should be able to create and modify recipes with ingredients, cooking times, and a difficulty parameter that will be automatically calculated. Users should also be able to search for recipes by their ingredients.

## Table of Contents
- [Exercise 1.1](/#exercise-1--getting-started-with-python)
- [Exercise 1.2](/#exercise-2--data-types-in-python)
- [Exercise 1.3](/#exercise-3--operators-and-functions-in-python)
- [Exercise 1.4](/#exercise-4--file-handling-in-python)
- [Exercise 1.5](/#exercise-5--oop-in-python)
- [Exercise 1.6](/#exercise-6--databases-in-python)
- [Exercise 1.7](/#exercise-7--object-relational-mapping-in-python)

### Exercise 1 | Getting Started with Python

- Preparing your developer environment for programming with Python

  <details>
    <summary>Step-by-Step</summary>
  
  #### Step 1: Install Python
  * Install Python on your system or check that Python is already installed
  * Verify the correct version is installed with `python --version`
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of checking Python version](/Exercise%201.1/Step%201_Install%20Python.png)
    
    </details>
  
  #### Step 2: Set up new virtual environment
  * Use `mkvirtualenv` to make a new virtual environment called cf-python-base
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of making new virtual environment](/Exercise%201.1/Step%202_New%20Virt%20Env.png)
    </details>
  
  #### Step 3: Create 'add.py' script
  * Create a script that adds two numbers that the user inputs
  * Store user input into a variable using `variable = int(input("Prompt"))`
  * Store product of the two numbers into a separate variable
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of creating the script that adds two numbers together](/Exercise%201.1/Step%203_VS%20Code.png)
    </details>
  
  #### Step 4: Install IPython
  * Using  `pip install`, install ipython
  * Verify installation by launching an IPython shell with `ipython`
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of installing ipython](/Exercise%201.1/Step%204_Install%20IPython.png)
    </details>
  
  #### Step 5: Install Export Requirements file
  * Use `pip install` command to generate a requirements.txt file from the environment created
  * Create a new virtual environment
  * Use `pip install -r` to install from the requirements.txt
    <details>
      <summary>Screenshots</summary>
      
    ![Screenshot of generating requirements.txt file](/Exercise%201.1/Step%205a_Requirements%20file.png)
      
    ![Screenshot of creating new virual environment](/Exercise%201.1/Step%205b_Copy%20env.png)
    
    ![Screenshot of using the requirements.txt file with pip install](/Exercise%201.1/Step%205c_%20Pip%20install%20requirements.png)
    </details>
    
  </details>

### Exercise 2 | Data Types in Python

- Create data structure for the Recipe app

  <details>

  <summary>Data Structures</summary>
  
  * For the individual recipes, I decided to use a dictionary data structure. Because each recipe will be storing a mix of data types, the need for key-value pairs, and must have the ability to be modified, dictionaries best fit the needs.
  
    
    `recipe = {'Name': str, 'Cooking time:' int, 'Ingredients': [list]}`
  
  * For the outer structure, I have decided to use a list data structure. Due to the criteria that `all_recipes` should be sequential and can be modified as required, the best structure would be a list.
  
    `all_recipes = []`
  </details>

  <details>
  
  <summary>Step-by-Step</summary>
  
  #### Step 1: Creating recipe_1
  * Using the chosen data structure, create `recipe_1`
  
    <details>
    
      <summary>Screenshot</summary>
      
    ![Screenshot of Tea Recipe](/Exercise%201.2/Step%201_Create%20Recipe.png)
    
    </details>
  
  #### Step 2: Adding recipe_1 to all_recipes
  * Using the chosen data structure, create `all_recipes`
  * Add `recipe_1` to the outer structure, `all_recipes`
  
    <details>
      <summary>Screenshot</summary>
    
    ![Screenshot of Creating All Recipes](/Exercise%201.2/Step%202a_Create%20all%20recipes.png)
    
    ![Screenshot of Adding Recipe to List](/Exercise%201.2/Step%202b_Adding%20Recipe%20to%20List.png)
    
    </details>
  
  #### Step 3: Creating more recipes
  * Create 4 additional recipes
  * Add these recipes to the `all_recipes` list
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of New Recipes](/Exercise%201.2/Step%203a_Create%20Recipes.png)
    
    ![Screenshot of Adding Recipes to List](/Exercise%201.2/Step%203b_Add%20Recipes%20to%20List.png)
    
    </details>
  
  #### Step 4: Ingredient lists
  * Print the ingredients of each recipe as different lists
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.2/Step%204_Ingredient%20Lists.png)
    
    </details>
  </details>

### Exercise 3 | Operators and Functions in Python

- Create script for user recipe input

  <details>

  <summary>Data Structures</summary>
  
  * Each recipe inputed by the user has the following structure:
    
    `recipe = {'Name': str, 'Cooking Time:' int, 'Ingredients': [list]}, 'Difficulty': str`
  
  * Each recipe entered by the user will be added to `recipes_list` and new ingredients will be added to `ingredients_list`
  </details>

  <details>
  
  <summary>Step-by-Step</summary>
  
  #### Step 1: Creating Exercise_1.3.py
  * Creating a Python script in VSCode
  
    <details>
    
      <summary>Screenshot</summary>
      
    ![Screenshot of Script](/Exercise%201.3/Step%201_Create%20script.png)
    
    </details>
  
  #### Step 2: Initialize Empty Lists
  * Initialized `recipes_list` that will hold all recipe dictionaries
  * Initialized `ingredients_list` that will hold all the ingredients
  
    <details>
      <summary>Screenshot</summary>
    
    ![Screenshot of Empty Lists](/Exercise%201.3/Step%202_Empty%20lists.png)
    
    </details>
  
  #### Step 3: Define `take_recipe` function
  * Takes user input to create `Name`, `Cooking Time`, and `Ingredients` variables
  * Stores variables inside `recipe` dictionary
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of New Recipes](/Exercise%201.3/Step%203_Define%20function.png)
    
    </details>
  
  #### Step 4: Prompt user for recipe amount
  * Asks user to input how many recipes they want to enter
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.3/Step%204_Variable%20n.png)
    
    </details>

  #### Step 5: Create `for` loop to run `n` times
  * Runs `take_recipe()` for how many times indicated by user and appends each recipe to `recipes_list`
  * Runs `for` loop to check if recipe's ingredients already exist in `ingredients_list`, if not, appends ingredient to list
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.3/Step%205_Recipe%20for%20Loop.png)
    
    </details>


  #### Step 6: Calculate recipe difficulty
  * Checks each recipe for cooking time and ingredients to set difficulty level
    * **easy**: < 10 mins and < 4 ingredients
    * **medium**: < 10 mins and >= 4 ingredients
    * **intermediate**: >= 10 mins and < 4 ingredients
    * **hard**: >= 10 mins and >= 4 ingredients
  * Display recipes in the following format:

  ```python
  Name: <name>
  Cooking Time (min): <cooking_time>
  Ingredients: <ingredients>
  Difficulty: <difficulty>
  ```
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.3/Step%206a_Difficulty%20for%20Loop.png)

    ![Screenshot of Ingredient Lists](/Exercise%201.3/Step%206b_Display%20recipe.png)
    
    </details>

  #### Step 7: Sort and print `ingredients_list`
  * Sorts `ingredients_list` alphabetically and prints each ingredient
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.3/Step%207_Show%20ingredients_list.png)
    
    </details>

  </details>

### Exercise 4 | File Handling in Python

- Create script for user input and storing recipes in local file
- Create script for user to search recipes

  <details>

  <summary>File Structures</summary>
  
  * Each recipe inputed by the user has the following structure:
    
    `{'Name': str, 'Cooking Time:' int, 'Ingredients': [list]}, 'Difficulty': str`
  
  * Each recipe entered by the user will be added to `recipes_list` and new ingredients will be added to `ingredients_list`
  * Both lists will be added to a dictionary with the variable `data`
  
  </details>

  <details>
  
  <summary>Part 1 (input script): Step-by-Step</summary>
  
  #### Step 1: Creating recipe_input.py and import pickle
  * Creating a Python script in VSCode
  * Import the `pickle` module
  
    <details>
    
      <summary>Screenshot</summary>
      
    ![Screenshot of Import](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%201.png)
    
    </details>
  
  #### Step 2: Define `take_recipe` function
  * Gathers user input for `Name`, `Cooking Time`, and `Ingredients` variables
  * Calls the `calc_difficulty()` function to determine recipe difficulty level
  * Returns completed recipe as a dictionary
  
    <details>
      <summary>Screenshot</summary>
    
    ![Screenshot of Function](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%202.png)
    
    </details>
  
  #### Step 3: Define `calc_difficulty` function
  * Checks each recipe for cooking time and ingredients to set difficulty level
    * **easy**: < 10 mins and < 4 ingredients
    * **medium**: < 10 mins and >= 4 ingredients
    * **intermediate**: >= 10 mins and < 4 ingredients
    * **hard**: >= 10 mins and >= 4 ingredients
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Difficulty Calculation](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%203.png)
    
    </details>
  
  #### Step 4: Open file or Create new dictionary
  * Asks user to input what file they would like to open
  * If file does not exist, or an error occurs, a new dictionary is created
  * Uses `try-except-else-finally` block
    * `try`: Opening file specified by user and load data via `pickle.load()`
    * `except`: Handles FileNotFoundError and other exceptions by alerting user and creating new dictionary
    * `else`: Closes file stream of file opened in `try` block
    * `finally`: Extracts dictionary data into `recipes_list` and `all_ingredients`

    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Try Except block](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%204.png)
    
    </details>

  #### Step 5: Define `for` loop
  * Prompts user for how many recipes to add
  * Runs `for` loop to call `take_recipe` `n` amount of times
  * Appends each recipe to `recipes_list`
  * Inner loop that checks `all_ingredients` and adds new ingredients
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%205.png)
    
    </details>

  #### Step 6 and 7: Gather updated lists and write into file
  * Adds updated `recipes_list` and `all_ingredients` into new dictionary, `data`
  * Opens binary file and writes `data` via `pickle.dump()`
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Ingredient Lists](/Exercise%201.4/Part%201%20-%20recipe_input.py/Part%201_Step%206-7.png)
    
    </details>

  </details>

    <details>
  
  <summary>Part 2 (search script): Step-by-Step</summary>
  
  #### Step 1: Creating recipe_search.py and import pickle
  * Creating a Python script in VSCode
  * Import the `pickle` module
  
    <details>
    
      <summary>Screenshot</summary>
      
    ![Screenshot of Import](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%201.png)
    
    </details>
  
  #### Step 2: Define `display_recipe` function
  * Takes a `recipe` dictionary as an argument
  * Prints all the recipe attributes in the following format:

  ```
  Recipe Name
  Time: cooking time in mins
  Difficulty: difficulty lvl
  Ingredients: 
  - ingredient
  ```
    <details>
      <summary>Screenshot</summary>
    
    ![Screenshot of Function](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%202.png)
    
    </details>
  
  #### Step 3: Define `search_ingredient` function
  * Takes `data` as an argument from loaded file
  * Prints all ingredients to the user with the format:
    * Sorts list alphabetically
    * Enumerates list in order to index each ingredient

    ```Ingredients List
    1.) ingredient 
    2.) ingredient 
    ....
    n.) ingredient
    ```
  * Implements `try-except` block
    * `try`: User inputs ingredient # they want to search and stores selection
    * `except`: User is alerted to invalid input
    * `else`: Takes selected ingredient and scans through the ingredients of each recipe then prints the found recipes

    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Function](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%203.png)
    
    </details>
  
  #### Step 4: Prompt user for recipe data file
  * Asks user to input what file they would like to open

    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Opening File](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%204.png)
    
    </details>

  #### Step 5, 6, and 7: Implement `try-except-else` block
  * `try`: attempts to open the file specified by user
    * Extracts content into `data` via `pickle.load()`
  * `except`: warns user that the file wasn't found
  * `else`: calls the `search_ingredient` function while passing `data` as an argument
  
    <details>
      <summary>Screenshot</summary>
      
    ![Screenshot of Try Block](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%205.png)
    
    ![Screenshot of Except Block](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%206.png)
    
    ![Screenshot of Else Block](/Exercise%201.4/Part%202%20-%20recipe_search.py/Part%202_Step%207.png)
    
    </details>

  </details>

### Exercise 5 | OOP in Python

- Create script that defines a custom class named Recipe
- Use class to generate recipe objects

  <details>
  
  <summary>Step-by-Step</summary>
  
  #### Step 1: Define custom Recipe class
  * Defining custom class with the following data attributes:
    * `name`, `ingredients`, `cooking_time`, `difficulty`
  
  #### Step 2: Define procedural attributes for `Recipe`
  * For recipe name:
    * `get_name(self)`
    * `set_name(self, name)`
  * For cooking time:
    * `get_cooking_time(self)`
    * `set_cooking_time(self, time)`
  * For ingredients:
    * `add_ingredients(self, *ingredients)`
    * `update_all_ingredients(self)`
    * `get_ingredients(self)`
    * `search_ingredients(self, ingredient)`
  * For difficulty level:
    * `calculate_difficulty(self, time, ingredients)`
    * `get_difficulty(self)`
  
  #### Step 3: Define `recipe_search` method
  * Parameters for this method include `data` and `search_term`
  * Uses a `for` loop to search recipe objects to find recipes containing `search_term`
  
  #### Step 4: Generate recipe objects
  * Using `Recipe` class, four recipes were generated and initialized with with a name
  * Cooking time, difficulty, and ingredients are added after intializing

  #### Step 5: Wrap recipes into a list
  * Utilizes `extend()` method to add recipes to list

  #### Step 6: Using `recipe_search` method
  * Search recipes for ingredients: `water`, `sugar`, `bananas`

  </details>

  <details>

  <summary>Script Execution</summary>

  ![Screenshot of Recipes](/Exercise%201.5/recipe_objects.png)

  ![Screenshot of Search](/Exercise%201.5/recipe_search_water.png)

  ![Screenshot of Search](/Exercise%201.5/recipe_search_sugar.png)

  ![Screenshot of Search](/Exercise%201.5/recipe_search_bananas.png)

  </details>

### Exercise 6 | Databases in Python

- Create recipes that are then stored in a database
- Search recipes in the database by ingredient
- Update/modify recipes in the database
- Delete recipes from the database

  <details>
  
  <summary>Step-by-Step</summary>
  
  #### Step 1: Create and Connect Database
  * Import `mysql.connector` module
  * Initialize connection object and a cursor object
  * Create database called `task_database`
  * Create table called `Recipes` to hold recipe info:
    * `id` is an integer and increments automatically
    * `name` is a string and has limit of 50 characters
    * `ingredients` is a string and has limit of 255 characters, stores ingredients as a string
    * `cooking_time` is an integer
    * `difficulty` is a string and has a limit of of 20 characters
  
  #### Step 2: Create Main Menu
  * Defines function `main_menu` that calls the following functions:
    * `create_recipe`
    * `search_recipe`
    * `update_recipe`
    * `delete_function`
  * Presents menu to user that assigns number to each option
  * User inputs number associated with task and main menu calls that function
  * Users can also exit the loop that then closes the connection and ends the program
  
  #### Step 3: Define `create_recipe` function
  * Prompts user to enter recipe name, cooking time, and ingredrients
  * The `calculate_difficulty` is called and the ingredients are joined into a string
  * INSERT query is then executed to add recipe to table
  
  #### Step 4: Define `search_recipe` function
  * Gathers ingredients from recipe database using SELECT on the ingredients column
  * Adds each unique ingredient found to a list, `all_ingredients`
  * Numerates this list and prints to the user for selection
  * Stores selected ingredient into a variable to use in a WHERE statement

  #### Step 5: Define `update_recipe` function
  * Prints a list of the recipes to user that includes recipes ID
  * Prompts user to enter ID of recipe they want to modify
  * Then gives them a list of what column/fields they can update
    * Prompts user to input what field they would like to modify
    * Then asks for new value

  #### Step 6: Define `delete_recipe` function
  * Prints a list of the recipes to user that includes recipes ID
  * Prompts user to enter ID of recipe they want to delete
  * Checks if ID exists and then uses DELETE query on table to delete recipe row

  </details>

  <details>

  <summary>Script Execution</summary>

  ![Screenshot of Recipe Creation](/Exercise%201.6/create%20recipe_1.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/create%20recipe_2.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/create%20recipe_3.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/search%20ingredients.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/update%20recipe_1.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/update%20recipe_2.png)

  ![Screenshot of Recipe Creation](/Exercise%201.6/delete%20recipe%20+%20exit.png)

  </details>

### Exercise 7 | Object Relational Mapping in Python

- Create final recipe app
- Utilize SQLAlchemy's ORM tool to create Recipe table

  <details>
  
  <summary>Step-by-Step</summary>
  
  #### Step 1: Set up Script + SQLAlchemy
  * Create `recipe_app.py` script
  * Import model definitions, `sessionmaker`, `declarative_base`
  * Create `engine` object to connect to database
  * Create `session` object to make changes to database
  
  #### Step 2: Create Model and Table
  * Store declarative base class in `Base` variable
  * `Recipe` class inherits `Base` class
    * Defines table name attribute as `final_recipes`
    * Defines the following columns:
      * `id` - Integer, primary key, auto-increments
      * `name` - String(50)
      * `ingredients` - String(255), stored ingredients as a string
      * `cooking_time` - Integer
      * `difficulty` - String(20)
    * Defines `__repr__` and `__str__` methods
  * Define `calculate_difficulty` function
  * Define function that retrieves the ingredients as a list

  #### Step 3: Define Main Operations
  * Define `create_recipe()`
    * Collects recipe name, ingredients, and cooking_time from user
    * Uses methods such as `isalpha()` to ensure appropriate inputs
    * Asks user how many ingredients to enter
      * Uses `for` loop to enter each ingredient
      * Converts ingredients into a string
    * Adds this recipe to Recipe table
  
  * Define `view_all_recipes()`
    * Retrieves all recipes from database
    * Informs user if no recipes were found
    * Prints each recipe using defined `__str__` method
  
  * Define `search_by_ingredients()`
    * Retrieves values from `ingredients` column of table
    * Adds each unique ingredient to list
    * Prints the result as a numbered list to the user
    * User is prompted to pick which ingredient(s) to search
    * List is created based on user input for search conditions
    * Recipes are filtered using this `conditions` list
  
  * Define `edit_recipe()`
    * Prints list of each recipes id and name
    * Prompts user to choose a recipe to edit
    * User is given option menu for what they would like to edit
    * Recipe is updated with new value and difficulty is recalculated

  * Define `delete_recipe()`
    * Prints list of each recipes id and name
    * Prompts user to choose which recipe to delete
    * Asks if user is sure and requires a `Y/N` input
    * If `Y`, recipe is deleted
    * If `N`, recipe is kept and user is taken back to main menu

  #### Step 4: Design Main Menu
  * Main menu exists in `while` loop that gives the user 6 options:
    * Create a Recipe
    * View all Recipes
    * Search for ingredients
    * Edit a Recipe
    * Delete a Recipe
    * Exit
  * Uses `if-elif` statements to check users input and call the associated function
  * If user chooses to exit, application is stopped and session is closed / engine is disposed

  </details>

  <details>

  <summary>Script Execution</summary>

  ![Screenshot of Main Menu](/Exercise%201.7/main_menu.png)

  ![Screenshot of Recipe Creation](/Exercise%201.7/recipe_creation.png)

  ![Screenshot of All Recipes](/Exercise%201.7/view_all_recipes.png)

  ![Screenshot of Recipe Update 1](/Exercise%201.7/update_recipe_1.png)

  ![Screenshot of Recipe Update 2](/Exercise%201.7/update_recipe_2.png)

  ![Screenshot of Ingredient Search 1](/Exercise%201.7/ingredient_search_1.png)

  ![Screenshot of Ingredient Search 2](/Exercise%201.7/ingredient_search_2.png)

  ![Screenshot of Ingredient Search 3](/Exercise%201.7/ingredient_search_3.png)

  ![Screenshot of Recipe Deletion](/Exercise%201.7/delete_recipe.png)

  </details>