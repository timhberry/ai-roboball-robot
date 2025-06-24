---
title: Variables | VEX AIM - Python API
description: Explore the Python API reference for variables on a VEX AIM Coding Robot. Find detailed descriptions for variables, usage, and examples.
---


```{highlight} python
:linenothreshold: 5
```

# Variables

```{contents}
:local: true
```

## Introduction

Variables store data and allow you to reuse and manipulate it throughout your program. Python is a *dynamically typed* language, meaning you don’t need to declare the type of a variable explicitly. Instead, the type is automatically inferred based on the value assigned to it. For example:

```python
angle = 90           # angle is an integer
dist = "Distance: "  # dist is a string
steps = 2.5          # steps is a float
```

Python is also *strongly typed*, which means you cannot perform operations on incompatible types without explicitly converting them. For example:

```python
sports_balls = 2                 # balls is an integer
barrels = "4"                    # barrels is a string
result = barrels + sports_balls  # Creates a TypeError
```

To resolve such issues, you must explicitly convert the types, if appropriate:

```python
sports_balls = 2   # sports_balls is an integer
barrels = "4"      # barrels is a string

# Convert barrels to an integer before adding
result = int(barrels) + sports_balls  
```

This API explains common variable types in Python. While not an exhaustive list, it covers the types you’re most likely to use in practice.

- [**Local variables**](#local-variables) – Declared inside a function and only used within that scope; best for temporary or isolated values.  
- [**Global variables**](#global-variables) – Declared outside any function and used throughout the project; good for sharing data between functions.  

- [**Integer**](#integer) – Whole numbers used for counting, distances, or anything without decimals.  
- [**Float**](#float) – Numbers with decimal points, useful for precise measurements or calculations.  
- [**String**](#string) – Text values, used for messages, labels, or displaying readable output.  
- [**Boolean**](#boolean) – `True` or `False` values for logic and decision-making.  
- [**NoneType**](#nonetype) – Represents “no value yet,” often used as a placeholder.  
- [**Range**](#range) – Automatically generates sequences of numbers, most commonly used in loops.  
- [**List**](#list) – A changeable collection of items; good for storing groups of values like objects or sensor readings.  
- [**2D List**](#2d-list) – A list of lists; ideal for representing rows, grids, or table-like data.  
- [**Tuple**](#tuple) – A fixed sequence of values that can’t be changed; useful for grouped, unchanging data.  


## Declaring and Assigning a Variable

To create a variable, simply assign a value to a name using the `=` operator:

```python
distance = 100
```

When naming a variable, the following rules must be adhered to:

+ The name cannot contain special characters (e.g., an exclamation point).
+ The name cannot begin with a number.
+ The name cannot use spaces.
+ The name cannot be a reserved word in VEXcode (e.g. Drivetrain).

### Local Variables

**Local variables** are defined *inside* a function or block of code. They are only accessible within the scope of that function or block and are not visible outside of it.

```python
def show_local():
    # This variable only exists inside this function
    message = "I'm local!" 
    robot.screen.print(message)

show_local()
```

Local variables are commonly used to store temporary values that are only relevant within a specific function or part of the program.

### Global Variables

**Global variables** are defined *outside* of any function or block. They can be accessed and read *anywhere* in the program, including inside functions.

**Note:** **Global variables** are accessible from anywhere in the program, which can make them convenient for sharing data across functions. However, relying heavily on **global variables** can lead to unintended side effects, as changes to the variable in one part of the program may affect other parts unpredictably. For this reason, **local variables** are generally preferred when possible, as they limit a variable’s scope to the specific function where it is defined. This reduces the likelihood of conflicts and makes debugging easier.

```python
# The variable is defined outside a function
message = "I'm global!"  

def show_global():
    # You can access 'message' inside a function
    robot.screen.print(message)
    robot.screen.next_row()

show_global()
# And you can access 'message' outside a function
robot.screen.print(message)
```

By default, assigning a value to a variable inside a function creates a local variable. To **modify** a global variable inside a function, you must explicitly declare it using the `global` keyword.

```python
# Define the global variable
count = 0 

def increase_count():
    # Use the global keyword to let you modify the
    # global variable
    global count
    count = count + 1
    robot.screen.print(f"Count: {count}")
    robot.screen.next_row()

increase_count()
increase_count()
```

## Types of Data

Python variables can store various types of data, each suited for different use cases. Below are the most commonly used types:

### Integer

```{vexcode}
id: aim_variables_my_number
```

An **integer** is a whole number.

```python
distance = 50

# Move the robot forward for the variable value in mm
robot.move_for(distance, 0)

# Add to the variable and move forward the new value, for 100mm total
distance = distance + 50
robot.move_for(distance, 0)
```
### Float

A **float** is a decimal-point number.

```python
# Store a value with decimal points
raw_value = 0.88

# Print the decimal value as a percentage
robot.screen.print(raw_value * 100, "%")
```

### String

```{vexcode}
id: aim_variables_my_string
```

A **string** is a sequence of characters, commonly used for text.

```python
# Set the variable to a string then print the string
message = "Ready!"
robot.screen.print(message)
```

**Note:** A string must always be enclosed within matching quotation marks, either single (`'`) or double (`"`). You can use either style, but the opening and closing marks must match.

### Boolean

```{vexcode}
id: aim_variables_my_boolean
```

A **Boolean** represents `True` or `False` values.

```python
# Set the state of the variable
delivered = False

# Print different messages depending on the Boolean.
if delivered:
    robot.screen.print("Package delivered!")
else: 
    robot.screen.print("Delivering...")
```

Booleans can be changed at any point in the project. 

```python
# Print the value of the delivered variable
delivered = True
robot.screen.print(delivered)
wait(2,SECONDS)

# Clear the screen and print the value of the variable again
robot.screen.clear_screen(Color.BLACK)
delivered = False
robot.screen.print(delivered)

```

### NoneType

**NoneType** represents the absence of a value in Python.

```python
# Write what the robot's task should be as a string
current_task = None

# Check if a task is assigned
if current_task is None:
    robot.screen.print("No task!")
else:
    robot.screen.print(f"Task: {current_task}")
```

### Range

A **range** is a sequences of numbers, commonly used in loops to generate numeric sequences. It follows the format:
```python
range(start, stop, step)
```
* The `start` value is inclusive (the sequence begins here). This defaults to 0.
* The `stop` value is exclusive (the sequence stops before this number).
* The `step` determines how much each number increases (or decreases). This defaults to 1.


```python
# Drive and turn 4 times to move in a square
for index in range(4):
    robot.move_for(50, 0)
    robot.turn_for(RIGHT, 90)
```

```python
# Count by 2 starting at 1 and ending before 12
for index in range(1, 12, 2): 
    # Print the values on the screen with each loop
    robot.screen.print(index)
    robot.screen.next_row()
```

### List

```{vexcode}
id: aim_variables_my_list
```

<!-- Ask Tim about making this 1D List -->

A **list** is a versatile structure that stores multiple values in a single variable. Its contents can be modified, accessed, or iterated over easily.

```python
# Define a list of colors
colors = ["Red", "Green", "Blue", "Purple"]

# Repeat for the number of items in the colors list
for index in colors:
    # Print each color in order
    robot.screen.print(index)
    robot.screen.next_row()

```
Lists can be added to using `append`.

```python
# Define a list of colors
colors = ["Red", "Green", "Blue", "Purple"]

# Append a new color to the list
colors.append("Yellow")

# Repeat for the number of items in the colors list
for index in colors:
    # Print each color in order
    robot.screen.print(index)
    robot.screen.next_row()
```

### 2D List

```{vexcode}
id: aim_variables_my_2d_list
```

A **2D list**, or list of lists, is commonly used to represent grids, tables, or matrices. Each sublist represents a row or a specific grouping of data.

```python
# Assign the values in the matrix 2D list
matrix = [
    ["A", 1, "Red"],
    ["B", 2, "Orange"],
    ["C", 3, "Yellow"]
]
# Loop through each row
for row in matrix: 
    # Loop through each column in the row 
    for element in row: 
        robot.screen.print(element, ", ")
    robot.screen.next_row()
```

You can modify specific elements or even entire sublists within a 2D list:

```python
# Assign the values in the matrix 2D list
matrix = [
    ["A", 1, "Red"],
    ["B", 2, "Orange"],
    ["C", 3, "Yellow"]
]
# Modify the color (in column 2) in row 0
matrix[0][2] = "Blue"

# Print the modified row from the matrix 2D list 
robot.screen.print(matrix[0])
```

### Tuple

A **tuple** is a sequences of items that cannot be changed after they are created. They are often used to group related values together.

```python
# Define a tuple
set_1 = (100, "Left")

# Print the tuple
robot.screen.print(set_1)
```
Tuples are created using parentheses`()` rather than square brackets `[]`.