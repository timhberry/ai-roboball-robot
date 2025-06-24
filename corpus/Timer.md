---
title: Timer | VEX AIM - Python API
description: Explore the Python API reference for the timer on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to code the robot's timer.
---

```{highlight} python
:linenothreshold: 5
```

# Timer

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

The VEX AIM Coding Robot's timer keeps track of elapsed time from the start of a project. It can be used to measure durations, trigger events after a set time, or reset for new timing operations. Below is a list of all available methods:

**Action – Control the timer.**
- [reset](#reset) – Resets the timer to zero.

**Getter – Return the current timer value.**
- [time](#time) – Returns the elapsed time since the project started.

**Callback – Trigger functions after a delay.**
- [event](#event) – Calls a function after a specified number of milliseconds, with optional arguments.

**Constructor - Create a Timer to track time.**
- [Timer](#timer) - Create a new timer object that can be used with these methods.

## Action

### reset

```{vexcode}
id: aim_sensing_robot_timer_reset
```

`reset` sets the timer to zero.

**Usage:**

`timer.reset()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Display how long a turn takes
robot.move_for(100, 0)
timer.reset()
robot.turn_for(RIGHT, 90)
robot.screen.print("Time elapsed:")
robot.screen.next_row()
robot.screen.print("%d seconds" % timer.time(SECONDS))
```

## Getter

### time

```{vexcode}
id: aim_sensing_robot_timer_time
```

`time` returns the current elapsed time of the timer in the specified units — an integer for `MSEC` or a float for `SECONDS`.

**Usage:**

`timer.time(units)`

| Parameters | Description |
|:-:|--|
| `units` | The time units are milliseconds `MSEC` (default) or `SECONDS`. |


```python   
# Print the time in seconds
# and in milliseconds on the next row.
while timer.time(SECONDS) <= 5:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    robot.screen.print("Time: %d" % timer.time(MSEC))
    robot.screen.next_row()
    robot.screen.print("Time: %.2f" % timer.time(SECONDS))
    wait(50, MSEC)
```


## Callback

### event

```{vexcode}
id: aim_events_robot_timer_event
```

`event` calls a function after a specified amount of time.

**Usage:**

`timer.event(callback, delay, arg)`

| Parameters | Description |
|:-:|--|
| `callback` | A function to execute when the timer event occurs. |
| `delay` | The delay before the function is called, in milliseconds. |
| `arg` | Optional. A tuple containing arguments to pass to the callback function. See [Using Events with Parameters](Events.md#using_events_with_parameters) for more information.|

```python
# Create a function to play a sparkle sound
def timer_callback():
    robot.sound.play(SPARKLE)

# Call the function after 2000 milliseconds (2 seconds)
timer.event(timer_callback, 2000)
```

## Constructor

### Timer

```{vexcode}
id: aim_logic_timer_new_timer
```

A new timer can be created using the `Timer` constructor. A new timer starts measuring time immediately when it is created.

**Usage:**<br>
`Timer()`

| Parameter | Description |
|:---------:|:------------|
|    | This constructor has no parameters. |

```python
## Display 2 timers with a 2 second difference
wait(2, SECONDS)

stopwatch = Timer()

while True:
    robot.screen.clear_screen()

    robot.screen.set_cursor(1, 1)
    robot.screen.print("Timer:")
    robot.screen.set_cursor(2, 1)
    robot.screen.print(timer.time(SECONDS))

    robot.screen.set_cursor(4, 1)
    robot.screen.print("Stopwatch:")
    robot.screen.set_cursor(5, 1)
    robot.screen.print(stopwatch.time(SECONDS))

    wait(0.1, SECONDS)
```