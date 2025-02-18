import os
import shutil
import subprocess


# Get project root directory
PROJECT_DIR = os.getcwd()

# Fetch user selections from environment (Cookiecutter replaces these variables before execution)
include_visualization = "{{cookiecutter.include_visualization}}".strip().lower()
include_training = "{{cookiecutter.include_training}}".strip().lower()
include_inference = "{{cookiecutter.include_inference}}".strip().lower()
include_data = "{{cookiecutter.include_data}}".strip().lower()
include_model = "{{cookiecutter.include_model}}".strip().lower()

# User selections mapping
user_selections = {
    "include_visualization": include_visualization,
    "include_training": include_training,
    "include_inference": include_inference,
    "include_data": include_data,
    "include_model": include_model,
}

# Define the directories based on user selection
dirs_to_remove = {
    "include_visualization": ["src/visualization"],
    "include_training": ["src/engines/train.py", "src/cmds/train_main.py"],
    "include_inference": ["src/engines/inference.py", "src/cmds/inference_main.py"],
    "include_data": ["src/data"],
    "include_model": ["src/model"],
}

# Iterate over user selections and remove unselected directories/files
for key, dir_paths in dirs_to_remove.items():
    print(f"Checking if {key} should be excluded... (User input: {user_selections[key]})")
    if user_selections[key] == "n":  # User selected 'n'
        for dir_path in dir_paths:
            full_path = os.path.join(PROJECT_DIR, dir_path)
            if os.path.exists(full_path):
                if os.path.isfile(full_path):
                    os.remove(full_path)  # Remove file
                    print(f"Removed file: {dir_path}")
                else:
                    shutil.rmtree(full_path)  # Remove directory
                    print(f"Removed directory: {dir_path}")
                    
                    
# ----------------------------------------
# Add 'data/' and 'model/' to .gitignore before Git initialization
# ----------------------------------------
gitignore_path = os.path.join(PROJECT_DIR, ".gitignore")

# Ensure .gitignore exists
if not os.path.exists(gitignore_path):
    with open(gitignore_path, "w") as gitignore_file:
        gitignore_file.write("# Git ignore file\n")

# Append 'data/' and 'model/' if they are not already in .gitignore
gitignore_entries = ["data/", "models/"]

with open(gitignore_path, "r+") as gitignore_file:
    existing_lines = gitignore_file.readlines()
    for entry in gitignore_entries:
        if entry + "\n" not in existing_lines:  # Ensure no duplicate entries
            gitignore_file.write(entry + "\n")

print("✅ Added 'data/' and 'models/' to .gitignore")

# ----------------------------------------
# Initialize Git repository
# ----------------------------------------
print("\nInitializing Git repository...")


try:
    subprocess.run(["git", "init"], cwd=PROJECT_DIR, check=True)  # Initialize Git
    subprocess.run(["git", "add", "."], cwd=PROJECT_DIR, check=True)  # Stage files
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=PROJECT_DIR, check=True)  # Commit
    print("✅ Git repository initialized successfully!")
except Exception as e:
    print(f"⚠️ Error initializing Git: {e}")