---
title: LED | VEX AIM - Python API
description: Explore the Python API reference for the LEDs on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to control the LEDs.
---

```{highlight} python
:linenothreshold: 5
```

# LED

```{contents}
:local: true
```

## Introduction

The VEX AIM Coding Robot features programmable LEDs (Light-Emitting Diodes) that can change color based on conditions in a project. These LEDs can be set individually or all at once to provide visual feedback or indicate robot status.

LED Names:

| ![A top down icon of the robot with a fan emerging from the location of the LED at the 11 o’clock position.](/_static/img/LEDs/1.png)<br>`LED1` | ![A top down icon of the robot with a fan emerging from the location of the LED at the 9 o’clock position.](/_static/img/LEDs/2.png)<br>`LED2` | ![A top down icon of the robot with a fan emerging from the location of the LED at the 7 o’clock position.](/_static/img/LEDs/3.png)<br>`LED3` |
|:--:|:--:|:--:|
| ![A top down icon of the robot with a fan emerging from the location of the LED at the 5 o’clock position.](/_static/img/LEDs/4.png)<br>`LED4` | ![A top down icon of the robot with a fan emerging from the location of the LED at the 3 o’clock position.](/_static/img/LEDs/5.png)<br>`LED5` | ![A top down icon of the robot with a fan emerging from the location of the LED at the 1 o’clock position.](/_static/img/LEDs/6.png)<br>`LED6` |
| ![A top down icon of the robot with fans emerging from the location of all six LEDs, clockwise at 1, 3, 5, 7, 9 and 11 o’clock positions.](/_static/img/LEDs/all.png)<br>`ALL_LEDS` |  |

- [on](#on) – Turns one or all LEDs on and sets their color. 
- [off](#off) – Turns one or all LEDs off. 


## Actions

### on

```{vexcode}
id: aim_looks_robot_led_on
```

```{vexcode}
id: aim_looks_robot_led_on_color
```

`on` sets the color of one or all of the robot's LEDs.

**Usage:**<br>
`robot.led.on(led, color)`

| Parameter | Description |
|:--------:|-------------|
| `led` | The LED or LEDs to turn on. You can use a single LED like `LED1`, all LEDs with `ALL_LEDS`, or a group of LEDs in a tuple like `(LED1, LED2)`. See all available LED names [here].(#introduction). |
| `color` | Optional. Sets the LED color. Options include: <ul><li>`BLACK`</li><li>`BLUE`</li><li>`CYAN`</li><li>`GREEN`</li><li>`ORANGE`</li><li>`PURPLE`</li><li>`RED`</li><li>`TRANSPARENT`</li><li>`WHITE` (default)</li><li>`YELLOW`</li></ul> You can also specify a [custom color](Logic/Color_objects.md). |


```python
# Turn LEDs green while the screen is pressed
while True:
    if robot.screen.pressing():
        robot.led.on(ALL_LEDS, GREEN)
    else: 
        robot.led.on(ALL_LEDS, BLACK)

    wait(50, MSEC)
```

```python
# Turn two LEDs red
robot.led.on((LED3, LED4), RED)
```

### off

```{vexcode}
id: aim_looks_robot_led_off
```

`off` turns off one or all of the robot's LEDs.

**Usage:**<br>
`robot.led.off(led)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `led` | The LED or LEDs to turn off. You can use a single LED like `LED1`, all LEDs with `ALL_LEDS`, or a group of LEDs in a tuple like `(LED1, LED2)`. See all available LED names [here].(#introduction). |


```python
# Turn the LEDs on for 2 seconds.
robot.led.on(ALL_LEDS)
wait(2, SECONDS)
robot.led.off(ALL_LEDS)
```

```python
# Turn off half the LEDs
robot.led.on(ALL_LEDS)
wait(1, SECONDS)
robot.led.off((LED3, LED4, LED5))
```