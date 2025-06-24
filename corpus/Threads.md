---
title: Threads | VEX AIM - Python API
description: Explore the Python API reference for threads on a VEX AIM Coding Robot. Find detailed descriptions for thread functions, usage, and examples.
---


```{highlight} python
:linenothreshold: 5
```

# Threads

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

Threads allow a robot to run multiple tasks simultaneously within the same program. They enable multitasking, letting the robot perform independent actions at the same time.

**Note:** You must [first define a function](Functions.md) to use it with a thread.

**Constructor – Create and start new threads.**  
- [Thread](#thread) – Starts a new thread that runs the specified function in parallel with the main program.

**Action – Control running threads.**  
- [stop](#stop) – Stops a thread manually, useful for halting background behavior.

## Constructor

### Thread

`Thread` creates and starts a thread. When you create a thread, you can name it to manage it individually in your project.

**Usage:**

`my_thread = Thread(my_function)`

| Parameters  | Description     |
|:---------: | :---------------------------|
| `my_thread`  | Optional. A name for the new thread.  |
| `my_function`  | The name of a previously defined function.   |

**Note:** A function must **always be defined *before*** it is called.

```python
# Drive forward while blinking lights
def blink_lights():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, BLUE)
        wait(0.5, SECONDS)
blink_lights_thread = Thread(blink_lights)
robot.move_at(0)
```

```python
# Run multiple threads simultaneously
# Turn right, blink lights and display heading at once
def blink_lights():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, GREEN)
        wait(0.5, SECONDS)

def display_heading():
    while True:
        robot.screen.clear_row()
        robot.screen.set_cursor(1, 1)
        robot.screen.print(f"Heading: {robot.inertial.get_yaw()}")
        wait(50, MSEC)

blink_lights_thread = Thread(blink_lights)     
display_heading_thread = Thread(display_heading)
robot.turn(RIGHT)
```
## Action

### stop

`stop` stops a thread manually, which is useful when a task is no longer needed or when a program needs to reset or reassign threads. Once a thread is stopped, it cannot be restarted. To run it again, you must create a new thread using [`Thread`](#thread).

**Usage:**

`my_thread.stop()`

| Parameters | Description |
|:-|--|
| `my_thread`  | A previously started thread object. This is the name assigned when the thread was created using `Thread`.  |

```python
"""
Run multiple threads simultaneously
Turn right, blink lights and display heading at once
Stop blinking lights after 2 seconds
"""
def blink_lights():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.off(ALL_LEDS)
        wait(0.5, SECONDS)

def display_heading():
    while True:
        robot.screen.clear_row()
        robot.screen.set_cursor(1, 1)
        robot.screen.print(f"Heading: {robot.inertial.get_yaw()}")
        wait(50, MSEC)

blink_lights_thread = Thread(blink_lights)     
display_heading_thread = Thread(display_heading)
robot.turn(RIGHT)

wait(2, SECONDS)
blink_lights_thread.stop()
```