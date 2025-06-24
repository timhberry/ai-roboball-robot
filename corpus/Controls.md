---
title: Controls | VEX AIM - Python API
description: Explore the Python API reference for controls on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples.
---

```{highlight} python
:linenothreshold: 5
```

# Control

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

Control includes methods for timing, program flow, conditional logic, and project termination. These controls let you pause execution, create loops, define logic paths, and end a program. Below is a list of available controls, including methods and core Python keywords:

- [wait](#wait) – Pauses execution for a given number of milliseconds or seconds.  
- [for](#for) – Repeats code for each item in a sequence.  
- [if](#if) – Executes code if a condition is true.  
- [if/else](#ifelse) – Runs different code depending on a condition.  
- [if/elif/else](#ifelifelse) – Checks multiple conditions in order.  
- [while](#while) – Repeats code while a condition is true.  
- [break](#break) – Exits a loop immediately.  
- [stop_program](#stop-program) – Ends the running program.  
- [pass](#pass) – Placeholder used when no action is needed.  



### Wait

```{vexcode}
id: aim_control_wait
```

`wait` pauses for a specific amount of time before moving to the next method.

**Usage:**<br>`wait(time, units)`

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `time` | The amount of time to wait, as a positive integer. |
| `units` | Milliseconds `MSEC` (default) or `SECONDS`. |

```python
# Move right for one second, then stop
robot.move_at(90)
wait(1, SECONDS)
robot.stop_all_movement()
```

### For

```{vexcode}
id: aim_control_for_loop
```

`for` iterates over a sequence (such as a list, tuple, dictionary, set, or string) or any iterable object. It executes the block of code once for each item in the sequence.

**Usage:**<br>
```python 
for value in expression_list:
    pass
```

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `value` | A temporary variable that stores the current element in the iteration. |
| `expression_list` | The collection of elements being looped through (e.g., list, string, range). |

```python
# Move in a square path.
for index in range(4):
    robot.move_for(50, 0)
    robot.turn_for(RIGHT, 90)
```

```python
# Print each item in the list
colors = ["Red", "Green", "Blue"]

for color in colors:
    robot.screen.print(color)
    robot.screen.next_row()
```

![Displays three objects being printed on the screen.](/_static/img/Controls/for.png)

### If

```{vexcode}
id: aim_control_if_statement
```

`if` executes the indented block of code if the condition evaluates as `True`.

**Usage:**
```python
if condition:
    pass
```

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `condition` | An expression or variable that is evaluated when the statement runs. If it evaluates as `True`, the code inside the `if` block executes; if it evaluates as `False`, the block is skipped. |

```python
# Kick when the screen is pressed
while True:
    if robot.screen.pressing():
        robot.kicker.kick(MEDIUM)
    wait(0.1, SECONDS)
```

### If/Else

```{vexcode}
id: aim_control_if_else_statement
```

`if` and `else` determine which indented block of code runs based on whether the condition evaluates as `True` or `False`.

**Usage:**
```python
if condition:
    pass
else:
    pass
```

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `condition` | An expression or variable that is evaluated when the statement runs. If it evaluates as `True`, the code inside the `if` block executes; if it evaluates as `False`, the code inside the `else` block executes instead. |


```python
# Show one emoji when the screen is pressed,
# and a different emoji when not pressed
while True:
    if robot.screen.pressing():
        robot.screen.show_emoji(EXCITED)

    else:
        robot.screen.show_emoji(BORED)
    
    wait(0.1, SECONDS)
```

### If/Elif/Else

```{vexcode}
id: aim_control_elseif_statement
```

The `if/elif/else` structure selects which indented block of code runs based on conditions:

- `if` runs its block if the condition evaluates as `True`.
- `elif` checks additional conditions only if all previous conditions evaluated as `False`. Multiple `elif` statements can be used.
- `else` runs its block only if none of the previous conditions evaluated as `True`.

**Usage:**
```python
if condition:
    pass
elif condition:
    pass
else:
    pass
```

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `condition` |  An expression or variable that is evaluated when the statement runs. The first condition that evaluates as `True` determines which block executes; if none are `True`, the `else` block runs. |


```python
# Move the robot forward or reverse
# based on the position of the joystick
def when_axis_changed():
    position = controller.axis1.position()
    if position > 0:
        robot.move_at(0)
    elif position < 0:
        robot.move_at(180)
    else:
        robot.stop_all_movement()

controller.axis1.changed(when_axis_changed)
```

### While

```{vexcode}
id: aim_control_while_loop
```

`while` repeatedly runs methods as long as the condition is `True`. It can also be used like a "Wait until" by adding `not` to the condition, as shown in the example below.

**Usage:**
```python
while condition:
    pass
```

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| `condition` | An expression or variable that is evaluated before each iteration. If it evaluates as `True`, the loop continues; if it evaluates as `False`, the loop stops. |

```python
# Keep the LEDs green while the robot is moving
robot.move_for(200, 0, wait=False)
while robot.is_move_active():
    robot.led.on(ALL_LEDS, GREEN)
    wait(50, MSEC)

robot.led.on(ALL_LEDS, BLACK)
```

```python
while True:
    # Continually flash all LEDs red then green.
    robot.led.on(ALL_LEDS, RED)
    wait(0.5, SECONDS)
    robot.led.on(ALL_LEDS, GREEN)
    wait(0.5, SECONDS)
```

```python
# Wait until the screen is pressed before
# turning off the LEDs
while not robot.screen.pressing():
    robot.led.on(ALL_LEDS, RED)
    wait(50, MSEC)

robot.led.on(ALL_LEDS, BLACK)
```

### Break

```{vexcode}
id: aim_control_break
```

`break` exits a loop immediately.

```python
# Flash LEDs until the screen is pressed
while True:
    robot.led.on(ALL_LEDS, RED)
    wait(0.5, SECONDS)
    robot.led.on(ALL_LEDS, GREEN)
    wait(0.5, SECONDS)

    if robot.screen.pressing():
        break

# Turn the LEDs Off
robot.led.off(ALL_LEDS)
```

### Stop Program

```{vexcode}
id: aim_control_robot_stop_program
```

`stop_program` ends a running project.

**Usage:**<br>`robot.stop_program()`

| Parameters | Description                                                  |
|------------|--------------------------------------------------------------|
| | This method has no parameters. |

```python
# Stop the project once the screen is pressed
while True:
    robot.led.on(ALL_LEDS, RED)
    wait(0.5, SECONDS)
    robot.led.on(ALL_LEDS, GREEN)
    wait(0.5, SECONDS)
    if robot.screen.pressing():
        robot.stop_program()
```

### Pass

```{vexcode}
id: aim_control_pass
```

`pass` is a placeholder for future code and can be used to avoid errors in empty loops, conditionals, and functions.

```python
if condition:
    pass
```
```python
def function():
    pass
```