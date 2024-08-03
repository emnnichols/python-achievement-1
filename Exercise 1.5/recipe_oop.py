# Defining Recipe class

class Recipe:
  # Class variable to store each unique ingredient
  all_ingredients = []

  # Intialization method that takes the name and cook time of the recipe
  def __init__(self, name):
    self.name = name
    self.cooking_time = None
    self.ingredients = set()
    self.difficulty = None

  # Getter method for recipe name
  def get_name(self):
    output = "Recipe Name: " + self.name
    return output

  # Setter method for recipe name
  def set_name(self, name):
    self.name = name

  # Getter method for recipe cook time
  def get_cooking_time(self):
    output = "Cooking time (mins): " + self.cooking_time
    return output

  # Setter method for recipe cook time
  def set_cooking_time(self, time):
    self.cooking_time = time

  # Add ingredients to recipe ingredient list
  def add_ingredients(self, *ingredients):
    for i in ingredients:
      self.ingredients.add(i.title())
    self.update_all_ingredients()

  # Add new ingredients to all_ingredients set
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if ingredient not in Recipe.all_ingredients:
        Recipe.all_ingredients.append(ingredient)
        Recipe.all_ingredients.sort()

  # Getter method for recipe ingredients
  def get_ingredients(self):
    for ingredient in self.ingredients.sort():
      print("- " + ingredient)

  # Method for calculating and updating recipe difficulty level
  def calculate_difficulty(self, time, ingredients):
    if time < 10 and ingredients < 4:
      self.difficulty = 'Easy'
    elif time < 10 and ingredients >= 4:
      self.difficulty = 'Medium'
    elif time >= 10 and ingredients < 4:
      self.difficulty = 'Intermediate'
    elif time >= 10 and ingredients >= 4:
      self.difficulty = 'Hard'
    return self.difficulty
  
  # Getter method for recipe difficulty
  def get_difficulty(self):
    if self.difficulty is None:
      self.calculate_difficulty(self.cooking_time, len(self.ingredients))
    output = "Difficulty: " + self.difficulty
    return output
  
  # Search recipe for specific ingredient
  def search_ingredient(self, ingredient):
    if ingredient in self.ingredients:
      return True
    else:
      return False

  # String representation that prints entire recipe
  def __str__(self):
    self.calculate_difficulty(self.cooking_time, len(self.ingredients))

    output = f"\n{self.name.title()} \
      \n{20*'-'} \
      \n Cooking Time: {self.cooking_time} minutes \
      \n Difficulty: {self.difficulty} \
      \n Ingredients: \n"
    for ingredient in self.ingredients: 
      output += " - " + ingredient + "\n"
    return output
    
  # Search recipe objects for specfic ingredient
  def recipe_search(data, search_term):
    ingredient = search_term.title()
    print(f"{30*'-'} \n RECIPES FOUND WITH '{search_term.upper()}' \n{30*'-'}")
    for recipe in data:
      if Recipe.search_ingredient(recipe, ingredient):
        print(recipe)

# Main Code
recipes_list = []

tea = Recipe("Tea")
tea.add_ingredients("Tea leaves", "Sugar", "Water")
tea.set_cooking_time(5)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee powder", "sugar", "water")
coffee.set_cooking_time(5)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla essence", "Flour", "Baking powder", "Milk")
cake.set_cooking_time(50)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "milk", "Peanut butter", "Sugar", "ice cubes")
banana_smoothie.set_cooking_time(5)

recipes_list.extend([tea, coffee, cake, banana_smoothie])

print(f"{20*'-'} \n RECIPES LIST \n{20*'-'}")
for recipe in recipes_list:
  print(recipe)

Recipe.recipe_search(recipes_list, "milk")
Recipe.recipe_search(recipes_list, "sugar")
Recipe.recipe_search(recipes_list, "bananas")