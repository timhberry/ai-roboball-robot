---
title: Emojis | VEX AIM - Python API
description: Explore the Python API reference for the emoji display on a VEX AIM Coding Robot. Find detailed descriptions for methods, parameters, and usage examples to display an emoji.
---

```{highlight} python
:linenothreshold: 5
```

# Emoji

```{contents}
:local: true
```


## Introduction

The VEX AIM Coding Robot features a screen-based emoji display that can show various expressions to indicate emotions or status. Below is a list of available methods:

- [show_emoji](#show_emoji) – Displays an emoji facing forward, left, or right.  
- [hide_emoji](#hide_emoji) – Clears the emoji from the screen.


## Actions

### show_emoji

```{vexcode}
id: aim_looks_robot_screen_show_emoji
```

```{vexcode}
id: aim_looks_robot_screen_show_emoji_look
```

`show_emoji` displays an emoji on the robot's screen, with an optional direction to face. The emoji will appear over any text or drawn images on the screen.

**Usage:**<br>`robot.screen.show_emoji(emoji, direction)`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| `emoji` | One of the emojis (shown below). |
| `direction` | Optional. The direction the emoji is facing on the screen. `LOOK_FORWARD` (default), `LOOK_LEFT`, or `LOOK_RIGHT`  |

| ![A smiling emoji with open eyes and an open mouth.](/_static/img/vexpressions/1-excited.png)<br>`EXCITED` | ![An emoji with a closed mouth smile and sunglasses.](/_static/img/vexpressions/2-confident.png)<br>`CONFIDENT` | ![A winking emoji sticking its tongue out.](/_static/img/vexpressions/3-silly.png)<br>`SILLY` | ![A grinning emoji with blushing cheeks and stars around its head.](/_static/img/vexpressions/4-amazed.png)<br>`AMAZED` |
|:--:|:--:|:--:|:--:|
| ![A smiling emoji with an open mouth and raised eyebrows, with a super hero style mask over its eyes.](/_static/img/vexpressions/5-strong.png)<br>`STRONG` | ![A smiling emoji with an open mouth and stars for eyes.](/_static/img/vexpressions/6-thrilled.png)<br>`THRILLED` | ![A grinning emoji with a closed mouth smile.](/_static/img/vexpressions/7-happy.png)<br>`HAPPY` | ![A smiling emoji with a wide open mouthed smile and closed happy eyes.](/_static/img/vexpressions/8-proud.png)<br>`PROUD` |
| ![An emoji with a wide open mouthed smile and eyes squeezed shut with tears emerging.](/_static/img/vexpressions/9-laughing.png)<br>`LAUGHING` | ![A closed eyed grinning emoji holding up crossed fingers.](/_static/img/vexpressions/10-optimistic.png)<br>`OPTIMISTIC` | ![An emoji with a half-smile and its tongue slightly sticking out, with one raised eyebrow.](/_static/img/vexpressions/11-determined.png)<br>`DETERMINED` | ![A grinning emoji with heart eyes.](/_static/img/vexpressions/12-affectionate.png)<br>`AFFECTIONATE` |
| ![A closed mouth grinning emoji with closed peaceful eyes and raised eyebrows.](/_static/img/vexpressions/13-calm.png)<br>`CALM` | ![A wide eyed emoji with no mouth.](/_static/img/vexpressions/14-quiet.png)<br>`QUIET` | ![A blushing emoji with no mouth.](/_static/img/vexpressions/15-shy.png)<br>`SHY` | ![A grinning emoji with closed happy eyes and blushing cheeks.](/_static/img/vexpressions/16-cheerful.png)<br>`CHEERFUL` |
| ![A grinning emoji with closed happy eyes and heart shaped blushing cheeks, with pink hearts around the face.](/_static/img/vexpressions/17-loved.png)<br>`LOVED` | ![An open mouthed wide eyed emoji.](/_static/img/vexpressions/18-surprised.png)<br>`SURPRISED` | ![A slightly frowning emoji with slightly raised eyebrows and a finger on the chin.](/_static/img/vexpressions/19-thinking.png)<br>`THINKING` | ![A yawning emoji with closed eyes and a hand covering the yawning mouth.](/_static/img/vexpressions/20-tired.png)<br>`TIRED` |
| ![A slightly frowning emoji with furrowed eyebrows and a question mark on its face.](/_static/img/vexpressions/21-confused.png)<br>`CONFUSED` | ![An emoji with half closed eyes and a closed expressionless mouth.](/_static/img/vexpressions/22-bored.png)<br>`BORED` | ![A wide eyed emoji with raised eyebrows, blushing cheeks, and a tightly closed mouth.](/_static/img/vexpressions/23-embarrassed.png)<br>`EMBARRASSED` | ![A slightly frowning emoji with a bead of sweat on the forehead and pleading eyes.](/_static/img/vexpressions/24-worried.png)<br>`WORRIED` |
| ![A frowning emoji with open eyes.](/_static/img/vexpressions/25-sad.png)<br>`SAD` | ![An emoji with swollen eyes and a thermometer sticking out of its closed mouth.](/_static/img/vexpressions/26-sick.png)<br>`SICK` | ![A frowning emoji with closed eyes and deeply furrowed eyebrows.](/_static/img/vexpressions/27-disappointed.png)<br>`DISAPPOINTED` | ![An emoji with a quivering closed mouth frown and open eyes with slightly raised eyebrows.](/_static/img/vexpressions/28-nervous.png)<br>`NERVOUS` |
| ![A slightly frowning emoji with half open scowling eyes looking to the right.](/_static/img/vexpressions/29-annoyed.png)<br>`ANNOYED` | ![A frowning emoji with eyes squeezed shut and deeply furrowed eyebrows.](/_static/img/vexpressions/30-stressed.png)<br>`STRESSED` | ![A deeply frowning emoji with glaring eyes.](/_static/img/vexpressions/31-angry.png)<br>`ANGRY` | ![A frowning emoji with closed eyes, holding its head in its hands.](/_static/img/vexpressions/32-frustrated.png)<br>`FRUSTRATED` |
| ![A half frowning emoji with eyes looking to the right and irritated eyebrows.](/_static/img/vexpressions/33-jealous.png)<br>`JEALOUS` | ![A wide eyed emoji with an open mouth of surprise and raised eyebrows.](/_static/img/vexpressions/34-shocked.png)<br>`SHOCKED` | ![An open eyed, open mouthed emoji with hands on the sides of its face.](/_static/img/vexpressions/35-fear.png)<br>`FEAR` | ![An emoji with its eyes squeezed shut, a green tinge to its cheeks, and its tongue fully sticking out of its open mouth.](/_static/img/vexpressions/36-disgust.png)<br>`DISGUST` |

```python
# Show two opposite emotions
robot.screen.show_emoji(CONFIDENT)
wait(2, SECONDS)
robot.screen.show_emoji(FRUSTRATED)
```
```python
# Show an emoji facing three different directions
robot.screen.show_emoji(EXCITED, LOOK_LEFT)
wait(2, SECONDS)
robot.screen.show_emoji(EXCITED, LOOK_FORWARD)
wait(2, SECONDS)
robot.screen.show_emoji(EXCITED, LOOK_RIGHT)
```

### hide_emoji

```{vexcode}
id: aim_looks_robot_screen_hide_emoji
```

`hide_emoji` clears the emoji displayed on the robot's screen.

**Usage:**<br>`robot.screen.hide_emoji()`

| Parameters | Description |
| :----------------: | :-------------------------------------- |
| | This method has no parameters. |

```python
# Show an emoji for 2 seconds  
robot.screen.show_emoji(THINKING)
wait(2, SECONDS)
robot.screen.hide_emoji()
```