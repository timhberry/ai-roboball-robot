---
title: Custom String Formatting | VEX AIM - Python API
description: Explore the Python API reference for custom string formatting on a VEX AIM Coding Robot. Find detailed descriptions for formatting text and displaying it on the screen.
---


```{highlight} python
:linenothreshold: 5
```

# String Formatting

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

f-strings are the recommended way to format text and numbers in Python. They allow variables, expressions, and function calls to be embedded directly inside `{}`.

To create an f-string, add `f` before the string, and place any variable, expression, or function call inside `{}`.

```python
x = 1
y = 5

# Display the variables using an f-string
robot.screen.print(f"Position: ({x}, {y})")
```

```python
# Display a calculation with an f-string
robot.screen.print(f"Sum: {5 + 3}")
```

```python
# Display the robot's battery capacity with an f-string
robot.screen.print(f"Battery: {robot.get_battery_level()}%")
```

**f-Strings – Embed variables and expressions directly in text.**  
- [f"{value}"](#introduction) – Displays variables, expressions, or function calls inside a string.  

**Formatting Numbers in f-strings – Control how numeric values appear.**  
- [:.xf](#fixed-decimal-places) – Sets the number of decimal places to show.  
- [round](#rounding-numbers) – Rounds a number to a given number of decimal places.  
- [:,](#thousands-separator) – Adds commas as thousands separators.  
- [:.x%](#percentage) – Converts a decimal to a percentage with x decimal places.  
- [:#x](#hexadecimal) – Formats a number as hexadecimal.  
- [:b](#binary) – Formats a number as binary.

**String Combination – Combine text and values.**  
- [f"{value}"](#using-f-strings) – Combine strings and variables in a single expression.  
- [+ operator](#-operator) – Concatenate strings manually with optional type conversion.

**String Methods – Change the case of text.**  
- [upper()](#upper) – Converts all characters to uppercase.  
- [lower()](#lower) – Converts all characters to lowercase.

**Substring Checks – Test for presence or position of text.**  
- [in](#in) – Checks if a word exists in a string.  
- [startswith()](#startswith) – Checks if a string begins with a given value.  
- [endswith()](#endswith) – Checks if a string ends with a given value.

**Escape Sequences – Format output with special characters.**  
- [\n](#new-line) – Adds a line break (new line).  
- [\t](#tab-spacing) – Adds a tab space between items.

## Formatting Numbers in f-strings

f-strings allow precise control over decimal places, rounding, thousands separators, and more by using the following format specifiers:

### Fixed Decimal Places

`.xf` controls how many decimal places a number is displayed with.

**Usage:**<br>
`.xf`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `x` | The amount of decimal places to show. |

```python
# Display pi with 2 decimal places
pi = 3.1415926535
robot.screen.print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14
```

### Rounding Numbers

`round` rounds numbers outside of an f-string or inside of the `{}`.

**Usage:**<br>
`round(number, x)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `number` | The number to round. |
| `x` | The amount of decimal places to round to. |

```python
# Display a value rounded to only 2 decimal places
value = 5.6789
robot.screen.print(f"{round(value, 2)}")  # Output: 5.68
```

### Thousands Separator

`,` inserts commas as thousands separators to make large numbers more readable.

**Usage:**<br>
`,`

| Parameters | Description |
|:-|--|
|  | This format specifier has no parameters. |

```python
# Display a large number separated with commas
number = 1234567
robot.screen.print(f"{number:,}")  # Output: 1,234,567
```

### Percentage

`.x%` formats decimal values as percentages.

**Usage:**<br>
`.x%`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `x` | The amount of decimal places to show. |

```python
# Display a converted decimal to a percentage
value = 0.875
robot.screen.print(f"{value:.1%}")  # Output: 87.5%
```

### Hexadecimal

`.#x` converts numbers to hexadecimal.

**Usage:**<br>
`.#x`

| Parameters | Description |
|:-|--|
|  | This format specifier has no parameters. |

```python
# Convert 255 to hexadecimal
number = 255
robot.screen.print(f"{number:#x}")  # Output: 0xff
```

### Binary

`b` converts numbers to binary (base 2).

**Usage:**<br>
`b`

| Parameters | Description |
|:-|--|
|  | This format specifier has no parameters. |

```python
# Convert 3 to binary
robot.screen.print(f"Binary: {3:b}")  # Output: 11
```

## Combining Strings

You can combine (or concatenate) strings using two approaches:

### Using f-strings

With f-strings, you can embed variables directly inside `{}`.

```python
# Display an answer based on the given emotion
emotion = "good"
robot.screen.print(f"I'm {emotion}, you?")
```

### + Operator

You can combine strings manually using the `+` operator. 

**Note:** Non-strings must first be converted to strings using `str()`.

```python
# Display the x and y values
x = 10
y = 20
robot.screen.print("X: " + str(x) + ", Y: " + str(y))
```

## String Methods

Python provides built-in methods for modifying and checking strings.

### upper

`upper` converts all letters in a string to uppercase.

**Usage:**<br>
`upper()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
message = "vexcode"
robot.screen.print(message.upper())  # Output: VEXCODE
```

### lower

`lower` converts all letters in a string to lowercase.

**Usage:**<br>
`lower()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
message = "VEXCODE"
robot.screen.print(message.lower())  # Output: vexcode
```

## Checking for Substrings

### in

`in` is a keyword that returns a Boolean indicating whether a word exists in a string.
- `True` - The word exists in the string.
- `False` - The word does not exist in the string.

```python
message = "Hey everyone!"
if "Hey" in message:
    robot.screen.print("Hello!")
```

### startswith

`startswith` returns a Boolean indicating whether a string begins with a given value.
- `True` - The word starts the string.
- `False` - The word does not start the string.

**Usage:**<br>
`startswith(substring)`

| Parameters | Description |
|:-|--|
| `substring` | The substring to check inside the string. |

```python
message = "AIM Robot"

if message.startswith("AIM"):
    robot.screen.print("AIM first!")
```

### endswith

`endswith` returns a Boolean indicating whether a string ends with a given value.
- `True` - The word ends the string.
- `False` - The word does not end the string.

**Usage:**<br>
`startswith(substring)`

| Parameters | Description |
|:-|--|
| `substring` | The substring to check inside the string. |

```python
message = "AIM Robot"

if message.endswith("Robot"):
    robot.screen.print("Robot last!")
```

## Escape Sequences

Escape sequences are special characters used inside strings to format text output. They are **only available** for use with the Console.

### New Line 

`\n` moves text to a new line when printing.

```python
# Display text on two lines
print("First line\nSecond line")
```

### Tab Spacing

`\t` inserts a tab space between words or numbers,

```python
# Display the quantity of barrels
quantity = 2
print("Barrels:\t", quantity)
```