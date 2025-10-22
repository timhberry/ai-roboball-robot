#!/bin/bash
# reset.sh
# This script helps reset the current Git working directory and optionally modifies main.py.
# It can also save current changes to a new branch before resetting.

# Check if at least one argument is provided
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
    echo "Usage: $0 [blue|orange] [branch-name]"
    echo "  blue: Resets the Git working directory."
    echo "  orange: Resets the Git working directory AND replaces 'ORANGE_BARREL' with 'BLUE_BARREL' in main.py."
    echo "  branch-name (optional): If provided, saves current changes to a new branch and pushes to remote before resetting."
    exit 1
fi

ARGUMENT=$1
BRANCH_NAME=$2

# If a branch name is provided, save current changes
if [ -n "$BRANCH_NAME" ]; then
    echo "Branch name provided: '$BRANCH_NAME'"
    echo "Saving current changes to a new branch..."
    
    # Check if there are any changes to save
    if git diff-index --quiet HEAD --; then
        echo "Warning: No changes detected in working directory. Skipping branch creation."
    else
        # Create and checkout new branch
        git checkout -b "$BRANCH_NAME"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create branch '$BRANCH_NAME'. It may already exist."
            exit 1
        fi
        
        # Stage all changes
        git add -A
        if [ $? -ne 0 ]; then
            echo "Error: Failed to stage changes."
            exit 1
        fi
        
        # Commit changes
        git commit -m "Save changes to branch $BRANCH_NAME"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to commit changes."
            exit 1
        fi
        
        # Push to remote
        git push -u origin "$BRANCH_NAME"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to push branch to remote."
            exit 1
        fi
        
        echo "Successfully saved and pushed changes to branch '$BRANCH_NAME'."
        
        # Return to the main branch
        git checkout main
        if [ $? -ne 0 ]; then
            echo "Error: Failed to checkout main branch."
            exit 1
        fi
    fi
fi

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
        sed -i '' '153s/ORANGE_BARREL/BLUE_BARREL/' main.py
        sed -i '' '172s/ORANGE_BARREL/BLUE_BARREL/' main.py
                
        if [ $? -eq 0 ]; then
            echo "Successfully replaced orange objects with blue objects in main.py."
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
    echo "Usage: $0 [blue|orange] [branch-name]"
    exit 1
fi

echo "Script execution finished."