---
title: Sound | VEX AIM - Python API
description: Explore the Python API reference for the sounds on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to play built-in and custom sounds.
---

```{highlight} python
:linenothreshold: 5
```

# Sound

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

The VEX AIM Coding Robot's sounds allow users to play built-in sounds, custom audio files, and musical notes. It also includes controls for stopping sounds and detecting if audio is currently playing. Below is a list of all available methods:

**Actions – Play or stop sounds.**  
- [play](#play) – Plays a built-in sound effect.  
- [play_file](#play_file) – Plays a user-uploaded custom sound.  
- [play_note](#play_note) – Plays a musical note for a set duration.  
- [stop](#stop) – Stops any currently playing sound.  

**Getter – Check sound status.**  
- [is_active](#is_active) – Returns whether a sound is currently playing.  

## Actions

### play

```{vexcode}
id: aim_sound_robot_sound_play
```

`play` plays one of the robot's built-in sounds at a specified volume percentage. Since this is a non-waiting method, the robot plays the built-in sound and moves to the next command without waiting for it to finish.

**Usage:**

`robot.sound.play(sound, volume)`

| Parameter | Description |
|:--|:--|
| `sound` | One of the built-in sound options listed below. |
| `volume` | Optional. The volume for the sound, as an integer from 0 to 100 percent. The default is 50 percent. |

| Built-In Sounds    | Play Sound                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------|
| `ACT_ANGRY`        | <button onclick="(new Audio('../../_static/audio/aim/act_angry.mp3')).play()">Play</button>   |
| `ACT_EXCITED`      | <button onclick="(new Audio('../../_static/audio/aim/act_excited.mp3')).play()">Play</button> |
| `ACT_HAPPY`        | <button onclick="(new Audio('../../_static/audio/aim/act_happy.mp3')).play()">Play</button>   |
| `ACT_SAD`          | <button onclick="(new Audio('../../_static/audio/aim/act_sad.mp3')).play()">Play</button>     |
| `ACT_SILLY`        | <button onclick="(new Audio('../../_static/audio/aim/act_silly.mp3')).play()">Play</button>   |
| `BLINKER`          | <button onclick="(new Audio('../../_static/audio/aim/blinker.mp3')).play()">Play</button>     |
| `BRAKES`           | <button onclick="(new Audio('../../_static/audio/aim/brakes.mp3')).play()">Play</button>      |
| `CHEER`            | <button onclick="(new Audio('../../_static/audio/aim/cheer.mp3')).play()">Play</button>       |
| `CHIRP`            | <button onclick="(new Audio('../../_static/audio/aim/chirp.mp3')).play()">Play</button>       |
| `COMPLETE`         | <button onclick="(new Audio('../../_static/audio/aim/complete.mp3')).play()">Play</button>    |
| `CRASH`            | <button onclick="(new Audio('../../_static/audio/aim/crash.mp3')).play()">Play</button>       |
| `DETECTED`         | <button onclick="(new Audio('../../_static/audio/aim/detected.mp3')).play()">Play</button>    |
| `DOORBELL`         | <button onclick="(new Audio('../../_static/audio/aim/doorbell.mp3')).play()">Play</button>    |
| `FAIL`             | <button onclick="(new Audio('../../_static/audio/aim/fail.mp3')).play()">Play</button>        |
| `FLOURISH`         | <button onclick="(new Audio('../../_static/audio/aim/flourish.mp3')).play()">Play</button>    |
| `HUAH`             | <button onclick="(new Audio('../../_static/audio/aim/huah.mp3')).play()">Play</button>        |
| `LOOPING`          | <button onclick="(new Audio('../../_static/audio/aim/looping.mp3')).play()">Play</button>     |
| `MOVE_FORWARD`     | <button onclick="(new Audio('../../_static/audio/aim/forward.mp3')).play()">Play</button>     |
| `MOVE_REVERSE`     | <button onclick="(new Audio('../../_static/audio/aim/reverse.mp3')).play()">Play</button>     |
| `OBSTACLE`         | <button onclick="(new Audio('../../_static/audio/aim/obstacle.mp3')).play()">Play</button>    |
| `PAUSE`            | <button onclick="(new Audio('../../_static/audio/aim/pause.mp3')).play()">Play</button>       |
| `PICKUP`           | <button onclick="(new Audio('../../_static/audio/aim/pickup.mp3')).play()">Play</button>      |
| `RECEIVE`          | <button onclick="(new Audio('../../_static/audio/aim/receive.mp3')).play()">Play</button>     |
| `RESUME`           | <button onclick="(new Audio('../../_static/audio/aim/resume.mp3')).play()">Play</button>      |
| `SENSING`          | <button onclick="(new Audio('../../_static/audio/aim/sensing.mp3')).play()">Play</button>     |
| `SEND`             | <button onclick="(new Audio('../../_static/audio/aim/send.mp3')).play()">Play</button>        |
| `SPARKLE`          | <button onclick="(new Audio('../../_static/audio/aim/sparkle.mp3')).play()">Play</button>     |
| `TADA`             | <button onclick="(new Audio('../../_static/audio/aim/tada.mp3')).play()">Play</button>        |
| `TURN_LEFT`        | <button onclick="(new Audio('../../_static/audio/aim/left.mp3')).play()">Play</button>        |
| `TURN_RIGHT`       | <button onclick="(new Audio('../../_static/audio/aim/right.mp3')).play()">Play</button>       |

```python
# Play cheer
robot.sound.play(CHEER)
```

```python
# Play cheer at full volume
robot.sound.play(CHEER, 100)
```

```python
# Wait until sound is finished to move
robot.sound.play(ACT_HAPPY)
while robot.sound.is_active():
    wait(50, MSEC)
robot.turn_to(180)
```

### play_file

```{vexcode}
id: aim_sound_robot_sound_play_file
```

`play_file` plays a custom sound uploaded by the user. Since this is a non-waiting method, the robot plays the custom sound and moves to the next command without waiting for it to finish.


**Usage:**

`robot.sound.play_file(file, volume)`

| Parameter | Description |
|:--|:--|
| `file` | One of the custom sound files uploaded by the user, from `SOUND1` to `SOUND10`. The sound number matches the number shown in the AIM control panel. |
| `volume` | Optional. The volume for the sound, as an integer from 0 to 100 percent. The default is 50 percent. |


```python
# Play an uploaded sound
robot.sound.play_file(SOUND1)
```

```python
# Play an uploaded sound at full volume
robot.sound.play_file(SOUND1, 100)
```

```python
# Wait until sound is finished to move
robot.sound.play_file(SOUND1)
while robot.sound.is_active():
    wait(50, MSEC)
robot.turn_to(180)
```

### play_note

```{vexcode}
id: aim_sound_robot_sound_play_note
```

`play_note` plays a specific note for a specific duration in milliseconds. Since this is a non-waiting method, the robot plays the specific note and moves to the next command without waiting for it to finish.

**Usage:**

`robot.sound.play_note(note, length, volume)`

<!-- | Parameters       | Description           |
|:------------------: | :----------------------------------|
| note | Defines the musical pitch: `C5`, `C#5`, `D5`, `D#5`, `E5`, `F5`, `F#5`, `G5`, `G#5`, `A5`, `A#5`, `B5`, `C6`, `C#6`, `D6`, `D#6`, `E6`, `F6`, `F#6`, `G6`, `G#6`, `A6`, `A#6` and `B6` as a string. |
| length | Sets the length of the note as an integer in milliseconds (ms). |
| volume | Optional. The volume of the specified sound as an integer percentage from 0 to 100. The default is 50 percent. | -->

| Parameter | Description |
|:--|:--|
| `note` | The musical pitch to play, written as a string (e.g., `C5`, `A#6`). Valid notes are `A` through `G` (with optional `#` for sharps) across octaves 5 to 8. |
| `length` | The duration of the note, given as an integer in milliseconds. |
| `volume` | Optional. The volume of the note, as an integer from 0 to 100 percent. The default is 50 percent. |

```python
# Play C5 for 2 seconds
robot.sound.play_note("C5", 2000)
```

```python
# Play C5 for 2 seconds at full volume
robot.sound.play_note("C5", 2000, 100)
```

```python
# Wait until note is finished to move
robot.sound.play_note("C6", 1000)
while robot.sound.is_active():
    wait(50, MSEC)
robot.turn_to(180)
```

### stop

```{vexcode}
id: aim_sound_robot_sound_stop
```

`stop` stops a sound that is currently playing.

**Usage:**

`robot.sound.stop()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Cut a sound off after 1 second
robot.sound.play(ACT_SILLY)
wait(1, SECONDS)
robot.sound.stop()
```

## Getters

### is_active

```{vexcode}
id: aim_sensing_robot_sound_is_active
```

`is_active` returns a Boolean indicating whether a sound is currently playing.
- `True` – A sound is currently playing
- `False` – No sound is playing

**Usage:**

`robot.sound.is_active()`

| Parameters | Description |
|:-|--|
|  | This method has no parameters. |

```python
# Play tada after cheer finishes
robot.sound.play(CHEER)   
while robot.sound.is_active():
    wait(10, MSEC)
robot.sound.play(TADA)
```