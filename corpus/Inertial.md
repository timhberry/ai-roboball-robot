---
title: Inertial | VEX AIM - Python API
description: Explore the Python API reference for the gyro on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to code the built-in gyro.
---

```{highlight} python
:linenothreshold: 5
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

# Inertial

```{contents}
:local: true
```
## Introduction

The VEX AIM Coding Robot's Inertial Sensor includes a built-in 3-axis gyroscope for measuring rotational movement and a 3-axis accelerometer for detecting changes in motion. These sensors allow the robot to track its orientation, heading, and acceleration. Below is a list of all available methods:

**Orientation – Get the robot’s heading and angles.**  
- [get_rotation](#get_rotation) – Returns how much the robot has turned since it started.  
- [get_heading](#get_heading) – Returns the current heading (0 to 359.99°).  
- [get_yaw](#get_yaw) – Returns the yaw angle (–180 to 180°).  
- [get_roll](#get_roll) – Returns the roll angle (–180 to 180°).  
- [get_pitch](#get_pitch) – Returns the pitch angle (–90 to 90°).  
- [reset_rotation](#reset_rotation) – Resets the rotation value to zero.  
- [reset_heading](#reset_heading) – Sets the current heading to zero.  
- [set_heading](#set_heading) – Sets the heading to a specific value.  

**Crash – Detect collisions.**  
- [crashed](#crashed) – Registers a function to run when a collision is detected.  
- [set_crash_sensitivity](#set_crash_sensitivity)

**Motion – Measure acceleration and turning speed.**  
- [get_acceleration](#get_acceleration) – Returns acceleration in a specific direction.  
- [get_turn_rate](#get_turn_rate) – Returns turning rate in degrees per second.  

**Calibration – Manage sensor calibration.**  
- [calibrate](#calibrate) – Calibrates the inertial sensor.  
- [is_calibrating](#is_calibrating) – Returns whether the sensor is currently calibrating.  

## Orientation

### get_rotation

```{vexcode}
id: aim_sensing_robot_inertial_get_rotation
```

`get_rotation` returns the robot’s net rotation in degrees as a float.

**Usage:**<br>
`robot.inertial.get_rotation()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display the robot's rotation as it rotates
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(f"Rotation: {robot.inertial.get_rotation():.2f}")
    wait(50, MSEC)
```


### get_heading

```{vexcode}
id: aim_sensing_robot_inertial_get_heading
```

`get_heading` returns the robot's heading angle as a float in the range 0 to 359.99 degrees.

**Usage:** 

`robot.inertial.get_heading()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Turn right until the heading reaches 90 degrees
robot.turn(RIGHT)
while robot.inertial.get_heading() < 90:
    wait(50, MSEC)
robot.stop_all_movement()
```

```python
# Display the robot's heading as it is rotated by hand
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(f"Heading: {robot.inertial.get_heading()} degrees")
    wait(50, MSEC)
```

### get_yaw

```{vexcode}
id: aim_sensing_robot_inertial_get_yaw
```

`get_yaw` returns the robot's yaw angle in the range –180.00 to 180.00 degrees as a float.

The image below uses arrows to show the direction of positive rotation for yaw.

```{image} /_static/img/Inertial/AIM-Yaw.png
:alt: A VEX sensor device is shown with three labeled colored arrows indicating its rotational axes. A red arrow labeled Pitch points diagonally upward to the left, a green arrow labeled Roll points diagonally upward to the right, and a blue arrow labeled Yaw points directly downward from the center.
:class: w-25
```

**Usage:** 

`robot.inertial.get_yaw()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display the robot's yaw angle as it is rotated by hand
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(robot.inertial.get_yaw())
    wait(50, MSEC)
```

### get_roll

```{vexcode}
id: aim_sensing_robot_inertial_get_roll
```

`get_roll` returns the robot's roll angle in the range –180.00 to 180.00 degrees as a float.

The image below uses arrows to show the direction of positive rotation for roll.

```{image} /_static/img/Inertial/AIM-Roll.png
:alt: A VEX sensor device is shown with three labeled colored arrows indicating its rotational axes. An arrow labeled Roll points diagonally upward to the left, a green arrow labeled Roll points diagonally upward to the right, and a blue arrow labeled Yaw points directly downward from the center.
:class: w-25
```

**Usage:** 

`robot.inertial.get_roll()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display the robot's roll angle as it is tilted by hand
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(robot.inertial.get_roll())
    wait(50, MSEC)
```

### get_pitch

```{vexcode}
id: aim_sensing_robot_inertial_get_pitch
```

`get_pitch` returns the robot's pitch angle in the range –90.00 to 90.00 degrees as a float.

The image below uses arrows to show the direction of positive rotation for pitch.

```{image} /_static/img/Inertial/AIM-Pitch.png
:alt: A VEX sensor device is shown with three labeled colored arrows indicating its rotational axes. An arrow labeled Roll points diagonally upward to the left, a green arrow labeled Roll points diagonally upward to the right, and a blue arrow labeled Yaw points directly downward from the center.
:class: w-25
```

**Usage:** 

`robot.inertial.get_pitch()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display the robot's pitch angle as it is tilted by hand
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(robot.inertial.get_pitch())
    wait(50, MSEC)
```

### reset_rotation

```{vexcode}
id: aim_sensing_inertial_reset_rotation
```

`reset_rotation` resets the robot’s gyro rotation value to 0 degrees.

**Usage:**<br>
`robot.inertial.reset_rotation()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Reset the robot's rotation if it exceeds 180 degrees
while True:
    if robot.inertial.get_rotation() >= 180:
        robot.inertial.reset_rotation()
    
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(f"Rotation: {robot.inertial.get_rotation():.2f}")
    
    wait(50, MSEC)
```

### reset_heading

```{vexcode}
id: aim_sensing_inertial_reset_heading
```

`reset_heading` resets the robot's heading to 0 degrees.

**Usage:** 

`robot.inertial.reset_heading()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Turn the robot around using a new 90 degree heading
robot.turn_to(90)
wait(1, SECONDS)
robot.inertial.reset_heading()
robot.turn_to(90)
```

### set_heading

```{vexcode}
id: aim_robot_set_heading
```

`set_heading` sets the robot’s heading to a specified value in the range 0 to 359.99 degrees.

**Usage:** 

`robot.inertial.set_heading(heading)`

| Parameters       | Description                                                                 |
|:---------------- | :---------------------------------------------------------------------------|
| `heading` | The value to use for the new heading in the range 0 to 359.99 degrees. |

```python
# Turn the robot to 90 degrees using its new heading
robot.inertial.set_heading(45)
robot.turn_to(90)
```

## Crash

### crashed

```{vexcode}
id: events_robot_inertial_crashed
```

`crashed` registers a function to be called when the robot detects a collision.

**Usage:**

`robot.inertial.crashed(callback, arg)`

| Parameters | Description |
|:-:|--|
| `callback` | A [function](Logic/Functions.md) that is previously defined to execute when a collision is detected. |
| `arg` | Optional. A tuple containing arguments to pass to the callback function. See [Using Functions with Parameters](Logic/Functions.md#functions-with-parameters) for more information. |

```python
# Define what happens when a crash occurs
def crash_detected():
    # Stop all movement and indicate a crash occurred
    robot.screen.print("Crash detected")
    robot.stop_all_movement()

robot.inertial.crashed(crash_detected)

# Drive forward until crash
robot.move_at(0, 100)
```

### set_crash_sensitivity

```{vexcode}
id: sensing_robot_inertial_set_crash_sensitivity
``` 

`set_crash_sensitivity` adjusts the acceleration threshold required to trigger a crash response.

**Usage:**<br>
`robot.set_crash_sensitivity(sensitivity)`

| Parameters | Description |
|:-:|--|
| `sensitivity` | The crash sensitivity: <ul> <li>`HIGH` — Most sensitive, triggers at 1G.</li> <li>`NORMAL` — Default sensitivity, triggers at 1.5G.</li> <li>`LOW` — Least sensitive, triggers at 2G.</li> </ul> |

```python
def crashed_callback():
    robot.stop_all_movement()
    robot.sound.play(CRASH)

# system event handlers
robot.inertial.crashed(crashed_callback)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

# Detect a crash at a slow velocity.
robot.set_move_velocity(35, PERCENT)
robot.inertial.set_crash_sensitivity(SensitivityType.HIGH)
robot.move_at(0)
```

## Motion

### get_acceleration

```{vexcode}
id: aim_sensing_robot_inertial_get_acceleration
```

`get_acceleration` returns the robot’s acceleration in a specified direction as a float in the range –4.00 to 4.00 g.

![A VEX sensor device is shown with three labeled colored arrows indicating direction. A red arrow labeled RIGHTWARD points diagonally upward to the left, a green arrow labeled FORWARD points diagonally upward to the right, and a blue arrow labeled DOWNWARD points directly downward from the center.](/_static/img/Inertial/Accelerometer-Callouts.png)

**Usage:**

`robot.inertial.get_acceleration(type)`

| Parameters | Description |
|:-:|--|
| `type` | The direction of acceleration to return: <li>`DOWNWARD` - Acceleration affecting the robot’s vertical movement.</li><li>`FORWARD` - Acceleration affecting the robot’s movement along its front-to-back direction.</li><li>`RIGHTWARD` - Acceleration affecting the robot’s movement along its side-to-side direction.</li></ul> |

```python
# Display the acceleration as the robot begins to move
robot.screen.set_cursor(4,1)
sitting_accel = robot.inertial.get_acceleration(RIGHTWARD)
robot.screen.print(f"Resting: {sitting_accel:.2f}")
wait(0.5, SECONDS)
robot.screen.next_row()

robot.move_at(90, 100)
wait(0.1, SECONDS)

robot.screen.print(f"Startup: {robot.inertial.get_acceleration(RIGHTWARD):.2f}")
```

### get_turn_rate 

```{vexcode}
id: aim_sensing_robot_inertial_get_turn_rate
```

`get_turn_rate` returns the robot's turning rate in degrees per second (DPS) as a float, from –1000.00 to 1000.00 dps.

The image below uses arrows to show the direction of positive rotation for roll, pitch, and yaw.

![A VEX sensor device is shown with three labeled colored arrows indicating its rotational axes. A red arrow labeled Pitch points diagonally upward to the left, a green arrow labeled Roll points diagonally upward to the right, and a blue arrow labeled Yaw points directly downward from the center.](/_static/img/Inertial/Gyro-Axes2.png)

**Usage:** 

`robot.inertial.get_turn_rate(axis)`

| Parameters | Description |
|:-|--|
| `axis` | Which orientation to return: `YAW`, `ROLL`, or `PITCH`. |

```python
# Display the gyro rate as the robot is rotated by hand
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print(robot.inertial.get_turn_rate(YAW))
    wait(50, MSEC)
```

## Calibration

Calibration is an internal procedure that measures and compensates for sensor noise and drift over a 2-second period. During this time, the robot must remain completely still (i.e., on a stable surface without any external movement). Movement during calibration will produce inaccurate results.

VEX robots attempt to calibrate themselves automatically upon startup, waiting until they detect no motion. However, if the robot is being carried or moved during startup, the sensor may fail to calibrate properly or yield incorrect calibration.

If your project relies heavily on having an accurate heading, or if you need consistent and repeatable turns, calling `calibrate` at the beginning of your code can help. It’s good practice to display a message like “Calibrating…” on the robot’s screen during calibration, then update it to “Calibration complete.” afterward to remind you (and anyone else using the robot) that the robot must remain motionless during this period.

### calibrate

```{vexcode}
id: aim_sensing_inertial_calibrate
```

`calibrate` calibrates the gyro. Calibration is an internal procedure that measures and compensates for sensor noise and drift over a 2-second period. During this time, the robot must remain completely still (i.e., on a stable surface without any external movement). Movement during calibration will produce inaccurate results.

VEX robots attempt to calibrate themselves automatically upon startup, waiting until they detect no motion. However, if the robot is being carried or moved during startup, the sensor may fail to calibrate properly or yield incorrect calibration.

**Usage:** 

`robot.inertial.calibrate()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Calibrate the gryo before moving
robot.inertial.calibrate()
robot.screen.show_emoji(THINKING)
wait(2,SECONDS)
robot.screen.show_emoji(PROUD)
robot.move_for(50, 90)
```

### is_calibrating

```{vexcode}
id: aim_sensing_inertial_is_calibrating
```

`is_calibrating` returns a Boolean indicating whether the gyro is calibrating.

- `True` - The gyro is calibrating.
- `False` - The gyro is not calibrating.

**Usage:** `robot.inertial.is_calibrating()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Move after the calibration is completed
robot.inertial.calibrate()
while robot.inertial.is_calibrating():
    robot.screen.show_emoji(THINKING)
    wait(50, MSEC)
robot.screen.show_emoji(PROUD)
robot.move_for(50, 90)
```