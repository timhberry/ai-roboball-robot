---
title: Screen | VEX AIM - Python API
description: Explore the Python API reference for the screen on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to code using the screen.
---

```{highlight} python
:linenothreshold: 5
```

# Screen

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

The VEX AIM Coding Robot's screen provides methods for displaying text, managing the cursor, drawing shapes, and handling touch interactions. Below is a list of all available methods:

<!-- ![A top down view of a turned-off AIM Robot that displays a white square overlay with its corners labeled with coordinates (0,0), (240,0), (0,240), and (240,240). A red circle is centered within the square, and a white dashed crosshair intersects at the middle of the image, marked with the coordinates 120,120.](/_static/img/screen/aim-screen-resolution.png) -->

**Cursor Print – Display text using a row/column system.**  
- [print](#print) – Prints text at the current cursor position.  
- [set_cursor](#set_cursor) – Sets the cursor to a specific row and column.  
- [next_row](#next_row) – Moves the cursor to column 1 of the next row.  
- [clear_row](#clear_row) – Clears a row of text.  
- [get_row](#get_row) – Returns the current cursor row.  
- [get_column](#get_column) – Returns the current cursor column.  

**XY Print – Display text at a specific screen coordinate.**  
- [print_at](#print_at) – Prints text at a specific x and y location.  
- [set_origin](#set_origin) – Sets a new origin for printing and drawing.  

**Mutators – Clear the screen or update visual settings.**  
- [clear_screen](#clear_screen) – Clears the screen of all drawings and text.  
- [set_font](#set_font) – Sets the font for printed text.  
- [set_pen_width](#set_pen_width) – Sets the thickness for drawn shapes and lines.  
- [set_pen_color](#set_pen_color) – Sets the color for outlines and text.  
- [set_fill_color](#set_fill_color) – Sets the fill color for shapes and backgrounds.  

**Draw – Add graphics and images to the screen.**  
- [draw_pixel](#draw_pixel) – Draws a pixel at a specific x and y position.  
- [draw_line](#draw_line) – Draws a line between two points.  
- [draw_rectangle](#draw_rectangle) – Draws a rectangle.  
- [draw_circle](#draw_circle) – Draws a circle.  
- [show_file](#show_file) – Displays an uploaded image.  
- [set_clip_region](#set_clip_region) – Restricts where drawings and text can appear.  

**Touch – Detect and respond to screen presses.**  
- [x_position](#x_position) – Returns the x-coordinate where the screen is pressed.  
- [y_position](#y_position) – Returns the y-coordinate where the screen is pressed.  
- [pressing](#pressing) – Returns whether the screen is currently being pressed.  

**Callback – Run functions when the screen is pressed or released.**  
- [pressed](#pressed) – Registers a function to call when the screen is pressed.  
- [released](#released) – Registers a function to call when the screen is released.  

## Cursor Print

### print

```{vexcode}
id: aim_looks_robot_screen_print
```

`print` displays text on the robot's screen at the current [cursor position](#set_cursor) and [font](#set_font).

**Usage:**<br>`robot.screen.print(text)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `text` | 	The text, number, or variable value to display on the screen. |

```python
# Display a message at the starting cursor position
robot.screen.print("Hello, Robot!")
```
![Shows the robot.screen.print method with the word "Hello Robot!"](/_static/img/screen/robot-screen-printA.png)

### set_cursor

```{vexcode}
id: aim_looks_robot_screen_set_cursor
```

`set_cursor` places the text cursor at a specific row and column on the screen. The number of rows and columns that fit depends on the selected font. With the default monospaced medium font, the screen can clearly display up to 8 rows and 13 columns. Text placed beyond this range may be cut off or harder to read.

Monospaced fonts have characters that are all the same width, making text placement consistent. In contrast, proportional fonts vary in character width, so some letters take up more space than others. However, regardless of which type is used, the `set_cursor` positions the cursor based on row and column size, not font style. The font size can be adjusted using the [set_font](#set_font).  

**Usage:**<br>`robot.screen.set_cursor(row, column)`

| Parameters | Description |
| :----------------:|:-------------------------------------- |
| `row` | The row of the cursor. |
| `column` | The column of the cursor. |

```python
# Display text starting at Row 3 Column 2
robot.screen.set_cursor(3, 2)
robot.screen.print("Row 3, Column 2")
```

![Shows the robot.screen.print_at method with Row 3, Column 2 printed at the row 3 column 2](/_static/img/screen/robot-screen-rowB.png)

### next_row

```{vexcode}
id: aim_looks_robot_screen_next_row
```

`next_row` moves the cursor to column 1 on the next row on the robot’s screen.

**Usage:**<br>`robot.screen.next_row()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| | This method has no parameters. |

```python
# Display two lines of text
robot.screen.print("Line 1")
robot.screen.next_row()
robot.screen.print("Line 2")
```

![Shows the robot.screen.next_row method with Line 1 and Line 2 printed on the robot screen in line 1 and line 2 respectively.](/_static/img/screen/robot-screen-next-rowA.png)

### clear_row

```{vexcode}
id: aim_looks_robot_screen_clear_row
```

`clear_row` clears a row of text on the robot's screen.

**Usage:**<br>`robot.screen.clear_row(row, color)`

| Parameter | Description |
|:--:|:--|
| `row` | Optional. The row to clear. The default is the current cursor row. |
| `color` | Optional. The color to apply to the cleared row. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](Logic/Color_objects.md). |


```python
# Display text on two rows
robot.screen.print("This text stays")
robot.screen.next_row()
robot.screen.print("This text disappears")

# Wait 3 seconds before clearing only the second row
wait(3, SECONDS)
robot.screen.clear_row()
```
```python
# Turn the 5th row green
robot.screen.clear_row(5, GREEN)
```

![Shows the robot.screen.clear_row method with a green stripe on the line 5 from the screen.](/_static/img/screen/robot-screen-clear-row.png)

### get_row

```{vexcode}
id: aim_sensing_robot_screen_row
```

`row` returns the current row where text will be printed as an integer.

**Usage:**<br>`robot.screen.get_row()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| | This method has no parameters. |


```python
# Set cursor to (3,2) and print row number
robot.screen.set_cursor(3, 2)
robot.screen.print(robot.screen.get_row())
```
![Shows the robot.screen.print_at method by showing row number 3 when you set curosr to 3,2](/_static/img/screen/row.png)

### get_column

```{vexcode}
id: aim_sensing_robot_screen_column
```

`column` returns the current column where text will be printed as an integer.

**Usage:**<br>`robot.screen.get_column()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| | This method has no parameters. |


```python
# Set cursor to (3,2) and print column number
robot.screen.set_cursor(3, 2)
robot.screen.print(robot.screen.get_column())
```

![Shows the robot.screen.print_at method by showing column number 2 when you set curosr to 3,2](/_static/img/screen/column.png)

## XY Print

### print_at

```{vexcode}
id: aim_looks_robot_screen_print_at
```

`print_at` block displays text on the robot's screen at a specified x and y-coordinate (in pixels) with the currently set [font](#set_font). This method disregards the current cursor position.

**Usage:**<br>
`robot.screen.print_at(text, x, y)`

| Parameter | Description |
|:--:|:--|
| `text` | The text, number, or variable value to display on the screen. |
| `x` | The horizontal position of the text, as an integer from 0 to 240 pixels. 0 is left; 240 is right. |
| `y` | The vertical position of the text, as an integer from 0 to 240 pixels. 0 is the top; 240 is the bottom. |


```python
# Display a message in the middle of the screen
robot.screen.print_at("Hello, Robot!", x=40, y=120)
```

![Shows the robot.screen.print_at method with "Hello, Robot!" in the middle of the screen which is (40, 120)](/_static/img/screen/robot-screen-print-atA.png)

### set_origin

```{vexcode}
id: aim_looks_robot_screen_set_origin
```

`set_origin` sets the origin (0,0) used for drawing or printing on the robot's screen. By default, drawing or printing methods consider the top left corner of the screen as the origin. This method can reset the origin to an alternate (x, y) screen coordinate location.

**Usage:**<br>
`robot.screen.set_origin(x, y)`

| Parameter | Description |
|:--:|:--|
| `x` | The new x-coordinate to set as the origin, given as an integer from 0 to 240. |
| `y` | The new y-coordinate to set as the origin, given as an integer from 0 to 240. |


```python
# Set the origin to the center of the screen
robot.screen.set_origin(120, 120)

# Draw a rectangle at the new origin
robot.screen.draw_rectangle(0, 0, 80, 40)
```

![The robot’s screen shows a white rectangle with the upper left corner in the center.](/_static/img/screen/aim-set-origin-example.png)

## Mutators

### clear_screen

```{vexcode}
id: aim_looks_robot_screen_clear_screen
```

```{vexcode}
id: aim_looks_robot_screen_clear_screen_color
```

`clear_screen` clears all drawings and text from the robot's screen. By default, it also resets the cursor position to row 1, column 1.

**Usage:**<br>
`robot.screen.clear_screen(row, column, color)`

| Parameter | Description |
|:--:|:--|
| `row` | Optional. The row number to move the cursor to after clearing. Default 1. |
| `column` | Optional. The column number to move the cursor to after clearing. Default is 1. |
| `color` | Optional. Sets the screen color. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](Logic/Color_objects.md). |


```python
# Draw a circle, and clear it after 2 seconds
robot.screen.draw_circle(120, 120, 60)
wait(2, SECONDS)
robot.screen.clear_screen()
```

```python
# Set the background color of the screen to red
robot.screen.clear_screen(RED)
```

![The robot’s screen is colored entirely red.](/_static/img/screen/aim-end-of-clear-screen-example.png)

### set_font

```{vexcode}
id: aim_looks_robot_screen_set_font
```

`set_font` sets the font used for displaying text on the robot’s screen. This font will apply to all text printed with [print](#print) or [print_at](#print_at). The default font at the start of a project is `MONO24`.

**Usage:**<br>
`robot.screen.set_font(fontname)`

| Parameter | Description |
|:--:|:--|
| `fontname` | Sets the font to one of the following:<br><ul><li>`MONO12`</li><li>`MONO15`</li><li>`MONO20`</li><li>`MONO24`</li><li>`MONO30`</li><li>`MONO40`</li><li>`MONO60`</li><li>`PROP20`</li><li>`PROP30`</li><li>`PROP40`</li><li>`PROP60`</li></ul>These options are shown below. |


| ![The robot screen printed numbers and letters with MONO 12 font. It shows A-Z. On the bottom of the screen, it is 26 across and 15 rows.](/_static/img/fonts/mono12.png)<br>`MONO12` | ![The robot screen printed numbers and letters with MONO 15 font. It shows A-T. On the bottom of the screen, it is 20 across and 12 rows.](/_static/img/fonts/mono15.png)<br>`MONO15` | ![The robot screen printed numbers and letters with MONO 20 font. It shows A-P. On the bottom of the screen, it is 16 across and 9 rows.](/_static/img/fonts/mono20.png)<br>`MONO20` |
|:--:|:--:|:--:|
| ![The robot screen printed numbers and letters with MONO 24 font. It shows A-M. On the bottom of the screen, it is 13 across and 8 rows.](/_static/img/fonts/mono24.png)<br>`MONO24` | ![The robot screen printed numbers and letters with MONO 30 font. It shows A-K. On the bottom of the screen, it is 11 across and 6 rows.](/_static/img/fonts/mono30.png)<br>`MONO30` | ![The robot screen printed numbers and letters with MONO 40 font. It shows A-K. On the bottom of the screen, it is 8 across and 5 rows.](/_static/img/fonts/mono40.png)<br>`MONO40` |
| ![The robot screen printed numbers and letters with MONO 60 font. It shows 1-6. On the bottom of the screen, it is 3 rows.](/_static/img/fonts/mono60.png)<br>`MONO60` | ![The robot screen printed numbers and letters with PROP 20 font. It shows A-S. On the bottom of the screen, it is 8 across and 9 rows.](/_static/img/fonts/prop20.png)<br>`PROP20` | ![The robot screen printed numbers and letters with PROP 30 font. It shows A-M. On the bottom of the screen, it is 15 across and 6 rows.](/_static/img/fonts/prop30.png)<br>`PROP30` |
| ![The robot screen printed numbers and letters with PROP 40 font. It shows A-M. On the bottom of the screen, it is 15 across and 6 rows.](/_static/img/fonts/prop40.png)<br>`PROP40` | ![The robot screen printed numbers and letters with PROP 60 font. It shows 1-7. On the bottom of the screen, it is 7 across and 3 rows.](/_static/img/fonts/prop60.png)<br>`PROP60` |  |

```python
# Display text using a larger font
robot.screen.set_font(MONO40)
robot.screen.print("VEX")
```

![The robot’s screen shows the word VEX in Mono 40 font in the upper left corner.](/_static/img/screen/robot-screen-set-font.png)

### set_pen_width

```{vexcode}
id: aim_looks_robot_screen_set_pen_width
```

`set_pen_width` sets the pen width used for drawing lines and shapes.

**Usage:**<br>
`robot.screen.set_pen_width(width)`

| Parameter | Description |
|:--:|:--|
| `width` | The pen width, given as an integer in pixels in a range from 0 to 32. |


```python
# Draw a rectangle with a pen width of 10
robot.screen.set_pen_width(10)
robot.screen.draw_rectangle(50, 50, 130, 60)
```

![The robot’s screen shows a red rectangle with a thin border drawn centered across the top.](/_static/img/screen/aim-set-pen-width.png)

### set_pen_color

```{vexcode}
id: aim_looks_robot_screen_set_pen_color
```

`set_pen_color` sets the pen color used for drawing lines, shapes, and text.

| Parameter | Description |
|:--:|:--|
| `color` | Optional. Sets the pen color. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](Logic/Color_objects.md). |


**Usage:**<br>
`robot.screen.set_pen_color(color)`

```python
# Draw a rectangle with a red pen
robot.screen.set_pen_color(RED)
robot.screen.draw_rectangle(50, 50, 130, 60)
```
![The robot’s screen shows a red rectangle with a thin border drawn centered across the top.](/_static/img/screen/aim-set-pen-color.png)

### set_fill_color

```{vexcode}
id: aim_looks_robot_screen_set_fill_color
```

`set_fill_color` method sets the fill color used when shapes are drawn. 

| Parameter | Description |
|:--:|:--|
| `color` | Optional. Sets the fill color. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](Logic/Color_objects.md). |

**Usage:**<br>`robot.screen.set_fill_color(color)`

```python
# Draw two orange rectangles
robot.screen.set_fill_color(ORANGE)
robot.screen.draw_rectangle(50, 50, 100, 60)
robot.screen.draw_rectangle(50, 130, 100, 60)
```
![The robot’s screen shows two parallel orange rectangles with white thin borders drawn on the screen, slightly off center to the left.](/_static/img/screen/aim-set-fill-color-example.png)


```python
# Display text with a purple background
robot.screen.set_fill_color(PURPLE)
robot.screen.print("Highlight")
```

![The robot’s screen shows the word Highlight in white text with purple highlighting around it printed beginning in the upper left corner.](/_static/img/screen/aim-set-fill-color-example2A.png)

## Draw

### draw_pixel

```{vexcode}
id: aim_looks_robot_screen_draw_pixel
```

`draw_pixel` draws a pixel at the specified (x, y) screen coordinate in the current pen color. It uses the current pen color set by [`set_pen_color`](#set_pen_color).

**Usage:**<br>
`robot.screen.draw_pixel(x, y)`

| Parameter | Description |
|:--:|:--|
| `x` | The x-coordinate where the pixel will be drawn, given as an integer from 0 to 240. |
| `y` | The y-coordinate where the pixel will be drawn, given as an integer from 0 to 240. |

```python
# Draw a pixel at the center of the screen
robot.screen.draw_pixel(120, 120)
```

![The robot’s screen shows a single pixel printed in white in the center.](/_static/img/screen/aim-draw-pixel.png)


### draw_line

```{vexcode}
id: aim_looks_robot_screen_draw_line
```

`draw_line` draws a line from the first specified screen coordinate `(x1, y1)` to the second specified screen coordinate `(x2, y2)`. It uses the current the pen width set by [set_pen_width](#set_pen_width) and pen color set by [set_pen_color](#set_pen_color).

The x and y-coordinates use the default origin of (0, 0) unless a different origin has been set using [`set_origin`](#set_origin).

**Usage:**<br>
`robot.screen.draw_line(x1, y1, x2, y2)`

| Parameter | Description |
|:--:|:--|
| `x1` | The starting x-coordinate of the line, given as an integer from 0 to 240. |
| `y1` | The starting y-coordinate of the line, given as an integer from 0 to 240. |
| `x2` | The ending x-coordinate of the line, given as an integer from 0 to 240. |
| `y2` | The ending y-coordinate of the line, given as an integer from 0 to 240. |

```python
# Draw a line from the top left to bottom right of the screen
robot.screen.draw_line(0, 0, 240, 240)
```

![The robot’s screen shows a thin diagonal line across the center, from the upper left corner to the lower right corner.](/_static/img/screen/aim-draw-line.png)

### draw_rectangle

```{vexcode}
id: aim_looks_robot_screen_draw_rectangle
```

`draw_rectangle` draws a rectangle with its top-left corner at the specified `(x, y)` coordinate and a size determined by the given width and height, all measured in pixels. The rectangle's outline is drawn using the current pen width set by [`set_pen_width`](#set_pen_width) and the pen color set by [`set_pen_color`](#set_pen_color). The interior is filled with the color set by [`set_fill_color`](#set_fill_color).

The x and y-coordinates use the default origin of (0,0) unless a different origin has been set using [set_origin](#set_origin).

**Usage:**<br>`robot.screen.draw_rectangle(x, y, width, height, color)`

| Parameter | Description |
|:--:|:--|
| `x` | The x-coordinate of the top-left corner of the rectangle, given as an integer from 0 to 240. |
| `y` | The y-coordinate of the top-left corner of the rectangle, given as an integer from 0 to 240. |
| `width` | The width of the rectangle, given as an integer from 0 to 240. |
| `height` | The height of the rectangle, given as an integer from 0 to 240. |
| `color` | Optional. The fill color of the rectangle. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](https://test-api.vex.com/aim

```python
# Draw a red rectangle on the screen
robot.screen.draw_rectangle(50, 50, 130, 60, RED)
```

![AIM Robot Draw Rectangle](/_static/img/screen/aim-draw-rectangle.png)

### draw_circle

```{vexcode}
id: aim_looks_robot_screen_draw_circle
```

`draw_circle` draws a circle with its center at the specified `(x, y)` coordinate and a size determined by the given radius, all measured in pixels. The circle's outline is drawn using the current pen width set by [`set_pen_width`](#set_pen_width) and the pen color set by [`set_pen_color`](#set_pen_color). The interior is filled with the color set by [`set_fill_color`](#set_fill_color).


The x and y-coordinates use the default origin of (0,0) unless a different origin has been set using [set_origin](#set_origin).

**Usage:**<br>`robot.screen.draw_circle(x, y, radius, color)`


| Parameter | Description |
|:--:|:--|
| `x` | The x-coordinate of the center of the circle, given as an integer from 0 to 240. |
| `y` | The y-coordinate of the center of the circle, given as an integer from 0 to 240. |
| `radius` | The radius of the circle, given as an integer from 0 to 240 pixels. |
| `color` | Optional. The fill color of the circle. Options include:<br><ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE`</li><li>`YELLOW`</li></ul>You can also specify a [custom color](Logic/Color_objects.md). |


```python
# Draw a green circle on the screen
robot.screen.draw_circle(120, 120, 40, GREEN)
```

![AIM Robot Draw Circle](/_static/img/screen/aim-draw-circle.png)

### show_file

```{vexcode}
id: aim_looks_robot_screen_show_file
```

`show_file` displays a custom uploaded image on the robot’s screen, with its position set using the `x`, `y`, and `center` parameters based on the image’s reference point.

**Usage:**<br>
`robot.screen.show_file(file, x, y, center)`

| Parameter | Description |
|:--:|:--|
| `file` | The custom image to use, from `IMAGE1` to `IMAGE10`. The image number matches the number shown in the AIM control panel. |
| `x` | The horizontal offset for the image, given as an integer in pixels. Positive values move it right; negative values move it left. |
| `y` | The vertical offset for the image, given as an integer in pixels. Positive values move it down; negative values move it up. |
| `center` | Optional. If `center=True`, the image is placed using its center at coordinate (120, 120). By default (`center=False`), the top-left corner of the image is used and positioned relative to the current [origin](#set_origin). |


```python
# Display uploaded Image 1 in the top left corner
robot.screen.show_file(IMAGE1, 0, 0)
```

```python
# Show the same image on both sides of the screen
# Image size is 120 x 120
robot.screen.show_file(IMAGE1, 65, 0, center=True)
robot.screen.show_file(IMAGE1, -65, 0, center=True)
```

### set_clip_region

`set_clip_region` defines a rectangular area on the screen where all drawings and text will be confined. Any content outside this region will not be displayed.

**Usage:**<br>
`robot.screen.set_clip_region(x, y, width, height)`

| Parameter | Description |
|:--:|:--|
| `x` | The x-coordinate of the top-left corner of the clip region, given as an integer or float from 0 to 240. |
| `y` | The y-coordinate of the top-left corner of the clip region, given as an integer or float from 0 to 240. |
| `width` | The width of the clip region in pixels, given as an integer or float from 0 to 240. |
| `height` | The height of the clip region in pixels, given as an integer or float from 0 to 240. |



```python
# Restrict text and drawings to a specific region
robot.screen.set_clip_region(0, 0, 120, 120)
robot.screen.draw_rectangle(60, 60, 100, 100, RED)
robot.screen.print_at("Cut off!", x=60, y=60)
```

![The robot’s screen shows a red square with the words Cut o above it in the upper left corner, stopping at the center of the screen.](/_static/img/screen/set_clip_region_exampleA.png)

## Touch

### pressing

```{vexcode}
id: aim_sensing_robot_screen_pressing
```

`pressing` returns a Boolean indicating whether the screen is currently being pressed.
- `True` – The screen is being pressed
- `False` – The screen is not being pressed

**Usage:**<br>
`robot.screen.pressing()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
|  | This method has no parameters. |

```python
# Turn LEDs white only while the screen is pressed.
while True:
    if robot.screen.pressing():
        robot.led.on(ALL_LEDS, WHITE)
    else: 
        robot.led.off(ALL_LEDS)

    wait(50, MSEC)
```

### x_position

```{vexcode}
id: aim_sensing_robot_screen_x_position
```

`x_position` returns the x-coordinate where the screen is pressed as an integer from 0 (left) to 240 (right).

**Usage:**<br>`robot.screen.x_position()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
|  | This method has no parameters. |

```python
# Display the x-coordinate of where
# the screen is pressed
while True:
    if robot.screen.pressing():
        robot.screen.clear_screen()
        robot.screen.print(robot.screen.x_position())
    wait (50, MSEC)
```

### y_position

```{vexcode}
id: aim_sensing_robot_screen_y_position
```

`y_position` returns the y-coordinate where the screen is pressed as an integer from 0 (top) to 240 (bottom).

**Usage:**<br>`robot.screen.y_position()`


```python
# Display the y-coordinate of where
# the screen is pressed
while True:
    if robot.screen.pressing():
        robot.screen.clear_screen()
        robot.screen.print(robot.screen.y_position())
    wait (50, MSEC)
```

## Callback

### pressed

```{vexcode}
id: aim_events_robot_screen_pressed
```

`pressed` registers a method to be called when the robot's screen is pressed.

**Usage:**<br>`robot.screen.pressed(callback, arg)`


| Parameters | Description                                                  |
|:------------:|--------------------------------------------------------------|
| `callback`  | A method that will be called when the screen is pressed. |
| `arg` | Optional. A tuple containing arguments to pass to the callback method when it is called. |     

```python
# Set the LEDs to green when the screen is pressed.
def screen_touched():
    robot.led.on(ALL_LEDS, GREEN)

robot.screen.pressed(screen_touched)
```

### released

```{vexcode}
id: aim_events_robot_screen_released
```

`released` registers a method to be called when the screen is no longer being pressed.

**Usage:**<br>`robot.screen.released(callback, arg)`


| Parameters | Description                                                  |
|:------------:|--------------------------------------------------------------|
| `callback`  | A method that will be called when the screen is released. |
| `arg` | Optional. A [tuple](Logic/Variables.md#tuple) containing arguments to pass to the callback method when it is called. |           

```python
# Set the LEDs to blue when the screen is released.
def screen_released():
    robot.led.on(ALL_LEDS, BLUE)

robot.screen.released(screen_released)
```