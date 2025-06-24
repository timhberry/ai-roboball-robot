---
title: Events | VEX AIM - Python API
description: Explore the Python API reference for handling events on a VEX AIM Coding Robot. Find detailed descriptions for creating, triggering, and managing events with examples.
---

```{highlight} python
:linenothreshold: 5
```

# Events

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

Events allow you to run functions in parallel by using event objects. Instead of calling functions or threads one after another, events let you register functions and then trigger them all at once. Each registered function runs in its own thread, so your robot can do multiple things—like blinking LEDs and driving—at the same time.

Below is a list of available methods and constructors:

- [Event](#create-an-event-object) – Creates a new event object.  
- [event](#register-functions-to-an-event) – Registers a function to the event object, optionally with arguments.  
- [broadcast](#broadcast) – Triggers all registered functions in an event object to run in parallel.  
- [broadcast_and_wait](#broadcast-and-wait) – Triggers all registered functions in an event object and waits for them to finish before continuing.  


### Create an Event Object

```{vexcode}
id: aim_events_event
```


The `Event` constructor is used to create an event object that manages function execution in separate threads.

**Usage:**<br>
`Event()`

| Parameter | description |
|:---------:|------------|
|  | This constructor has no parameters. |

```python
# Blink LEDs while moving forward
# Create move_event as an Event object
move_event = Event()

def blink_leds():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, BLACK)
        wait(0.5, SECONDS)

move_event(blink_leds)
move_event.broadcast()
robot.move_at(0)
```

### Register Functions to an Event

When you register a function to an event, it will execute in a separate thread when the event is broadcasted.

```{vexcode}
id: aim_events_event_register_function
```

**Usage:**<br>
`event(callback, args)`

| Parameter | Description |
|:---------:|-------------|
| `event`   | The name of the previously created event object. |
| `callback` | A function that is previously defined to execute when the event is broadcasted. |
| `args`    | Optional. A tuple containing arguments to pass to the callback function. See [Using Functions with Parameters](Functions.md#functions-with-parameters) for more information. |



<!-- ```python
# Blink LEDs while moving forward
move_event = Event()

def blink_leds():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, BLACK)
        wait(0.5, SECONDS)

# Register the function to the Event object
move_event(blink_leds)
move_event.broadcast()

robot.move_at(0)
``` -->

```python
# Blink LEDs while moving forward and turning
move_event = Event()

def blink_leds():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, BLACK)
        wait(0.5, SECONDS)

def turning():
    robot.turn(RIGHT)

# Register multiple functions to the Event object
move_event(blink_leds)
move_event(turning)

move_event.broadcast()
```

```python
# Move in a specified direction
move_event = Event()

def move_distance(movement_angle):
    robot.move_for(50, movement_angle)

# Change the parameter to modify how the robot moves
move_event(move_distance, (180,))
move_event.broadcast()
```

### Broadcast

```{vexcode}
id: aim_events_event_broadcast
```

`broadcast` triggers an event, starting all registered functions in separate threads. This method does not pause execution of any subsequent functions.

**Usage:**<br>
`event.broadcast()`


| parameter | description |
|:---------:|------------|
| `event`    | The name of the previously created event object. |

```python
# Blink LEDs while moving forward and turning
move_event = Event()

def blink_leds():
    while True:
        robot.led.on(ALL_LEDS, RED)
        wait(0.5, SECONDS)
        robot.led.on(ALL_LEDS, BLACK)
        wait(0.5, SECONDS)


move_event(blink_leds)

# Trigger the move_event Event
move_event.broadcast()
robot.move_at(0)
```

### Broadcast and wait

```{vexcode}
id: aim_events_event_broadcast_and_wait
```

`broadcast_and_wait` starts an event but waits for all registered functions to finish before continuing with subsequent functions.

**Usage:**<br>
`event.broadcast_and_wait()`

| parameter | description |
|:---------:|------------|
| `event`    | The name of the previously created event object. |

```python
# Move after the screen is pressed
move_event = Event()

def move_and_turn():
    robot.move_for(50, 0)
    robot.turn_for(RIGHT, 90)

move_event(move_and_turn)

while True:
    if robot.screen.pressing():
        move_event.broadcast_and_wait()
        break
robot.screen.print("Movement done.")
```