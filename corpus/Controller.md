---
title: Controller | VEX AIM - Python API
description: Explore the Python API reference for the Controller buttons on a VEX AIM Onestick Controller. Find detailed descriptions for methods, parameters, and usage examples to code Controller buttons.
---

```{highlight} python
:linenothreshold: 5
```

# Controller

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

The One Stick Controller features a 4-button layout and a joystick that functions as both an analog input and a pressable button. These inputs allow the robot to detect button presses and joystick movements, enabling interactive and responsive control. Below is a list of all available methods:

**Getters – Read button, joystick, and connection status.**  
- [.pressing](#pressing) – Returns whether the specified button is being pressed.   
- [.position](#position) – Returns the position of the joystick's specified axis.
- [is_connected](#is_connected) – Returns whether the controller is connected.  
- [get_battery_level](#get_battery_level) – Returns the controller's battery level as a percentage.  

**Callbacks – Respond to button or joystick input changes.**  
- [.pressed](#pressed) – Calls a function when the specified button is pressed.  
- [.released](#released) – Calls a function when the specified button is released.  
- [.changed](#changed) – Calls a function when the joystick's axis changes.  

## Getters

### .pressing

`.pressing` returns an integer indicating whether a specific button on the controller is currently being pressed. This method must be called on a specific button object, such as `button_up` (see full list of button objects below).
- `1` - The specified button is being pressed.
- `0` - The specified button is not being pressed.

**Usage:**<br>
One of five available button objects can be used with this method, as shown below:

| button | Command |
|:-:|--|
| `button_up` | `controller.button_up.pressing()` — The **Up** button |
| `button_down` | `controller.button_down.pressing()` — The **Down** button |
| `button_left` | `controller.button_left.pressing()` — The **Left** button |
| `button_right` | `controller.button_right.pressing()` — The **Right** button |
| `button_stick` | `controller.button_stick.pressing()` — The **Joystick** button |

```{image} /_static/img/Controller/Controller-ButtonAndStickCallout.png
:alt: settings
:class: w-25
```

<!-- ![Settings](/_static/img/Controller/Controller-ButtonAndStickCallout.png) -->

| Parameters | Description |
|:-:|--|
|  | This method has no parameters. |

```python
# Move forwards while the Up button is being pressed
while True:
    if controller.button_up.pressing():
        robot.move_at(0)
    else:
        robot.stop_all_movement()  
```

### .position

```{vexcode}
id: aim_sensing_controller_axis1_position
```

```{vexcode}
id: aim_sensing_controller_axis2_position
```

`.position` returns the position of the joystick’s specified axis as an integer from –100 to 100, representing a percentage.

**Usage:**

One of two available axes can be used with this method, as shown below:

| button | Command |
|:-:|--|
| `axis1` | `controller.axis1.position()` — The vertical axis |
| `axis2` | `controller.axis2.position()` — The horizontal axis |

<!-- ![Settings](/_static/img/Controller/Controller-AxisCallout.png) -->

```{image} /_static/img/Controller/Controller-AxisCallout.png
:alt: settings
:class: w-25
```

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
while True:
    if controller.axis1.position() > 0:
        # Move forward when the joystick is moved up
        robot.move_at(0)
    else:
        # Stop moving when the joystick is centered
        robot.stop_all_movement()
```

### is_connected

```{vexcode}
id: aim_sensing_controller_is_connected
```

`is_connected` returns a Boolean indicating whether the Controller is connected.
- `True` - The Controller is connected.
- `False` - The Controller is not connected.

**Usage:**

`controller.is_connected()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Start moving forward.
# When the Controller disconnects, the robot stops.
robot.move_at(0)
while True:
    if not controller.is_connected():
        robot.stop_all_movement()
    wait(100, MSEC)  
```

### get_battery_level

```{vexcode}
id: aim_sensing_controller_get_battery_capacity
```

`get_battery_level` returns the Controller’s battery level as an integer from 0 to 100, representing a percentage.

**Usage:**

`controller.get_battery_level()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display the Controller's battery level.
robot.screen.print(controller.get_battery_level())
```

## Callbacks

### .pressed

`.pressed` registers a function to be called when a specific button on the controller is pressed. This method must be called on a specific button object, such as `button_up` – (see full list of button objects below).

**Usage:**<br>
One of five available button objects can be used with this method, as shown below:

| button | Command |
|:-:|--|
| `button_up` | `controller.button_up.pressed(callback, arg)` — The **Up** button |
| `button_down` | `controller.button_down.pressed(callback, arg)` — The **Down** button |
| `button_left` | `controller.button_left.pressed(callback, arg)` — The **Left** button |
| `button_right` | `controller.button_right.pressed(callback, arg)` — The **Right** button |
| `button_stick` | `controller.button_stick.pressed(callback, arg)` — The **Joystick** button |

<!-- ![Settings](/_static/img/Controller/Controller-ButtonAndStickCallout.png) -->

```{image} /_static/img/Controller/Controller-ButtonAndStickCallout.png
:alt: settings
:class: w-25
```

| Parameters | Description |
|:-:|--|
| callback | A [function](Logic/Functions.md) that is previously defined to execute when the specified button is being pressed. |
| arg | Optional. A tuple containing arguments to pass to the callback function. See [Using Events with Parameters](Logic/Events.md#using-events-with-parameters) for more information.|

```python
# Kick hard when Up button is pressed
def kick_object():
    robot.kicker.kick(HARD)

controller.button_up.pressed(kick_object)
```

### .released

`.released` registers a function to be called when a specific button on the controller is released. This method must be called on a specific button object, such as `button_up` – (see full list of button objects below).

**Usage:**<br>
One of five available button objects can be used with this method, as shown below:

| button | Command |
|:-:|--|
| `button_up` | `controller.button_up.released(callback, arg)` — The **Up** button |
| `button_down` | `controller.button_down.released(callback, arg)` — The **Down** button |
| `button_left` | `controller.button_left.released(callback, arg)` — The **Left** button |
| `button_right` | `controller.button_right.released(callback, arg)` — The **Right** button |
| `button_stick` | `controller.button_stick.released(callback, arg)` — The **Joystick** button |

<!-- ![Settings](/_static/img/Controller/Controller-ButtonAndStickCallout.png) -->

```{image} /_static/img/Controller/Controller-ButtonAndStickCallout.png
:alt: settings
:class: w-25
```

| Parameters | Description |
|:-:|--|
| callback | A [function](Logic/Functions.md) that is previously defined to execute when the specified button is released. |
| arg | Optional. A tuple containing arguments to pass to the callback function. See [Using Events with Parameters](Logic/Events.md#using-events-with-parameters) for more information.|

```python
# Clear the text after the Up button is released
def clear_screen():
    robot.screen.clear_screen(BLUE)

controller.button_up.released(clear_screen)

robot.screen.print("Press Up, then")
robot.screen.next_row()
robot.screen.print("Release Up!")
```

### .changed

```{vexcode}
id: aim_events_controller_axis1_changed
```

```{vexcode}
id: aim_events_controller_axis2_changed
```

`.changed` registers a function to be called when the joystick’s position changes.

<!-- ![Settings](/_static/img/Controller/Controller-AxisCallout.png)

```{image} /_static/img/Controller/Controller-AxisCallout
:alt: settings
:class: w-25
``` -->

**Usage:**<br>
One of two available axes can be used with this method, as shown below:

| button | Command |
|:-:|--|
| `axis1` | `controller.axis1.changed()` — The vertical axis |
| `axis2` | `controller.axis2.changed()` — The horizontal axis |

<!-- ![Settings](/_static/img/Controller/Controller-AxisCallout.png) -->

```{image} /_static/img/Controller/Controller-AxisCallout.png
:alt: settings
:class: w-25
```

| Parameters | Description |
|:-:|--|
| callback | A [function](Logic/Functions.md) that is previously defined to execute when the axis' value changes. |
| arg | Optional. A tuple containing arguments to pass to the callback function. See [Using Events with Parameters](Logic/Events.md#using-events-with-parameters) for more information.|

```python
# Function to display an emoji when the joystick is moved
def move_joystick():
    robot.screen.show_emoji(CONFUSED)

# Run the function when the joystick is moved up or down
controller.axis1.changed(move_joystick)
```