---
title: Functions | VEX AIM - Python API
description: Explore the Python API reference for using functions on a VEX AIM Coding Robot. Find detailed explanations and examples for defining and calling functions.
---

```{highlight} python
:linenothreshold: 5
```

# Functions

```{vexcode}
id: aim_function_name
```

```{contents}
:local: true
```

<!-- Complete
<div class="completeCallout bg-success">
    <h3 class="text-white"><svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
            fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
            class="text-white">
            <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        Complete</h3>
</div> -->

## Introduction

Functions are a fundamental component of Python programming, packaging code snippets in to reusable, efficient sections of code designed to perform a specific task. Functions can be called multiple times within a program, making code organization easier, and helping to avoid repeated code. Functions also make code easier to debug.

- `def` defines a function. 
- `return` sends the function's output back to the main program.

**Usage:**

```python
def function_name(parameters):
    # Code to execute when the function is called
    return result  # Optional, used to return a value
```

| Parameters  | Description     |
|:---------: | :---------------------------|
| `function_name` | A name you give to your function. |
| `parameters` | Optional. Variables that accept input values when the function is called, allowing data to be passed into the function.|
| `result` | Optional. Let the function send a result back to the caller. If a function does not include a return statement, it will return [`None`](Variables.md#nonetype) by default.

**Note:** A function must **always be defined *before*** it is called.

## Defining and Calling Functions

### Functions with No Parameters

If a function does not require input, you can define it without parameters.

```python
# Define a function to display a message
def greeting():
    robot.screen.print("Hello!")

# Call the function to display the message
greeting()
```

### Functions with Parameters

You can also add parameters to functions, which let you pass in information the function needs to work.

```python
# Define a function with a parameter
def named_greeting(name):
    robot.screen.print("Hello, " + name + "!")
named_greeting("Stranger")
```

### Functions with Default Arguments

A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

```python
# Define a function with a parameter and a default argument
def named_greeting(name = "Stranger"):
    robot.screen.print("Hello, " + name + "!")

# Use the default argument
named_greeting()
robot.screen.next_row()
# Change the parameter to a different name
named_greeting("AIM")
```

### Return Values from Functions

Functions can send data back to the caller using the `return` keyword. This allows you to capture and use the output in your program.

```python
# Define a function that multiplies numbers by 2
def times_two(number):
    return number * 2

# Display the return value
robot.screen.print(times_two(2))
```