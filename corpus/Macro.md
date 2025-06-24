---
title: Macro | VEX AIM - Python API
description: Explore the Python API reference for prebuilt actions, also known as macros, on a VEX AIM Coding Robot. Find a description of prebuilt sets of methods that can be used to display emotions and move the robot.
---

```{highlight} python
:linenothreshold: 5
```

# Macro

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

The VEX AIM Coding Robot includes prebuilt macros—groups of commands bundled into reusable code sequences. Each macro performs a full behavior, such as expressing an emotion or using the AI Vision Sensor to find and approach an object. Below is a list of available macros:

**Emotions – Make the robot act expressively.**  
- [act_happy](#act-happy) – Makes the robot act happy.  
- [act_sad](#act-sad) – Makes the robot act sad.  
- [act_silly](#act-silly) – Makes the robot act silly.  
- [act_angry](#act-angry) – Makes the robot act angry.  
- [act_excited](#act-excited) – Makes the robot act excited.  

**AI Vision (Sports Ball) – Turn toward and get sports balls.**  
- [turn_right_until_sports_ball](#turn-right-until-sports-ball) – Turns right until a sports ball is detected.  
- [turn_left_until_sports_ball](#turn-left-until-sports-ball) – Turns left until a sports ball is detected.  
- [get_sports_ball](#get-sports-ball) – Moves to collect a sports ball.  

**AI Vision (Orange Barrel) – Turn toward and get orange barrels.**  
- [turn_right_until_orange_barrel](#turn-right-until-orange-barrel) – Turns right until an orange barrel is detected.  
- [turn_left_until_orange_barrel](#turn-left-until-orange-barrel) – Turns left until an orange barrel is detected.  
- [get_orange_barrel](#get-orange-barrel) – Moves to collect an orange barrel.  

**AI Vision (Blue Barrel) – Turn toward and get blue barrels.**  
- [turn_right_until_blue_barrel](#turn-right-until-blue-barrel) – Turns right until a blue barrel is detected.  
- [turn_left_until_blue_barrel](#turn-left-until-blue-barrel) – Turns left until a blue barrel is detected.  
- [get_blue_barrel](#get-blue-barrel) – Moves to collect a blue barrel.  

**AI Vision (AIM Robot) – Turn and move toward other AIM robots.**  
- [turn_right_until_aim_robot](#turn-right-until-aim-robot) – Turns right until another AIM Robot is detected.  
- [turn_left_until_aim_robot](#turn-left-until-aim-robot) – Turns left until another AIM Robot is detected.  
- [move_to_aim_robot](#move-to-aim-robot) – Moves toward another AIM Robot.  

**AI Vision (AprilTag) – Turn and move toward AprilTags.**  
- [turn_right_until_april_tag](#turn-right-until-apriltag) – Turns right until AprilTag is detected.  
- [turn_left_until_april_tag](#turn-left-until-apriltag) – Turns left until AprilTag is detected.  
- [move_to_april_tag](#move-to-apriltag) – Moves toward AprilTag.  

## Emotions

### act happy

```{vexcode}
id: aim_actions_robot_act_happy
```

This set of methods makes the robot act happy.

```python
# act happy
robot.screen.show_emoji(HAPPY)
wait(.5,SECONDS)
robot.sound.play(ACT_HAPPY)
wait(115, MSEC)

robot.screen.show_emoji(HAPPY, LOOK_RIGHT)
robot.led.on(ALL_LEDS, YELLOW)
robot.turn_for(RIGHT, 4, 100)
robot.led.on(ALL_LEDS, WHITE)
robot.screen.show_emoji(HAPPY, LOOK_LEFT)
robot.turn_for(RIGHT, -8, 100)
robot.led.on(ALL_LEDS, YELLOW)
robot.screen.show_emoji(HAPPY, LOOK_RIGHT)
robot.turn_for(RIGHT, 4, 100)

wait(100,MSEC)
for i in range(3):
    robot.screen.show_emoji(QUIET)
    robot.led.on(ALL_LEDS, WHITE)
    robot.move_for(1,-90)
    robot.screen.show_emoji(HAPPY)
    robot.led.on(ALL_LEDS, YELLOW)
    robot.move_for(1,90)

robot.stop_all_movement()
robot.led.off(ALL_LEDS)
wait(.5,SECONDS)
```

### act sad

```{vexcode}
id: aim_actions_robot_act_sad
```

This set of methods makes the robot act sad.

```python
# act sad
robot.screen.show_emoji(SAD)
wait(.5,SECONDS)
robot.sound.play(ACT_SAD)
wait(115, MSEC)

robot.led.on(ALL_LEDS, Color(0, 0, 250))
robot.screen.show_emoji(SAD, LOOK_RIGHT)
robot.move_for(11, 135, 70)
robot.led.on(ALL_LEDS, Color(0, 0, 100))
robot.screen.show_emoji(SAD, LOOK_FORWARD)
robot.move_for(11, 315, 70)
robot.led.on(ALL_LEDS, Color(0, 0, 50))
robot.screen.show_emoji(SAD, LOOK_LEFT)
robot.move_for(11, 225, 70)
robot.led.on(ALL_LEDS, Color(0, 0, 10))
robot.screen.show_emoji(SAD, LOOK_FORWARD)
robot.move_for(11, 45, 70)
wait(.5,SECONDS)
robot.led.off(ALL_LEDS)
```

### act silly

```{vexcode}
id: aim_actions_robot_act_silly
```

This set of methods makes the robot act silly.

```python
# act silly
robot.screen.show_emoji(SILLY)
wait(.5,SECONDS)
robot.sound.play(ACT_SILLY)
wait(115,MSEC)

robot.turn_for(RIGHT, 360, 100, wait=False)
face_list = [SILLY, HAPPY, EXCITED, PROUD, THRILLED, LAUGHING]
colors = [BLUE, CYAN, GREEN, ORANGE, PURPLE, RED, WHITE, YELLOW]

while robot.is_turn_active():
    robot.screen.show_emoji(SILLY)
    robot.led.on(ALL_LEDS, random.choice(colors))
    wait(110,MSEC)
    robot.screen.show_emoji(random.choice(face_list))
    wait(110,MSEC)

robot.screen.show_emoji(SILLY)
robot.led.off(ALL_LEDS)
wait(.5,SECONDS)
```

### act angry

```{vexcode}
id: aim_actions_robot_act_angry
```

This set of methods makes the robot act angry.

```python
# act angry
robot.screen.show_emoji(ANGRY)
wait(.5,SECONDS)
robot.sound.play(ACT_ANGRY)
wait(115,MSEC)

robot.led.on(ALL_LEDS, RED)
robot.move_for(25, 0, 50)
wait(50,MSEC)

for i in range(5):
    robot.screen.show_emoji(ANNOYED)
    robot.move_for(5, 180, 50)
    robot.screen.show_emoji(ANGRY)
    wait(50,MSEC)

wait(.5,SECONDS)
robot.led.off(ALL_LEDS)
```

### act excited

```{vexcode}
id: aim_actions_robot_act_excited
```

This set of methods makes the robot act excited.

```python
# act excited
robot.screen.show_emoji(EXCITED)
wait(.5,SECONDS)
robot.sound.play(ACT_EXCITED)
wait(115, MSEC)

for angle in [3,-3,2,-2,2,-2,2,-2,1,-1]:
    if angle > 0:
        robot.screen.show_emoji(EXCITED, LOOK_RIGHT)
        robot.led.on(LED4, ORANGE)
        robot.led.on(LED5, ORANGE)
        robot.led.on(LED6, ORANGE)
        robot.led.off(LED1)
    else:
        robot.screen.show_emoji(EXCITED, LOOK_LEFT)
        robot.led.on(LED1, ORANGE)
        robot.led.on(LED2, ORANGE)
        robot.led.on(LED3, ORANGE)
        robot.led.off(LED6)
    robot.turn_for(RIGHT, angle)
    robot.led.off(ALL_LEDS)

robot.screen.show_emoji(EXCITED, LOOK_FORWARD)
wait(.5,SECONDS)
```

## AI Vision (Sports Ball)

### turn right until sports ball

```{vexcode}
id: aim_robot_turn_right_sports_ball
```

This set of methods makes the robot turn right until the AI Vision Sensor detects a sports ball.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md/#set_turn_velocity).

```python
# Turn right until sports ball is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(SPORTS_BALL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### turn left until sports ball

```{vexcode}
id: aim_robot_turn_left_sports_ball
```

This set of methods makes the robot turn left until the AI Vision Sensor detects a sports ball.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn left until sports ball is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(SPORTS_BALL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### get sports ball

```{vexcode}
id: aim_robot_get_object
```

This set of methods makes the robot move to collect a sports ball.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's move and turn velocities with [set_move_velocity](Motion.md#set_move_velocity) and [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Get sports ball
while True:
    vision_data = robot.vision.get_data(SPORTS_BALL)

    if vision_data[0].exists:
        if robot.has_sports_ball():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)
```

## AI Vision (Orange Barrel)

### turn right until orange barrel

```{vexcode}
id: aim_robot_turn_right_orange_barrel
```

This set of methods makes the robot turn right until the AI Vision Sensor detects an orange barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn right until orange barrel is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(ORANGE_BARREL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### turn left until orange barrel

```{vexcode}
id: aim_robot_turn_left_sports_ball
```

This set of methods makes the robot turn left until the AI Vision Sensor detects an orange barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn left until orange barrel is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(ORANGE_BARREL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### get orange barrel

```{vexcode}
id: aim_robot_get_object_orange_barrel
```

This set of methods makes the robot move to collect an orange barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's move and turn velocities with [set_move_velocity](Motion.md#set_move_velocity) and [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Get orange barrel
while True:
    vision_data = robot.vision.get_data(ORANGE_BARREL)

    if vision_data[0].exists:
        if robot.has_orange_barrel():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)
```

## AI Vision (Blue Barrel)

### turn right until blue barrel

```{vexcode}
id: aim_robot_turn_right_blue_barrel
```

This set of methods makes the robot turn right until the AI Vision Sensor detects a blue barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn right until blue barrel is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### turn left until blue barrel

```{vexcode}
id: aim_robot_turn_left_blue_barrel
```

This set of methods makes the robot turn left until the AI Vision Sensor detects a blue barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn left until blue barrel is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### get blue barrel

```{vexcode}
id: aim_robot_get_object_blue_barrel
```

This set of methods makes the robot move to collect a blue barrel.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's move and turn velocities with [set_move_velocity](Motion.md#set_move_velocity) and [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Get blue barrel
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data[0].exists:
        if robot.has_blue_barrel():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)
```

## AI Vision (AIM Robot)

### turn right until AIM robot

```{vexcode}
id: aim_robot_turn_right_aim_robot
```

This set of methods makes the robot turn right until the AI Vision Sensor detects a VEX AIM Coding Robot.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn right until AIM robot is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(AIM_ROBOT)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### turn left until AIM robot

```{vexcode}
id: aim_robot_turn_left_aim_robot
```

This set of methods makes the robot turn left until the AI Vision Sensor detects a VEX AIM Coding Robot.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn left until AIM robot is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(AIM_ROBOT)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### move to AIM robot

```{vexcode}
id: aim_robot_move_to_aim_robot
```

This set of methods makes the robot move towards a VEX AIM Coding Robot.

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's move and turn velocities with [set_move_velocity](Motion.md#set_move_velocity) and [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Move to AIM robot
while True:
    vision_data = robot.vision.get_data(AIM_ROBOT)

    if vision_data[0].exists:
        if vision_data[0].width >= 140:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)
```

## AI Vision (AprilTag)

### turn right until AprilTag

```{vexcode}
id: aim_robot_turn_right_april_tag
```

This set of methods makes the robot turn right until the AI Vision Sensor detects AprilTag ID 0. To change which AprilTag the robot will turn until, replace the `0` in `TAG0` with any number from `0` to `37` (AprilTags 5 through 37 can be used with printed AprilTags from [AIM Printables](https://kb.vex.com/hc/en-us/articles/4410295384980-VEX-Printables#aim-printables-header-9).)

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn right until AprilTag ID 0 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### turn left until AprilTag

```{vexcode}
id: aim_robot_turn_left_april_tag
```

This set of methods makes the robot turn left until the AI Vision Sensor detects AprilTag ID 0. To change which AprilTag the robot will turn until, replace the `0` in `TAG0` with any number from `0` to `37` (AprilTags 5 through 37 can be used with printed AprilTags from [AIM Printables](https://kb.vex.com/hc/en-us/articles/4410295384980-VEX-Printables#aim-printables-header-9).)

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's turn velocity with [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Turn left until AprilTag ID 0 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data[0].exists:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)
```

### move to AprilTag

```{vexcode}
id: aim_robot_move_to_april_tag
```

This set of methods makes the robot move towards AprilTag ID 0. To change which AprilTag the robot will move to, replace the `0` in `TAG0` with any number from `0` to `37` (AprilTags 5 through 37 can be used with printed AprilTags from [AIM Printables](https://kb.vex.com/hc/en-us/articles/4410295384980-VEX-Printables#aim-printables-header-9).)

**Note**: If the robot appears to be having difficulties with detecting objects, try lowering the robot's move and turn velocities with [set_move_velocity](Motion.md#set_move_velocity) and [set_turn_velocity](Motion.md#set_turn_velocity).

```python
# Move to AprilTag ID 0
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data[0].exists:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)
```