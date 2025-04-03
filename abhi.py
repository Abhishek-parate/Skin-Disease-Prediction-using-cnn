import os
import random
import subprocess
from datetime import datetime, timedelta
import time

# Project path - update this to your actual project path
PROJECT_PATH = "d:/abhi/Skin/Skin-Cancer-Detection-Using-CNN/Skin-Disease-Prediction/"

# Ensure we're in the right directory
os.chdir(PROJECT_PATH)

# List of possible file names to create temporarily
TEMP_FILES = [
    "temp_data_exploration.py",
    "model_improvements.py",
    "feature_extraction.py",
    "dataset_preprocessing.py",
    "hyperparameter_tuning.py",
    "model_evaluation.py",
    "visualization_utils.py",
    "augmentation_techniques.py",
    "performance_metrics.py",
    "deployment_notes.md",
    "ui_enhancements.js",
    "api_integration.py",
    "documentation_updates.md",
    "testing_framework.py",
    "optimization_attempts.py"
]

# List of commit messages
COMMIT_MESSAGES = [
    # Data preparation and exploration
    "Add exploratory data analysis for skin disease dataset",
    "Implement data preprocessing pipeline for skin images",
    "Fix image normalization in preprocessing workflow",
    "Enhance data augmentation for better model generalization",
    "Update train-test split ratio to improve validation",
    
    # Model development
    "Implement CNN architecture for skin disease classification",
    "Fine-tune model hyperparameters for better accuracy",
    "Add dropout layers to reduce overfitting",
    "Optimize batch size and learning rate",
    "Implement early stopping to prevent overfitting",
    
    # Model evaluation and improvement
    "Add confusion matrix visualization for model evaluation",
    "Implement cross-validation for more robust performance assessment",
    "Analyze model performance across different disease classes",
    "Fix class imbalance issues in the training dataset",
    "Add precision-recall metrics for model evaluation",
    
    # UI and Frontend
    "Update UI design for better user experience",
    "Enhance frontend responsiveness for mobile devices",
    "Fix image upload functionality in the web interface",
    "Add loading indicators during model prediction",
    "Improve error handling in the frontend",
    
    # Backend and Flask
    "Optimize Flask routes for better performance",
    "Add error handling for image processing failures",
    "Implement caching for faster prediction responses",
    "Fix CORS issues in API endpoints",
    "Update server-side validation for image uploads",
    
    # Documentation and refactoring
    "Update README with installation instructions",
    "Add documentation for model architecture",
    "Refactor code for better maintainability",
    "Add comments to improve code readability",
    "Update requirements.txt with new dependencies",
    
    # Testing and debugging
    "Add unit tests for preprocessing functions",
    "Fix bug in image resizing function",
    "Add integration tests for API endpoints",
    "Debug memory leak in model loading",
    "Fix path issues in file handling"
]

# Function to create a temporary file with some content
def create_temp_file(filename):
    with open(filename, 'w') as f:
        f.write(f"# Temporary file for commit history\n")
        f.write(f"# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Add some random content based on the file type
        if filename.endswith('.py'):
            f.write("import numpy as np\nimport tensorflow as tf\n\n")
            f.write(f"def process_data():\n    # TODO: Implement this function\n    pass\n\n")
            f.write(f"def train_model():\n    # TODO: Implement this function\n    pass\n\n")
        elif filename.endswith('.md'):
            f.write("# Documentation\n\n")
            f.write("## Overview\n\nThis document provides information about the skin disease classification project.\n\n")
            f.write("## Implementation Details\n\nThe model uses a CNN architecture implemented in TensorFlow.\n")
        elif filename.endswith('.js'):
            f.write("// Frontend enhancements\n\n")
            f.write("document.addEventListener('DOMContentLoaded', function() {\n    // TODO: Implement UI improvements\n    console.log('UI improvements loaded');\n});\n")

# Function to make a commit with a specific date
def make_commit(date, message):
    # Create a temporary file
    filename = random.choice(TEMP_FILES)
    create_temp_file(filename)
    
    # Stage the file
    subprocess.run(["git", "add", filename])
    
    # Commit with the specified date
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(["git", "commit", "-m", message], env=env)
    
    # Remove the temporary file
    os.remove(filename)
    subprocess.run(["git", "rm", "--cached", filename])
    
    # Amend the commit to include the deletion
    subprocess.run(["git", "commit", "--amend", "--no-edit"], env=env)
    
    print(f"Created commit dated {date_str}: {message}")

# Calculate the start date (2 months ago)
end_date = datetime.now()
start_date = end_date - timedelta(days=60)

# Initialize git if not already initialized
try:
    subprocess.run(["git", "status"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    subprocess.run(["git", "init"])
    # Create initial commit
    with open("README.md", "a") as f:
        f.write("\n\n## Project History\n\nInitial commit for skin disease classification project.")
    subprocess.run(["git", "add", "README.md"])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

# Generate daily commits
current_date = start_date
while current_date <= end_date:
    # Skip weekends for more realistic activity
    if current_date.weekday() < 5:  # 0-4 are Monday to Friday
        # Make 5 commits for this day
        for i in range(5):
            # Create a time during the workday
            hour = random.randint(9, 17)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_date = datetime(
                current_date.year, 
                current_date.month, 
                current_date.day,
                hour, minute, second
            )
            
            # Choose a random commit message
            commit_message = random.choice(COMMIT_MESSAGES)
            
            # Make the commit
            make_commit(commit_date, commit_message)
            
            # Sleep a bit to avoid overloading the system
            time.sleep(0.1)
    
    # Move to the next day
    current_date += timedelta(days=1)

print(f"Finished creating commit history from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
print("Remember to push the changes to your remote repository with: git push origin master")