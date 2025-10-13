#region VEXcode Generated Robot Configuration
from vex import *
from vex_globals import *
import math
import random
import time

# Robot initialization for AIM platform
robot = Robot()

# Timer initialization
timer = Timer()

# AI Vision configuration code
robot.vision.model_detection(True)
robot.vision.tag_detection(False)

# Console Colors
def set_console_text_color(COLOR):
    if (COLOR == Color.RED):
        print("\033[31m", end="")
    elif (COLOR == Color.GREEN):
        print("\033[32m", end="")
    elif (COLOR == Color.BLUE):
        print("\033[34m", end="")
    elif (COLOR == Color.BLACK):
        print("\033[30m", end="")
    elif (COLOR == Color.WHITE):
        print("\033[37m", end="")
    elif (COLOR == Color.YELLOW):
        print("\033[33m", end="")
    elif (COLOR == Color.ORANGE):
        print("\033[91m", end="")
    elif (COLOR == Color.PURPLE):
        print("\033[35m", end="")
    elif (COLOR == Color.CYAN):
        print("\033[36m", end="")
    elif (COLOR == Color.TRANSPARENT):
        print("\033[97m", end="")
    else:
        print("\033[30m", end="")

# Clear Console
def clear_console():
    print("\033[2J", end="")

# User Uploaded Images
IMG_AMAZED = "image1.png"
IMG_THRILLED = "image2.png"
IMG_DETERMINED = "image3.png"
IMG_THINKING = "image4.png"
IMG_STRESSED = "image5.png"
IMAGE6 = "image6.png"
IMAGE7 = "image7.png"
IMAGE8 = "image8.png"
IMAGE9 = "image9.png"
IMAGE10 = "image10.png"


# User Uploaded Sounds
SOUND1 = "sound1.mp3"
SOUND2 = "sound2.mp3"
SOUND3 = "sound3.mp3"
SOUND4 = "sound4.mp3"
SOUND5 = "sound5.mp3"
SOUND6 = "sound6.mp3"
SOUND7 = "sound7.mp3"
SOUND8 = "sound8.mp3"
SOUND9 = "sound9.mp3"
SOUND10 = "sound10.mp3"


# reset console text color
set_console_text_color(BLUE)
# Reset the Inertial Sensor heading and rotation
robot.inertial.reset_heading()
robot.inertial.reset_rotation()

#endregion VEXcode Generated Robot Configuration

# --- Constants and Enums ---

# Robot Status "Enum" (using a class for namespacing on MicroPython)
class RobotStatus:
    FINDING_BALL = "findingBall"
    GETTING_BALL = "gettingBall"
    FINDING_GOAL = "findingGoal"
    CRASHED = "crashed"

# Movement Constants
DEFAULT_SPEED = 50
PRECISION_MOVE_VELOCITY = 25
PRECISION_TURN_VELOCITY = 20 # Used for aligning with goal
SCAN_TURN_VELOCITY = 20      # New constant for ball scanning turns
SCAN_RANDOM_MOVE_MM = 20     # Distance to move after a full scan

# Vision and Behavior Constants
GOAL_HEIGHT_THRESHOLD = 30  # Minimum height of goal barrel to consider close enough
SCAN_MOVE_DURATION_SEC = 2
SCAN_CYCLES_BEFORE_ACTION = 3
APPROACH_MOVE_DURATION_MSEC = 20
TURN_MOVE_DURATION_MSEC = 500

# Set the inital state for the robot
crashed = False
status = RobotStatus.FINDING_BALL
robot.set_move_velocity(DEFAULT_SPEED)
robot.set_turn_velocity(DEFAULT_SPEED)

# If we ever crash, use this callback
def crashed_callback():
    global crashed
    crashed = True

# Set up the callback and crash sensitivity
robot.inertial.crashed(crashed_callback)
robot.inertial.set_crash_sensitivity(NORMAL)

# Calibrate the robot and disable AprilTag sensing
robot.inertial.calibrate()
if robot.inertial.is_calibrating():
    print("Waiting for callibration to complete")
    wait(2, SECONDS)


def look_for_ball():
    print(f"{time.time()}: look_for_ball() called")
    """Makes the robot rotate in place to scan for the ball."""
    robot.turn(RIGHT, SCAN_TURN_VELOCITY) # Or LEFT, or alternate directions for a more thorough scan
    wait(TURN_MOVE_DURATION_MSEC, MSEC) # Use a small duration for a quick turn
    robot.stop_all_movement() # Stop after the turn


def align_with_goal():
    print(f"{time.time()}: align_with_goal() called")
    """Turns the robot to face the opponent's goal barrel."""
    robot.set_turn_velocity(PRECISION_TURN_VELOCITY)
    robot.set_move_velocity(PRECISION_MOVE_VELOCITY)

    max_turns = 100  # Prevent infinite loop
    turn_count = 0
    while turn_count < max_turns:
        # Check if we still have the ball at the start of each turn
        if not robot.has_sports_ball():
            print("Dropped the ball while aligning with goal!")
            return False

        vision_data = robot.vision.get_data(ORANGE_BARREL)
        if vision_data and vision_data[0].exists:
            robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
            robot.stop_all_movement()
            return True
        else:
            robot.turn(RIGHT)
            wait(TURN_MOVE_DURATION_MSEC, MSEC)
            robot.stop_all_movement()
            turn_count += 1
    print("Warning: Goal not found after many turns.")
    return False


def approach_goal():
    print(f"{time.time()}: approach_goal() called")
    """Moves the robot closer to the goal until a certain height threshold is met."""
    while True:
        vision_data = robot.vision.get_data(ORANGE_BARREL)
        if vision_data and vision_data[0].exists:
            goal_height = vision_data[0].height
            if goal_height >= GOAL_HEIGHT_THRESHOLD:
                robot.stop_all_movement()
                return True
            robot.move_at(vision_data[0].bearing)
            wait(APPROACH_MOVE_DURATION_MSEC, MSEC)
        else:
            # Lost sight of the goal, stop approaching
            robot.stop_all_movement()
            return False


def execute_kick():
    print(f"{time.time()}: execute_kick() called")
    """Performs the kicking action and celebratory animations."""
    robot.kicker.kick(MEDIUM)
    robot.screen.show_file(IMG_AMAZED, 0, 0)
    robot.sound.play(ACT_HAPPY)
    for _ in range(3):
        robot.led.on(ALL_LEDS, YELLOW)
        wait(.25, SECONDS)
        robot.led.off(ALL_LEDS)
        wait(.25, SECONDS)

    # Back to the game, reset velocity and turn around
    wait(3, SECONDS)
    robot.set_move_velocity(DEFAULT_SPEED)
    robot.set_turn_velocity(DEFAULT_SPEED)
    robot.turn(RIGHT)
    wait(1, SECONDS)
    robot.stop_all_movement()

# Main loop
while True:
    print(f"{time.time()}: Entering main loop")

    if status == RobotStatus.FINDING_BALL:
        print(f"{time.time()}: State is FINDING_BALL")
        # If we are finding the ball, we run the look_for_ball function in a thread
        # and stop when we see the ball in our AI Vision camera.
        # Since look_for_ball() is now non-blocking, we call it directly.

        robot.screen.show_file(IMG_THINKING, 0, 0)

        # Get the robot's rotation at the start of the scan
        start_scan_rotation = robot.inertial.get_rotation()

        ball_found = False
        while True:
            if crashed:
                status = RobotStatus.CRASHED
                break
            look_for_ball() # Perform a small turn to scan

            detected_ball_object = None

            vision_data_sports_ball = robot.vision.get_data(SPORTS_BALL)
            if vision_data_sports_ball: # Check if the tuple is not empty
                detected_ball_object = vision_data_sports_ball[0]

            if detected_ball_object:
                robot.turn_to(robot.inertial.get_heading() + detected_ball_object.bearing)
                status = RobotStatus.GETTING_BALL
                ball_found = True
                break

            # After checking for the ball, see if we need to move
            if abs(robot.inertial.get_rotation() - start_scan_rotation) >= 360:
                print("Completed a full 360 scan, moving to a new spot.")
                
                # Choose a random direction: 0=fwd, 90=right, 180=back, 270=left
                move_directions = [0, 90, 180, 270]
                random_direction = random.choice(move_directions)
                
                # Move in that direction. This is a blocking call.
                robot.move_at(random_direction, PRECISION_MOVE_VELOCITY)
                wait(SCAN_MOVE_DURATION_SEC, SECONDS)
                robot.stop_all_movement()
                
                # Reset the scan rotation tracker for the next 360-degree scan
                start_scan_rotation = robot.inertial.get_rotation()
            
        if not ball_found and not crashed: # If loop broke for other reason
            status = RobotStatus.FINDING_BALL # Re-enter finding ball state


    elif status == RobotStatus.GETTING_BALL:
        print(f"{time.time()}: State is GETTING_BALL")
        # If we've seen the ball, we now need to go get it!

        robot.screen.show_file(IMG_THRILLED, 0, 0)

        ball_acquired = False
        while True:
            if crashed:
                status = RobotStatus.CRASHED
                break

            detected_ball_object = None

            vision_data_sports_ball = robot.vision.get_data(SPORTS_BALL)
            if vision_data_sports_ball: # Check if the tuple is not empty
                detected_ball_object = vision_data_sports_ball[0]

            if detected_ball_object:           # We can still see the ball
                if robot.has_sports_ball():                     # Do we have it?
                    robot.stop_all_movement()                   # If so, break the While loop
                    ball_acquired = True
                    break
                else:
                    robot.move_at(detected_ball_object.bearing)       # If not, move towards it
                    wait(APPROACH_MOVE_DURATION_MSEC, MSEC)
            else:                                               # We can't see the ball
                break                                           # so break the While loop

        if ball_acquired:                                       # Did we get it?
            robot.stop_all_movement()                           # Stop before looking for the goal
            status = RobotStatus.FINDING_GOAL                   # Great, go find the goal
        else:
            robot.stop_all_movement()                           # Stop before searching again
            status = RobotStatus.FINDING_BALL                   # We lost it, go back to playing


    elif status == RobotStatus.FINDING_GOAL:
        print(f"{time.time()}: State is FINDING_GOAL")
        # We've got the ball, now we need to find the goal and attempt to score

        robot.screen.show_file(IMG_DETERMINED, 0, 0)

        if not robot.has_sports_ball():
            status = RobotStatus.FINDING_BALL # We dropped the ball
            continue

        if align_with_goal():
            if approach_goal():
                if robot.has_sports_ball():
                    execute_kick()
                else:
                    status = RobotStatus.FINDING_BALL # Dropped ball while approaching
            else:
                status = RobotStatus.FINDING_BALL # Lost goal while approaching
        else:
            status = RobotStatus.FINDING_BALL # Failed to align with goal

        status = RobotStatus.FINDING_BALL # After attempting to score, go back to finding ball


    elif status == RobotStatus.CRASHED:
        print(f"{time.time()}: State is CRASHED")
        # We crashed! We may have hit another robot, or the edge of the field
        # We'll try turning around to see if that helps

        robot.screen.show_file(IMG_STRESSED, 0, 0)
        robot.sound.play(CRASH)
        robot.stop_all_movement()
        wait(3, SECONDS) # Allow some time for robot to settle
        robot.turn(RIGHT)
        wait(1, SECONDS)
        robot.stop_all_movement()
        crashed = False
        status = RobotStatus.FINDING_BALL