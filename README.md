# Recipe app (CLI version)

## Context

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

### Exercise 1 | Getting Started with Python

Preparing your developer environment for programming with Python

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

Create data structure for the Recipe app

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