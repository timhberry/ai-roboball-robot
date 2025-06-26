#!/bin/bash

# reset.sh
# This script helps reset the current Git working directory and optionally modifies main.py.

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [blue|orange]"
    echo "  blue: Resets the Git working directory."
    echo "  orange: Resets the Git working directory AND replaces 'ORANGE_BARREL' with 'BLUE_BARREL' in main.py."
    exit 1
fi

ARGUMENT=$1

echo "Attempting to reset Git working directory to match the remote repository..."

# Reset the current branch to the HEAD of the upstream remote, discarding local changes.
# 'git reset --hard HEAD' discards changes in the working directory and staging area.
# 'git clean -fd' removes untracked files and directories.
git reset --hard HEAD && git clean -fd

if [ $? -eq 0 ]; then
    echo "Git working directory reset successfully."
else
    echo "Error: Failed to reset Git working directory. Please check your Git status."
    exit 1
fi

# If the argument is "orange", perform the string replacement in main.py
if [ "$ARGUMENT" == "orange" ]; then
    echo "Argument is 'orange'. Proceeding to modify main.py..."

    # Check if main.py exists
    if [ -f "main.py" ]; then
        # Use sed to replace "ORANGE_BARREL" with "BLUE_BARREL" on lines 159 and 175.
        # The -i option edits the file in place. On macOS (BSD sed), -i requires an argument
        # for the backup file extension (e.g., -i.bak). Using -i '' provides an empty extension,
        # which makes it compatible with both GNU sed (Linux) and BSD sed (macOS) for in-place editing
        # without creating a backup file.
        # 's/old_string/new_string/' is the substitution command.
        sed -i '' '143s/ORANGE_BARREL/BLUE_BARREL/' main.py
        sed -i '' '160s/ORANGE_BARREL/BLUE_BARREL/' main.py

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

echo "Script execution finished."
