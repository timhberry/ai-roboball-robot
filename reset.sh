#!/bin/bash

# reset.sh
# This script resets the robot starter code in main.py, sets the ball colour signature and updates the target barrel colour

# Ball signature colours - change these if you're calibrating to different lighting
BALL_R=236
BALL_G=237
BALL_B=88

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [blue|orange]"
    echo "  blue: Resets the robot starter code (main.py)"
    echo "  orange: Resets the robot starter code (main.py) AND replaces 'ORANGE_BARREL' with 'BLUE_BARREL'."
    exit 1
fi

ARGUMENT=$1

echo "Attempting to reset main.py..."

git checkout HEAD -- main.py

if [ $? -eq 0 ]; then
    echo "main.py reset successfully."
else
    echo "Error: Failed to reset main.py. Please check your Git status."
    exit 1
fi

# If the argument is "orange", perform the string replacement in main.py
if [ "$ARGUMENT" == "orange" ]; then
    echo "Argument is 'orange'. Proceeding to modify main.py..."

    # Check if main.py exists
    if [ -f "main.py" ]; then

        sed -i '' '153s/ORANGE_BARREL/BLUE_BARREL/' main.py
        sed -i '' '172s/ORANGE_BARREL/BLUE_BARREL/' main.py

        if [ $? -eq 0 ]; then
            echo "Successfully replaced 'ORANGE_BARREL' with 'BLUE_BARREL' in main.py."
        else
            echo "Error: Failed to modify main.py. 'sed' command might have encountered an issue."
        fi
    else
        echo "Warning: main.py not found in the current directory. Skipping file modification."
    fi
elif [ "$ARGUMENT" == "blue" ]; then
    echo "Argument is 'blue'. No further actions required."
else
    echo "Invalid argument: '$ARGUMENT'. Please use 'blue' or 'orange'."
    echo "Usage: $0 [blue|orange]"
    exit 1
fi

echo "Updating ball signature colours."
sed -i '' "119s/Colordesc([^,]*, [^,]*, [^,]*, [^,]*/Colordesc(1, $BALL_R, $BALL_G, $BALL_B/" main.py

echo "Script execution finished."
