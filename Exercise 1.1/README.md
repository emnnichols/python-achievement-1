# Introduction to Python
## Table of Contents
[Exercise 1](/Exercise%201.1#exercise-1-1)

## Exercise 1 | Getting Started with Python

### Step 1: Install Python
* Install Python on your system or check that Python is already installed
* Verify the correct version is installed with `python --version`
<details>
  <summary>Screenshot</summary>
  
![Screenshot of checking Python version](/Exercise%201.1/Step%201_Install%20Python.png)

</details>

### Step 2: Set up new virtual environment
* Use `mkvirtualenv` to make a new virtual environment called cf-python-base
<details>
  <summary>Screenshot</summary>
  
![Screenshot of making new virtual environment](/Exercise%201.1/Step%202_New%20Virt%20Env.png)
</details>

### Step 3: Create 'add.py' script
* Create a script that adds two numbers that the user inputs
* Store user input into a variable using `variable = int(input("Prompt"))`
* Store product of the two numbers into a separate variable
<details>
  <summary>Screenshot</summary>
  
![Screenshot of creating the script that adds two numbers together](/Exercise%201.1/Step%203_VS%20Code.png)
</details>

### Step 4: Install IPython
* Using  `pip install`, install ipython
* Verify installation by launching an IPython shell with `ipython`
<details>
  <summary>Screenshot</summary>
  
![Screenshot of installing ipython](/Exercise%201.1/Step%204_Install%20IPython.png)
</details>

### Step 5: Install Export Requirements file
* Use `pip install` command to generate a requirements.txt file from the environment created
* Create a new virtual environment
* Use `pip install -r` to install from the requirements.txt
<details>
  <summary>Screenshots</summary>
  
![Screenshot of generating requirements.txt file](/Exercise%201.1/Step%205a_Requirements%20file.png)
  
![Screenshot of creating new virual environment](/Exercise%201.1/Step%205b_Copy%20env.png)

![Screenshot of using the requirements.txt file with pip install](/Exercise%201.1/Step%205c_%20Pip%20install%20requirements.png)
</details>
