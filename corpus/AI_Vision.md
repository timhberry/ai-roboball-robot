---
title: AI Vision | VEX AIM - Python API
description: Explore the Python API reference for the AI Vision Sensor on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples.
---

```{highlight} python
:linenothreshold: 5
```

# AI Vision

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

The VEX AIM Coding Robot's AI Vision Sensor detects and tracks objects, colors, and AprilTags. This allows the robot to analyze its surroundings, follow objects, and react based on detected visual data. Below is a list of all available methods and properties:

**Actions – Show or hide the AI Vision camera feed.**  
- [show_aivision](#show_aivision) – Displays the AI Vision feed on the robot’s screen.  
- [hide_aivision](#hide_aivision) – Hides the AI Vision feed from the screen.  
- [tag_detection](#tag_detection) – Turns AprilTag detection on or off.  

**Getters – Detect if the robot is holding an object.**  
- [get_data](#get_data) – Returns a tuple of detected objects based on a given signature.  
- [has_sports_ball](#has_sports_ball) – Returns whether the robot has a sports ball.  
- [has_any_barrel](#has_any_barrel) – Returns whether the robot has any type of barrel.  
- [has_blue_barrel](#has_blue_barrel) – Returns whether the robot has a blue barrel.  
- [has_orange_barrel](#has_orange_barrel) – Returns whether the robot has an orange barrel.  

**Properties – Object data returned from [get_data](#get_data).**  
- [exists](#exists) – Whether the object exists in the current detection as a Boolean.  
- [width](#width) – Width of the detected object in pixels.  
- [height](#height) – Height of the detected object in pixels.  
- [centerX](#centerx) – X position of the object’s center in pixels.  
- [centerY](#centery) – Y position of the object’s center in pixels.  
- [bearing](#bearing) – Horizontal angle relative to the front of the robot in degrees.  
- [rotation](#rotation) – Orientation of the object in degrees.  
- [originX](#originx) – X position of the object’s top-left corner in pixels.  
- [originY](#originy) – Y position of the object’s top-left corner in pixels.  
- [id](#id) – Classification or tag ID of the object.  
- [score](#score) – Confidence score for AI Classifications (1–100).
- [type](#type) – Returns the object’s type (AI, Tag, Color, or Code).  

**Constructors – Define color signatures and codes.**
- [Create a Color Signature](#creating-a-color-signature) – Creates a new Color Signature based on RGB and hue/saturation ranges.  
- [Create a Color Code](#creating-a-color-code) – Combines multiple Color Signatures into a single Color Code.

## Actions

### show_aivision

```{vexcode}
id: aim_looks_robot_screen_show_aivision
```

`show_aivision` displays the AI Vision Sensor’s live data feed on the robot’s screen. The live data feed will cover any other images or text on the screen.

**Note:** The screen will not display any other images or text unless [hide_aivision](#hide_aivision) is used to hide the feed.

**Usage:**<br>
`robot.screen.show_aivision()`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |

```python
# Watch the AI Vision Sensor detect AI Classifications
# and AprilTags as you move the robot
robot.screen.show_aivision()
```

<!-- while True:
    ai_objects = robot.take_snapshot(AiVision.ALL_AIOBJS)
    if ai_objects[0].exists:
        robot.move_for(10,0)
    wait(10,MSEC) -->

### hide_aivision

```{vexcode}
id: aim_looks_robot_screen_hide_aivision
```

`hide_aivision` removes the AI Vision Sensor’s live data feed from the robot’s screen.

**Usage:**<br>
`robot.screen.hide_aivision()`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |

```python
# View the AI Vision Sensor's feed for five seconds
robot.screen.show_aivision()
wait(5, SECONDS)
robot.screen.hide_aivision()
```

<!-- ```python
# Hide a message with the AI Vision Sensor's feed
robot.screen.print("I will hide.")
wait(2, SECONDS)
robot.screen.show_aivision()
wait(2, SECONDS)
robot.screen.hide_aivision()
``` -->

<!-- ```python
# Display AI Vision video feed on the screen
robot.screen.show_aivision()
while True:
    # Take a snapshot of an Orange Barrel
    ai_objects = robot.take_snapshot(AiVision.ORANGE_BARREL)
    if ai_objects[0].exists:
        # If the object is in the center on the field of view, stop turning
        if 140 < ai_objects[0].centerX < 180:
            break
    wait(10,MSEC)
wait(2, SECONDS)
# Hide AI Vision video feed to print text
robot.screen.hide_aivision()
robot.screen.print("Found object")
``` -->

### tag_detection

```{vexcode}
id: aim_looks_robot_screen_tag_detection
```

`tag_detection` enables or disables the AprilTag detection, where the state is a Boolean value.

The sensor can detect AprilTag IDs 0 to 36 from the Circle21h7 family.

**Usage:**<br>
`robot.vision.tag_detection(state)`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
| `state` | Values are: <ul><li>`True` Enables AprilTag detection.</li> <li>`False` Disables AprilTag detection.</li></ul> |

```python
robot.screen.set_font(PROP30)

# Cut off APrilTag detection after 5 seconds
while True:
    if robot.timer.time(SECONDS) > 5:
        robot.vision.tag_detection(False)

    robot.screen.clear_screen()
    robot.screen.set_cursor(3, 1)
    apriltags = robot.vision.get_data(ALL_TAGS)
    
    if apriltags:
        robot.screen.print("AprilTag detected!")
    else:
        robot.screen.print("Nothing detected!")

    wait(0.1, SECONDS)
```

## Getters

### get_data
```{vexcode}
id: aim_sensing_ai_vision_get_data
```

`get_data` filters the data from the AI Vision Sensor frame to return a tuple. The AI Vision Sensor can detect signatures that include pre-trained objects, AprilTags, or configured Colors and Color Codes.

[Color Signatures](#color-signatures) and [Color Codes](#color-codes) must be configured first in the AI Vision Utility before they can be used with this method.

The tuple stores objects ordered from largest to smallest by width, starting at index 0. Each object's [properties](#properties) can be accessed using its index. An empty tuple is returned if no matching objects are detected.

**Usage:**<br>
`robot.vision.get_data(signature, count)`

| Parameters | Description |
|:----------:|-------------|
| `signature`  | What signature to get data of. Available signatures are: <ul><li><code>ALL_VISION</code> - Sports balls, barrels, VEX AIM Coding Robots, AprilTags, colors, and color codes</li> <li><code>ALL_CARGO</code> - Sports balls and barrels</li> <li><code>ALL_TAGS</code> - All AprilTags</li> <li><code>ALL_COLORS</code> - All configured color signatures and color codes</li> <li><code>SPORTS_BALL</code> - Only sports balls</li> <li><code>BLUE_BARREL</code> - Only blue barrels</li> <li><code>ORANGE_BARREL</code> - Only orange barrels</li> <li><code>AIM_ROBOT</code> - All VEX AIM Coding Robots</li> <li><code>TAG0</code> through <code>TAG37</code> - A single AprilTag with an ID from 0 to 37</li><li><code>NAME</code> - Color signature or color code where <code>NAME</code> is the name configured in the AI Vision Utility.</li></ul> |
| `count` | Optional. Sets the maximum number of objects that can be returned from 1 to 24 (default: 8).  |

**Note:** AprilTags 5 through 37 can be obtained by using the printed AprilTags from [AIM Printables](https://kb.vex.com/hc/en-us/articles/4410295384980-VEX-Printables#aim-printables-header-9).

```python
# Move forward if a sports ball is detected
while True:
    ball = robot.vision.get_data(SPORTS_BALL)
    if ball:
        robot.move_for(10, 0)
    wait(50, MSEC)
```
#### Color Signatures
A color signature is a unique color that the AI Vision Sensor can recognize. These signatures allow the sensor to detect and track objects based on their color. Once a Color Signature is configured, the sensor can identify objects with that specific color in its field of view. Color signatures are used with [get_data](#robot_take_snapshot) to process and detect colored objects in real-time.

![The AI Vision Utility showing a connected vision sensor detecting two colored objects. The left side displays a live camera feed with a blue box on the left and a red box on the right, each outlined with white bounding boxes. Black labels display their respective names, coordinates, and dimensions. The right side contains color signature settings, with sliders for hue and saturation range for both the red and blue boxes. Buttons for adding colors, freezing video, copying, and saving the image are at the bottom, along with a close button in the lower right corner.](/_static/img/AiVision/color_signatures.png)

```python
# Display if any objects match the Red_Box signature
while True:
    robot.screen.set_cursor(1, 1)
    robot.screen.clear_row(1)
    # Change to any configured Color Signature
    ai_objects = robot.vision.get_data(Red_Box)
    if ai_objects:
        robot.screen.print("Color signature detected!")
```

#### Color Codes
A color code is a structured pattern made up of 2 to 4 color signatures arranged in a specific order. These codes allow the AI Vision Sensor to recognize predefined patterns of colors. Color codes are useful for identifying complex objects or creating unique markers for autonomous navigation.

![The AI Vision Utility interface shows a connected vision sensor detecting two adjacent objects, a blue box on the left and a red box on the right, grouped together in a single white bounding box labeled BlueRed. Detection information includes angle (A:11°), coordinates (X:143, Y:103), width (W:233), and height (H:108). On the right panel, three color signatures are listed: Red_Box, Blue_Box, and BlueRed, with adjustable hue and saturation ranges. The BlueRed signature combines the Blue_Box and Red_Box. Below the video feed are buttons labeled Freeze Video, Copy Image, Save Image, and Close.](/_static/img/AiVision/color_code.png)

```python
# Display if any objects match the BlueRed code
while True:
    robot.screen.set_cursor(1, 1)
    robot.screen.clear_row(1)
    # Change to any configured Color Code
    ai_objects = robot.vision.get_data(BlueRed)
    if ai_objects:
        robot.screen.print("Color code detected!")
```

### has_sports_ball

```{vexcode}
id: aim_sensing_robot_has_ball
```

`has_sports_ball` returns a Boolean indicating whether the robot currently has a sports ball.
- `True` – The robot has a sports ball.
- `False` – The robot does not have a sports ball.

**Usage:**<br>
`robot.has_sports_ball()`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |

```python
# Kick when the robot has a sports ball
while True:
    if robot.has_sports_ball():
        robot.kicker.kick(MEDIUM)

    wait(50, MSEC)
```

### has_any_barrel

```{vexcode}
id: aim_sensing_robot_has_barrel
```

`has_any_barrel` returns a Boolean indicating whether the robot currently has any type of barrel.
- `True` – The robot has a barrel.
- `False` – The robot does not have a barrel.

**Usage:**<br>
`robot.has_any_barrel()`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |


```python
# Push a barrel away when detected
while True:
    if robot.has_any_barrel():
        robot.kicker.place()

    wait(50, MSEC)
```

### has_blue_barrel

```{vexcode}
id: aim_sensing_robot_has_blue_barrel
```

`has_blue_barrel` returns a Boolean indicating whether the robot currently has a blue barrel.
- `True` – The robot has a blue barrel.
- `False` – The robot does not have a blue barrel.

**Usage:**<br>
`robot.has_blue_barrel()`

| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |

```python
# Push a blue barrel away when detected
while True:
    if robot.has_blue_barrel():
        robot.kicker.place()

    wait(50, MSEC)
```

### has_orange_barrel

```{vexcode}
id: aim_sensing_robot_has_orange_barrel
```

`has_orange_barrel` returns a Boolean indicating whether the robot currently has an orange barrel.

- `True` – The robot has an orange barrel.
- `False` – The robot does not have an orange barrel.

**Usage:**<br>
`robot.has_orange_barrel()`


| Parameters       | Description                                                                 |
|:------------------: | :-----------------------------------------------------------------------------|
|  | This method has no parameters. |

```python
# Push an orange barrel away when detected
while True:
    if robot.has_orange_barrel():
        robot.kicker.place()

    wait(50, MSEC)
```

## Properties

There are twelve properties that are included with each object stored in a tuple after the [robot.vision.get_data](#robot_take_snapshot) method is used.

Some property values are based off of the detected object's position in the AI Vision Sensor's view at the time that `robot.vision.get_data` was used. The AI Vision Sensor has a resolution of 240 by 320 pixels.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box.](/_static/img/AiVision/VisionSensor-Barrel-Blank.png)

### .exists

```{vexcode}
id: aim_sensing_ai_vision_exists
```

`.exists` returns a Boolean indicating if the index exists in the tuple or not.
- `True`: The index exists.
- `False`: The index does not exist.

```python
# Check if at least two objects are detected
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    ai_objects = robot.vision.get_data(ALL_CARGO)

    if ai_objects:
        if ai_objects[1].exists:
            robot.screen.print("More than 2")
        else:
            robot.screen.print("Less than 2")
    wait(0.1, SECONDS)
```

### .width

```{vexcode}
id: aim_sensing_ai_vision_width
```

`.width` returns the width of the detected object in pixels, which is an integer between 1 and 320.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. Two vertical red dashed lines extend from the top of the frame down to the left and right edges of the bounding box. A double-headed black arrow between these lines indicates the width measurement.](/_static/img/AiVision/VisionSensor-Barrel-Width.png)

```python
# Move towards a Blue Barrel until its width is
# larger than 100 pixels
while True:
    barrel = robot.vision.get_data(BLUE_BARREL)

    if barrel:
        if barrel[0].width < 100:
            robot.move_at(0)
    else:
        robot.stop_all_movement()

    wait(50, MSEC)
```

### .height

```{vexcode}
id: aim_sensing_ai_vision_height
```

`.height` returns the height of the detected object in pixels, which is an integer between 1 and 240.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. Two horizontal red dashed lines extend from the left side of the frame to the top and bottom edges of the bounding box. A double-headed black arrow between these lines indicates the height measurement.](/_static/img/AiVision/VisionSensor-Barrel-Height.png)

```python
# Move towards a Blue Barrel until its height is
# larger than 100 pixels
while True:
    barrel = robot.vision.get_data(BLUE_BARREL)

    if barrel:
        if barrel[0].height < 100:
            robot.move_at(0)
    else:
        robot.stop_all_movement()

    wait(50, MSEC)
```

### .centerX

```{vexcode}
id: aim_sensing_ai_vision_centerX
```

`.centerX` returns the x-coordinate of the detected object’s center in pixels, which is an integer between 0 and 320.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. A vertical red dashed line extends from the top of the frame down to the center of the bounding box, indicating the X-coordinate of the center.](/_static/img/AiVision/VisionSensor-Barrel-CenterX.png)

```python
# Turn slowly until a Blue Barrel is centered in
# front of the robot
robot.set_turn_velocity(30)
robot.turn(RIGHT)

while True:
    barrel = robot.vision.get_data(BLUE_BARREL)

    if barrel:
        if 140 < barrel[0].centerX < 180: 
            robot.stop_all_movement()

    wait(10,MSEC)
```

### .centerY

```{vexcode}
id: aim_sensing_ai_vision_centerY
```

`.centerY` returns the y-coordinate of the detected object’s center in pixels, which is an integer between 0 and 240.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. A horizontal red dashed line extends from the left side of the frame to the center of the bounding box, indicating the Y-coordinate of the center.](/_static/img/AiVision/VisionSensor-Barrel-CenterY.png)

```python
# Move towards a Blue Barrel until its
# center y-coordinate is more than 140 pixels
while True:
    barrel = robot.vision.get_data(BLUE_BARREL)

    if barrel:
        if barrel[0].centerY < 140:
            robot.move_at(0)
    else:
        robot.stop_all_movement()

    wait(50, MSEC)
```

### .bearing

```{vexcode}
id: aim_sensing_ai_vision_bearing
```

`.bearing` returns a float representing how far an object is to the left or right of the center of the AI Vision Sensor’s view as a degree. A value of 0 means it’s centered, positive values mean the object is to the right, and negative values mean the object is to the left.

<!-- image needed -->

```python
# Keep the blue barrel directly in front of the robot
robot.set_turn_velocity(40)
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data:

        if vision_data[0].bearing > 5:
            robot.turn(RIGHT)
        elif vision_data[0].bearing < -5:
            robot.turn(LEFT)
        else:
            robot.stop_all_movement()

    else:
        robot.stop_all_movement()

    wait(0.1, SECONDS)
```

### .rotation

```{vexcode}
id: aim_sensing_ai_vision_rotation
```

`.rotation` returns the orientation of the detected object in degrees, which is an integer between 0 and 359.

![A camera interface displays a vertically stacked object with a blue top half and a red bottom half, centered in the frame. A label beneath the object reads Red_Blue A:270° CX:185 CY:81 W:93 H:150, indicating the object's name, angle of rotation, center X and Y coordinates, width, and height. Gridlines and numeric axes mark the image dimensions, with X ranging from 0 to 320 and Y from 0 to 240.](/_static/img/AiVision/rotation.png)

```python
# Slide left or right depending on how the
# AprilTag is rotated
while True: 
    apriltags = robot.vision.get_data(ALL_TAGS)

    if apriltags: 
        if 50 < apriltags[0].rotation < 100 :
            robot.move_at(90)
            
        elif 270 < apriltags[0].rotation < 330 :
            robot.move_at(270)
        
        else:
            robot.stop_all_movement()
    else:
        robot.stop_all_movement()

    wait(50, MSEC)
```

### .originX

```{vexcode}
id: aim_sensing_ai_vision_originX
```

`.originX` returns the x-coordinate of the top-left corner of the detected object’s bounding box in pixels, which is an integer between 0 and 320.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. A vertical red dashed line extends from the top of the frame to the left edge of the bounding box, indicating the X-coordinate of the bounding box's origin.](/_static/img/AiVision/VisionSensor-Barrel-OriginX.png)

```python
# Display if an Orange Barrel is to the
# left or the right
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1,1)
    
    orange_barrel = robot.vision.get_data(ORANGE_BARREL)
    
    if orange_barrel:
        if orange_barrel[0].originX < 160:
            robot.screen.print("To the left!")
        else: 
            robot.screen.print("To the right!")

    wait(50, MSEC)
```

### .originY

```{vexcode}
id: aim_sensing_ai_vision_originY
```

`.originY` returns the y-coordinate of the top-left corner of the detected object’s bounding box in pixels, which is an integer between 0 and 240.

![A blue barrel with an orange stripe is centered in the frame, surrounded by a black bounding box. A horizontal red dashed line extends from the left side of the frame to the top edge of the bounding box, indicating the Y-coordinate of the bounding box's origin.](/_static/img/AiVision/VisionSensor-Barrel-OriginY.png)

```python
# Display if an Orange Barrel is close or far
# from the robot
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)

    orange_barrel = robot.vision.get_data(ORANGE_BARREL)
    
    if orange_barrel:
        if orange_barrel[0].originY < 80:
            robot.screen.print("Far")
        else: 
            robot.screen.print("Close")

    wait(50, MSEC)
```

### .id

```{vexcode}
id: aim_sensing_ai_vision_id
```

`.id` returns the ID of the detected AI Classification or AprilTag as an integer.

For an AprilTag, the `.id` property represents the detected AprilTag's ID number in the range of 0 to 36. For an AI Classification, the id corresponds to the predefined id as shown below.

| AI Classification        | id | Signature        |
|---------------|----|--------------------------|
| Ball          | 0  | `SPORTS_BALL`            |
| Blue Barrel   | 1  | `BLUE_BARREL`     |
| Orange Barrel | 2  | `ORANGE_BARREL`   |
| AIM Robot         | 3  | `AIM_ROBOT`           |

```python
# Move forward when AprilTag 1 is detected
while True:
    apriltags = robot.vision.get_data(ALL_TAGS)

    if apriltags:
        if apriltags[0].id == 1:
            robot.move_at(0)
    else:
        robot.stop_all_movement()

    wait(50, MSEC)
```

### .score

```{vexcode}
id: aim_sensing_ai_vision_score
```

`.score` returns the confidence score of the detected AI Classification as an integer between 1 and 100.

```python
# Look confident if an Orange Barrel is detected
while True:
    barrel = robot.vision.get_data(ORANGE_BARREL)

    if barrel:
        if barrel[0].score > 95: 
            robot.screen.show_emoji(CONFIDENT)
        else:
            robot.screen.hide_emoji()

    wait(50, MSEC)
```

### .type

```{vexcode}
id: aim_sensing_ai_vision_type
```

`.type` returns what type of object is detected. It will return one of the following:

| Object Type        | Included Objects |
|:---------------:|-----------------------------------------------------------|
| `AiVision.AI_OBJECT`   | - Sports balls <br> - Blue barrels <br> - Orange barrels |
| `AiVision.TAG_OBJECT`  | - AprilTags |
| `AiVision.COLOR_OBJECT` | - Color signatures |
| `AiVision.CODE_OBJECT`  | - Color codes |

```python
# Display if an AprilTag or AI Classification
# is detected
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    vision_data = robot.vision.get_data(ALL_VISION)
    if vision_data:
        if vision_data[0].type == AiVision.AI_OBJECT:
            robot.screen.print("AI Object!")
        elif vision_data[0].type == AiVision.TAG_OBJECT:
            robot.screen.print("AprilTag!")
    wait(0.1, SECONDS)
```

```python
# Display a list of all detected objects
while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)
    vision_data = robot.vision.get_data(ALL_VISION)
    
    if vision_data:
        for obj in vision_data:
            if obj.type == AiVision.AI_OBJECT:
                robot.screen.print("- AI Object")
            elif obj.type == AiVision.TAG_OBJECT:
                robot.screen.print("- AprilTag")
            robot.screen.next_row()
    
    wait(0.1, SECONDS)
```

## Constructors

### Creating a Color Signature

A new Color Signature is created using the `Colordesc` constructor and then registered with the AI Vision Sensor using the `color_description` method. A `Colordesc` object defines 1 of up to 7 detectable color signatures for the sensor, but it must be explicitly set using `color_description` to take effect.

**Colordesc Usage:**<br>
`Colordesc(index, red, green, blue, hangle, hdsat)`

| Parameter | Description |
|:--:|:--|
| `index` | An integer from 1 to 7 representing the Color Signature index. If two Color Signatures use the same index, the second will override the first. |
| `red` | An integer from 0 to 255 for the red component of the color. |
| `green` | An integer from 0 to 255 for the green component of the color. |
| `blue` | An integer from 0 to 255 for the blue component of the color. |
| `hangle` | A float from 1 to 40 representing the hue range in degrees. |
| `hdsat` | A float from 0.10 to 1.00 representing the saturation range. |

**color_description Usage:**<br>
`robot.vision.color_description(object)`

| Parameter | Description |
|:--:|:--|
| `object` | The `Colordesc` object to set as a detectable Color Signature. |

```python
# Detect a red object
red_box = Colordesc(1, 207, 19, 25, 10.00, 0.20)
robot.vision.color_description(red_box)

while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)

    red_boxes = robot.vision.get_data(red_box)

    if red_boxes:
        robot.screen.print("Red detected!")
    else:
        robot.screen.print("No red detected.")

    wait(0.2, SECONDS)
```

### Creating a Color Code

```{contents}
:local: true
```

A new Color Code is created using the `Codedesc` constructor and then activated using the `code_description` method. A Color Code groups 2 to 4 existing `Colordesc` objects into a single identifier that the AI Vision Sensor can detect as a sequence, but it must be explicitly set using `code_description` to take effect.

**Codedesc Usage:**<br>
`Codedesc(index, c1, c2, c3, c4, c5)`

| Parameter | Description |
|:---------:|:------------|
| `index`   | The index of the Color Code, from 1 to 8. Note: If you create two `Codedesc` objects with the same index, the second will override the first. |
| `c1`      | The first `Colordesc` object in the code. |
| `c2`      | The second `Colordesc` object in the code. |
| `c3`      | Optional. A third `Colordesc` object. |
| `c4`      | Optional. A fourth `Colordesc` object.  |

**code_description Usage:**<br>
`robot.vision.code_description(object)`

| Parameter | Description |
|:---------:|:------------|
| `object`   | A `Codedesc` object to register as a detectable Color Code. |

```python
# Create Color Signatures
red_box = Colordesc(1, 207, 19, 25, 10.00, 0.20)
purple_box = Colordesc(2, 98, 18, 227, 10.00, 0.20)

robot.vision.color_description(red_box)
robot.vision.color_description(purple_box)

# Detect a red_purple Color Code
red_purple = Codedesc(1, red_box, purple_box)
robot.vision.code_description(red_purple)

while True:
    robot.screen.clear_screen()
    robot.screen.set_cursor(1, 1)

    code_objects = robot.vision.get_data(red_purple)

    if code_objects:
        robot.screen.print("Code detected!")
    else:
        robot.screen.print("No code detected.")

    wait(0.2, SECONDS)
```