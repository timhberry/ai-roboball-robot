---
title: Motion | VEX AIM - Python API
description: Explore the Python API reference for motion with the VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples.
---

```{highlight} python
:linenothreshold: 5
```

# Motion

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

The VEX AIM Coding Robot features a holonomic drivetrain, allowing it to move in any direction and rotate independently. Motion provides methods for movement, turning, speed adjustments, and position tracking.

![Circular compass dial from 0-315 degrees surrounding a dark gray display with navy blue screen. The front of the robot faces 0 degrees on the compass dial.](/_static/img/Movement/rotation_angles.png)

Below is a list of available methods:

**Actions – Move and turn the robot.**  
- [move_at](#move_at) – Moves the robot at a specified angle.  
- [move_for](#move_for) – Moves the robot at an angle for a specific distance.  
- [move_with_vectors](#move_with_vectors) – Moves the robot using vector-based x, y, and rotation values.  
- [turn](#turn) – Turns the robot left or right.  
- [turn_for](#turn_for) – Turns the robot a set number of degrees.  
- [turn_to](#turn_to) – Turns the robot to face a specific heading.  
- [stop_all_movement](#stop_all_movement) – Stops all movement of the robot.  

**Mutators – Set default movement and turn speeds.**  
- [set_move_velocity](#set_move_velocity) – Sets the default movement speed.  
- [set_turn_velocity](#set_turn_velocity) – Sets the default turn speed.  
- [set_xy_position](#set_xy_position) – Sets the robot’s current position.  

**Getters – Return robot state and position.**  
- [get_x_position](#get_x_position) – Returns the robot’s x-coordinate.  
- [get_y_position](#get_y_position) – Returns the robot’s y-coordinate.  
- [is_move_active](#is_move_active) – Returns whether the robot is currently moving.  
- [is_turn_active](#is_turn_active) – Returns whether the robot is currently turning.  
- [is_stopped](#is_stopped) – Returns whether the robot is stopped.  

## Actions

### move_at

```{vexcode}
id: aim_robot_move_at
```

<!-- **incomplete - velocity range for MMPS validation needed** -->

`move_at` moves the robot at a specified angle (from -360 to 360 degrees) and velocity (from 0 to 100 in `PERCENT` or 0 to 200 in `MMPS`).

**Usage:**

`robot.move_at(angle, velocity, units)`

| Parameters       | Description                                                                 |
|:------------------: | :------------------------------------------------------------------------|
| `angle` | The angle, as an integer or float, at which the robot moves, ranging from -360 to 360 degrees. |
| `velocity` | Optional. The velocity as an integer or float number at which the robot will move. If the velocity is not specified, the default velocity is 50 percent. The range can be: <ul><li> from 0 to 100 in `PERCENT`.</li><li> from 0 to 200 in `MMPS`.</li></ul> |
| `units` | Optional. The velocity unit is `PERCENT` (default) or millimeters per second `MMPS`.|

```python
# Move right, then move forward and stop.
robot.move_at(90)
wait(1,SECONDS)
robot.move_at(0)
wait(1,SECONDS)
robot.stop_all_movement()
```

```python
# Move right slowly, move in reverse quickly and stop.
robot.move_at(90, 25)
wait(2, SECONDS)
robot.move_at(180, 100, PERCENT)
wait(1, SECONDS)
robot.stop_all_movement()
```

```python
# Move diagonally to the right and stop.
robot.move_at(45.33)
wait(1,SECONDS)
robot.stop_all_movement()
```

### move_for

```{vexcode}
id: aim_robot_move_for
```

<!-- **incomplete - is heading parameter going to exist?** -->

`move_for` moves the robot at a specific angle for a specified distance.

**Usage:**

`robot.move_for(distance, angle, velocity, units, wait)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `distance` | The distance, as an integer or float, that the robot will move, measured in millimeters (mm). |
| `angle` | The angle, as an integer or float, at which the robot moves, ranging from -360 to 360 degrees. |
| `velocity` | Optional. The velocity as an integer or float number at which the robot will move. If the velocity is not specified, the default velocity is 50%. |
| `units` | Optional. The velocity unit is `PERCENT` (default) or millimeters per second `MMPS`.|
| `wait` | Optional.<ul><li>`wait=True` (default) - The robot waits until `move_for` is complete before executing the next line of code.</li><li>`wait=False` - The robot starts the action and moves on to the next line of code right away, without waiting for `move_for` to finish.</li></ul>|

<!-- | Parameter | Description |
|:--|:--|
| `distance` | A `float` representing how far the robot should move, measured in millimeters. |
| `angle` | A `float` representing the direction the robot will move, in degrees from –360 to 360. |
| `velocity` | Optional. A `float` representing how fast the robot should move, in the unit defined by the `units` parameter (default is `50` `PERCENT`). Valid ranges:<br>– `PERCENT`: 0 to 100<br>– `MMPS`: 0 to 200 |
| `units` | Optional. The velocity unit:<br>– `PERCENT` (default)<br>– `MMPS`: Millimeters per second |
| `wait` | Optional. Whether or not the robot should wait for the action to complete:<br>– `wait=True` (default): The robot waits until the action is done.<br>– `wait=False`: The robot starts the next line of code immediately. | -->


```python
# Move right, then move forward.
robot.move_for(50, 90)
robot.move_for(100, 0)
```

```python
# Move in reverse slowly, then move forward quickly.
robot.move_for(100, 180, 25)
robot.move_for(100, 0, 100, PERCENT)
```

```python
# Drive forward and blink all LEDs red.
robot.move_for(100, 0, wait=False)
robot.led.on(ALL_LEDS, RED)
wait(0.5, SECONDS)
robot.led.on(ALL_LEDS, BLACK)
wait(0.5, SECONDS)
robot.led.on(ALL_LEDS, RED)
wait(0.5, SECONDS)
robot.led.on(ALL_LEDS, BLACK)
```

### move_with_vectors

```{vexcode}
id: aim_robot_move_with_vectors
```

`move_with_vectors` moves the robot using vector-based motion, combining horizontal (X-axis) and vertical (Y-axis) movement and having the robot rotate at the same time.

<!-- ![test](/_static/img/Movement/move_with_vectors.png)
_Placeholder Image_ -->

**Usage:**

`robot.move_with_vectors(x, y, r)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `x` | The robot's velocity along the X-axis (side-to-side movement). Accepts a value from -100 to 100 as a percent, where negative values move left and positive values move right. |
| `y` | The robot's velocity along the Y-axis (forward and backward movement). Accepts a value from -100 to 100 as a percent, where negative values move backward and positive values move forward. |
| `r` | The robot's rotational velocity. Accepts a value from -100 to 100 as a percent, where negative values rotate counterclockwise and positive values rotate clockwise. |

```python
# Move at 15°
robot.move_with_vectors(48.3, 12.95, 0)
wait(2, SECONDS)
robot.stop_all_movement()
```

```python
# Move at 45° while turning counterclockwise.
robot.move_with_vectors(50, 50, -30)
wait(2, SECONDS)
robot.stop_all_movement()
```

### turn

```{vexcode}
id: aim_robot_turn
```

`turn` turns the robot in a specific direction.

**Usage:**

`robot.turn(direction, velocity, units)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `direction` | The direction in which the robot turns: `LEFT` or `RIGHT`. |
| `velocity` | Optional. The velocity, as an integer or float, at which the robot turns. If the velocity is not specified, the default velocity is 50%. |
| `units` | Optional. degrees per second `PERCENT` (default) or `DPS`.|

```python
# Turn left, then stop.
robot.turn(LEFT)
wait(1, SECONDS)
robot.stop_all_movement()
```

```python
# Turn left quickly, turn right slowly, then stop.
robot.turn(LEFT, 80)
wait(2, SECONDS)
robot.turn(RIGHT, 20, PERCENT)
wait(3, SECONDS)
robot.stop_all_movement()
```

### turn_for

```{vexcode}
id: aim_robot_turn_for
```

`turn_for` turns the robot in a specified direction for a set distance relative to its current facing direction.

**Usage:**

`robot.turn_for(direction, angle, velocity, units, wait)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `direction` | The direction in which the robot turns: `LEFT` or `RIGHT`. |
| `angle` | The angle, as an integer or float, at which the robot moves, ranging from -360 to 360 degrees. |
| `velocity` | Optional. The velocity at which the robot will turn. If the velocity is not specified, the default velocity is 50% or any velocity. |
| `units` | Optional. degrees per second `PERCENT` (default) or `DPS`.|
| `wait` | Optional.<ul><li>`wait=True` (default) - The robot waits until `turn_for` is complete before executing the next line of code.</li> <li>`wait=False` - The robot starts the action and moves to the next command without waiting for `turn_for` to finish.</li></ul> |

```python
# Turn left, then turn around to the right.
robot.turn_for(LEFT, 90)
robot.turn_for(RIGHT, 180)
```

```python
# Turn left quickly, then turn right slowly.
robot.turn_for(LEFT, 90, 100)
robot.turn_for(RIGHT, 180, 15, PERCENT)
```

```python
# Turn right and blink all LEDs blue.
robot.turn_for(RIGHT, 180, wait=False)
robot.led.on(ALL_LEDS, BLUE)
wait (0.5, SECONDS)
robot.led.off(ALL_LEDS)
wait (0.5, SECONDS)
robot.led.on(ALL_LEDS, BLUE)
wait (0.5, SECONDS)
robot.led.off(ALL_LEDS)
```

### turn_to

```{vexcode}
id: aim_robot_turn_to
```

`turn_to` is used to turn the robot to face a specific heading.

**Usage:**

`robot.turn_to(heading, velocity, units, wait)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `heading` | The heading that the robot will turn to face from –360 to 360 degrees. |
| `velocity` | Optional. The velocity as an integer or float number at which the robot will turn. If the velocity is not specified, the default velocity is 50%. |
| `units` | Optional. degrees per second `PERCENT` (default) or `DPS`.|
| `wait` | Optional. <ul><li>`wait=True` (default) - The robot waits until `turn_to` is complete before executing the next line of code.</li> <li>`wait=False` - The robot starts the action and moves on to the next line of code right away, without waiting for `turn_to` to finish.</li></ul>|

```python
# Turn to face each cardinal directions.
robot.turn_to(90)
wait(2, SECONDS)
robot.turn_to(180)
wait(2, SECONDS)
robot.turn_to(270)
wait(2, SECONDS)
robot.turn_to(0)
```

```python
# Turn to face backward slowly, then face forward quickly.
robot.turn_to(180, 25)
wait(1, SECONDS)
robot.turn_to(0, 90, PERCENT)
```

```python
# Turn around quickly and blink all LEDs green.
robot.turn_to(180, 100, wait=False)
robot.led.on(ALL_LEDS, GREEN)
wait(0.5, SECONDS)
robot.led.off(ALL_LEDS)
wait(0.5, SECONDS)
robot.led.on(ALL_LEDS, GREEN)
wait(0.5, SECONDS)
robot.led.off(ALL_LEDS)
```

### stop_all_movement

```{vexcode}
id: aim_robot_stop_all_movement
```

`stop_all_movement` is used to stop all movement of the robot. 

**Usage:**

`robot.stop_all_movement()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Turn right, then stop moving
robot.turn(RIGHT)
wait(1, SECONDS)
robot.stop_all_movement()
```

## Mutators

### set_move_velocity

```{vexcode}
id: aim_robot_set_move_velocity
```

`set_move_velocity` overrides the default velocity for all subsequent movement methods in the project. The default move velocity is 50% (100 millimeters per second).

**Usage:**

`robot.set_move_velocity(velocity, units)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `velocity` | Sets the default movement velocity. |
| `units` | Optional. The velocity unit is `PERCENT` (default) or `MMPS`.|


```python
# Move forward at the default velocity,
robot.set_move_velocity(50)
robot.move_for(100, 0)
wait(1, SECONDS)
# Move slower than the default velocity
robot.set_move_velocity(20)
robot.move_for(100, 0)
wait(1, SECONDS)
# Move faster than the default velocity
robot.set_move_velocity(100)
robot.move_for(100, 0)
```

### set_turn_velocity

```{vexcode}
id: aim_robot_set_turn_velocity
```

`set_turn_velocity` overrides the default velocity for all subsequent turn methods in the project. The default turn velocity is 50% (75 degrees per second).

**Usage:**

`robot.set_turn_velocity(velocity, units)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `velocity` | Sets the default turn velocity. |
| `units` | Optional. degrees per second `PERCENT` (default) or `DPS`.|

```python
# Turn around at default velocity
robot.set_turn_velocity(50)
robot.turn_for(RIGHT, 180)
wait(1, SECONDS)
# Turn around slower than the default velocity
robot.set_turn_velocity(20)
robot.turn_for(RIGHT, 180)
wait(1, SECONDS)
# Turn around faster than the default velocity
robot.set_turn_velocity(100)
robot.turn_for(RIGHT, 180)
```

### set_xy_position

```{vexcode}
id: aim_sensing_set_xy_position
```

`set_xy_position` sets the robot’s current position to specified values. This updates the robot’s internal coordinates.

**Usage:**

`robot.set_xy_position(x, y)`

| Parameters | Description |
|---|---|
| `x` | The new x-coordinate in mm as an integer. |
| `y` | The new y-coordinate in mm as an integer. |

```python
# Set the robot's current position
# Move forward and print the new coordinate
robot.set_xy_position(100, 50)
robot.move_for(150, 0)
robot.screen.print("X:", robot.get_x_position())
robot.screen.next_row()
robot.screen.print("Y:", robot.get_y_position())
```

## Getters

### get_x_position

```{vexcode}
id: aim_sensing_robot_get_x_position
```

`get_x_position` returns the robot’s x-coordinate as an integer in millimeters.

**Usage:**

`robot.get_x_position()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |


```python
# Print the start and end x-value 
# of the robot's position after moving
robot.screen.print("Start X:", robot.get_x_position())
robot.move_for(200, 90)
robot.screen.next_row()
robot.screen.print("End X:", robot.get_x_position())
```

### get_y_position

```{vexcode}
id: aim_sensing_robot_get_y_position
```

`get_y_position` returns the robot’s y-coordinate as an integer in millimeters.

**Usage:**

`robot.get_y_position()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Print the start and end y-value 
# of the robot's position after moving
robot.screen.print("Start Y:", robot.get_y_position())
robot.move_for(200, 0)
robot.screen.next_row()
robot.screen.print("End Y:", robot.get_y_position())
```

### is_move_active

```{vexcode}
id: aim_sensing_robot_is_move_active
```

`is_move_active` returns a Boolean indicating whether the robot is currently moving.
- `True` – The robot is moving.
- `False` – The robot is not moving.

**Usage:**

`robot.is_move_active()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Blink all the LEDs when the robot is moving.
robot.move_for(200, 0, wait=False)

while robot.is_move_active():
    robot.led.on(ALL_LEDS, ORANGE)
    wait(0.5, SECONDS)
    robot.led.on(ALL_LEDS, CYAN)
    wait(0.5, SECONDS)

robot.led.off(ALL_LEDS)
```

### is_turn_active

```{vexcode}
id: aim_sensing_robot_is_turn_active
```

`is_turn_active` returns a Boolean indicating whether the robot is currently turning.
- `True` – The robot is turning.
- `False` – The robot is not turning.

**Usage:**

`robot.is_turn_active()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Blink all the LEDs while the robot is turning
robot.turn_for(RIGHT, 180, wait=False) 

while robot.is_turn_active():
    robot.led.on(ALL_LEDS, GREEN)
    wait(0.5, SECONDS)
    robot.led.on(ALL_LEDS, CYAN)
    wait(0.5, SECONDS)

robot.led.off(ALL_LEDS)
```

### is_stopped

```{vexcode}
id: aim_sensing_robot_is_stopped
```

`is_stopped` returns a Boolean indicating whether the robot is stopped.
- `True` – The robot is completely stopped.
- `False` – The robot is currently moving or turning.

**Usage:**

`robot.is_stopped()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Blink all the LEDs while the robot is moving or turning

def light_show():
    # Flash LEDs while the robot is moving or turning
    while not robot.is_stopped():
        robot.led.on(ALL_LEDS, GREEN)
        wait(.5, SECONDS)
        robot.led.on(ALL_LEDS, PURPLE)
        wait(.5, SECONDS)

    robot.led.off(ALL_LEDS)

robot.move_for(200, 0, wait=False)
light_show()

robot.turn_for(RIGHT, 180, wait=False)
light_show()
```