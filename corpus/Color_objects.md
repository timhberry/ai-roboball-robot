---
title: Custom Colors | VEX AIM - Python API
description: Explore the Python API reference for custom colors on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and examples for creating and using custom colors in color-based functions.
---


```{highlight} python
:linenothreshold: 5
```

# Custom Colors

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

The VEX AIM Coding Robot supports the use of custom colors for drawing, display, and its LEDs. Custom colors can be created using RGB values, hex codes, HSV values, or predefined constants. Custom Colors includes methods for both creating and updating color objects. Below is a list of available methods:

**Constructors – Create a new `Color` object.**  
- [Color(value)](#creating-a-custom-color) – Accepts a predefined constant, hex string (e.g. `"#FFF700"`), or hex integer (e.g. `0xFFF700`).  
- [Color(r, g, b)](#rgb) – Creates a color using red, green, and blue values (0–255).  

**Mutators – Update an existing `Color` object.**  
- [rgb](#rgb) – Updates a color using new RGB values.  
- [hsv](#hsv) – Updates a color using hue (0–360), saturation, and brightness (0.0–1.0).  
- [web](#web) – Updates a color using a web hex color string (e.g. `"#32C8B6"`).  

## Creating a Custom Color

To use a custom color, you must first create a `Color` object using one of the following constructors:

### Hexadecimal Integer

Creates a color using a six-digit hexadecimal integer.

**Usage:**<br>
`Color(value)`

| Parameter | Description |
|:---------:|:------------|
| `value`   | A six-digit integer in hexadecimal format (e.g., `0xFFF700` for yellow). |


```python
# Construct a yellow Color "yellow" using a
# hexadecimal value
yellow = Color(0xFFF700)

robot.screen.set_pen_color(yellow)
robot.screen.print("My Yellow")
```

### RGB

Creates a color using separate red, green, and blue values.

**Usage:**<br>
`Color(r, g, b)`

| Parameter |	Description |
|:---------:|:------------|
| `r` |	An integer from 0 to 255 representing the red component. |
| `g` |	An integer from 0 to 255 representing the green component. |
| `b` |	An integer from 0 to 255 representing the blue component. |

```python
# Construct a yellow Color "yellow" using
# RGB values
yellow = Color(255, 247, 0)

robot.screen.set_pen_color(yellow)
robot.screen.print("My Yellow")
```

### Web Color

Creates a color using a web color string (hex code).

**Usage:**<br>
`Color(value)`

| Parameter | Description |
|:---------:|:------------|
| `value`   | A web color as a string (hex code) (e.g., `"#FFF700"`). |

```python
# Construct a yellow Color "yellow" using a
# web string
yellow = Color("#FFF700")

robot.screen.set_pen_color(yellow)
robot.screen.print("My Yellow")
```

### Predefined Color

Creates a color using a predefined `Color` constant.

**Usage:**<br>
`Color(value)`

| Parameter | Description |
|:---------:|:------------|
| `value`   | A built-in color constant:<br>`BLACK`, `BLUE`, `CYAN`, `GREEN`, `ORANGE`, `PURPLE`, `RED`, `TRANSPARENT`, `WHITE`, `YELLOW`. |

```python
# Construct a yellow Color "yellow" using a
# predefined Color constant
yellow = Color(YELLOW)

robot.screen.set_pen_color(yellow)
robot.screen.print("My Yellow")
```

## Mutators

These methods allow you to modify a `Color` object after it has been created during a project.

### rgb

`rgb` updates the color of an existing `Color` object using RGB values.

**Usage:**<br>
`rgb(r, g, b)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `r` | An integer from 0 to 255 representing the red component of the color. |
| `g` | An integer from 0 to 255 representing the green component of the color. |
| `b` | An integer from 0 to 255 representing the blue component of the color. |

```python 
# Create a custom teal color and set it as the pen color
robot_color = Color(50, 200, 180)
robot.screen.set_pen_color(robot_color)

# Draw a rectangle with the teal outline
robot.screen.draw_rectangle(30, 70, 80, 50)

# Draw another rectangle with a magenta outline
robot_color.rgb(170, 40, 150)
robot.screen.set_pen_color(robot_color)
robot.screen.draw_rectangle(130, 70, 80, 50)
```

### hsv

`hsv` updates the color of an existing `Color` object using HSV values.

**Note:** `hsv` can only be used to change a `Color` object that has already been created. It cannot be used to create a new `Color` Object.

**Usage:**<br>
`hsv(h, s, v)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `h` | An integer from 0 to 360 representing the hue of the color. |
| `s` | A float from 0.0 to 1.0 representing the saturation of the color. |
| `v` | A float from 0.0 to 1.0 representing the brightness of the color. |

```python 
# Create a custom teal color using RGB (HSV can't be used)
robot_color = Color(50, 200, 180)
robot.screen.set_pen_color(robot_color)

# Draw a rectangle with the teal outline
robot.screen.draw_rectangle(30, 70, 80, 50)

# Draw another rectangle with a magenta outline
robot_color.hsv(300, 0.75, 0.78)
robot.screen.set_pen_color(robot_color)
robot.screen.draw_rectangle(130, 70, 80, 50)
```

### web

`web` updates the color of an existing `Color` object using a web color (hex code).

**Usage:**<br>
`web(value)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `value` | A web color (hex code) as a string used to update the existing color instance. |

```python
# Create a custom teal color and set it as the pen color
robot_color = Color("#32C8B6")
robot.screen.set_pen_color(robot_color)

# Draw a rectangle with the teal outline
robot.screen.draw_rectangle(30, 70, 80, 50)

# Draw another rectangle with the new magenta outline
robot_color.web("#AA2896")
robot.screen.set_pen_color(robot_color)
robot.screen.draw_rectangle(130, 70, 80, 50)
```