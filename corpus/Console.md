---
title: Console | VEX AIM - Python API
description: Explore the Python API reference for the console on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to output and input information on the Console.
---

```{highlight} python
:linenothreshold: 5
```

# Console

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

<!-- In Progress
<div class="inProgressCallout bg-warning">
    <h3 class="text-black"><svg class="inline me-2 mb-1 text-lg text-black" width="2em" height="2em" viewBox="0 0 72 72"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_40_48064)">
                <path
                    d="M24 27C24 25.3431 25.3431 24 27 24H45C46.6569 24 48 25.3431 48 27C48 28.6569 46.6569 30 45 30H27C25.3431 30 24 28.6569 24 27Z"
                    fill="currentColor"></path>
                <path
                    d="M24 39C24 37.3431 25.3431 36 27 36H39C40.6569 36 42 37.3431 42 39C42 40.6569 40.6569 42 39 42H27C25.3431 42 24 40.6569 24 39Z"
                    fill="currentColor"></path>
                <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M12 18C12 13.0294 16.0294 9 21 9H51C55.9706 9 60 13.0294 60 18V54C60 58.9706 55.9706 63 51 63H21C16.0294 63 12 58.9706 12 54V18ZM21 15H51C52.6569 15 54 16.3431 54 18V54C54 55.6569 52.6569 57 51 57H21C19.3431 57 18 55.6569 18 54V18C18 16.3431 19.3431 15 21 15Z"
                    fill="currentColor"></path>
            </g>
            <defs>
                <clipPath id="clip0_40_48064">
                    <rect width="72" height="72" fill="white"></rect>
                </clipPath>
            </defs>
        </svg>In Progress</h3>
</div> -->

## Introduction

The VEXcode AIM Console is displayed in the Monitor window within VEXcode. It allows you to display text, receive input, and format printed data in real time. Below is a list of the available methods for interacting with the console:

**Actions – Output text or clear the console.**  
- [print](#print) – Outputs text to the Console.  
- [clear_console](#clear_console) – Clears all text from the Console.  

**Getter – Read user input.**  
- [input](#input) – Returns the most recent user input as a string.  

**Mutator – Format printed text.**  
- [set_console_text_color](#set_console_text_color) – Sets the color for all subsequent console text.  


## Actions

### print

```{vexcode}
id: aim_looks_console_print
```
```{vexcode}
id: aim_looks_console_print_end
```

`print` outputs the specified text to the Console and moves the cursor to the next line by default.

**Usage:**<br>
`print(string, end)`

| Parameter      | Description |
|--------------|-------------|
| `string` | The text that will be printed as a string. |
| `end` | Optional. The string added to the end of the printed text. Specified as `end=`. Default: `end="\n"`, which is automatically hidden and moves the cursor to the next line. |

```python
# Display two messages consecutively
print("I'm printed on one line.")
print("I'm printed automatically on the next line!")
```

<!-- ![Displays the two messages being displayed consecutively in the Print Console.](/_static/img/Print_console/print_console_1.png) -->

```python
# Print three colors on one line in the Print Console
colors = ["Red", "Green", "Blue"]

for color in colors:
    print(color, end=", ")
```

<!-- ![Displays three colors being printed one after the other on one line.](/_static/img/Print_console/print_console_2.png) -->

### clear_console

```{vexcode}
id: aim_looks_console_clear_console
```

`clear_console` clears all text from the Console.

**Usage:**<br>
`clear_console()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display text then clear it after two seconds
print("I will be cleared!")
wait(2, SECONDS)
clear_console()
```

## Getter

### input

```{vexcode}
id: aim_console_input
```

`input` returns the most recent user input from the Console as a string.

**Usage:**<br>
`input()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Message the robot a name for the robot to greet
print("What is your name?")
answer = input()
print("Hi, " + answer + "! My name is AIM.")
```

<!-- ![Displays a greeting as the robot greets VEX, as VEX was the name used in the input.](/_static/img/Print_console/input.png) -->

## Mutator

### set_console_text_color

```{vexcode}
id: aim_looks_set_console_text_color
```

`set_console_text_color` sets the color for all subsequent console text.

**Usage:**<br>
`set_console_text_color(color)`

| Parameter      | Description |
|--------------|-------------|
| `color` | The color to set:<br>`BLACK`, `BLUE`, `CYAN`, `GREEN`, `ORANGE`, `PURPLE`, `RED`, `TRANSPARENT`, `WHITE`, or `YELLOW`. |

```python
# Display a green message on the Console
set_console_text_color(GREEN)
print("I am green!")
```

<!-- ![Displays a message with green text.](/_static/img/Print_console/set_console_text_color.png) -->