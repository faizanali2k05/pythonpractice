import os
import random
import datetime
import subprocess
from pathlib import Path

def generate_random_content():
    """Generate random content for the dummy file"""
    sentences = [
        f"This is commit #{random.randint(1000, 9999)} made on {datetime.datetime.now()}",
        f"Random update #{random.randint(1, 100)} at {datetime.datetime.now()}",
        f"Another daily update - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Daily code improvement #{random.randint(1, 50)}",
        f"Minor tweak made at {datetime.datetime.now().strftime('%H:%M:%S')}",
        f"Documentation update #{random.randint(1, 25)}",
        f"Bug fix #{random.randint(1, 30)} - resolved issue with implementation",
        f"Feature enhancement #{random.randint(1, 20)}",
        f"Code cleanup and optimization",
        f"Performance improvements for module X"
    ]
    return random.choice(sentences)

def create_dummy_file(file_path):
    """Create or update a dummy file with random content"""
    content = generate_random_content()
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Append content to file
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"\n{content}\n")
        
def commit_changes():
    """Stage and commit changes to git"""
    try:
        # Stage all changes
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Create commit with random message
        commit_messages = [
            "Update documentation",
            "Fix minor typo",
            "Add new feature",
            "Refactor code",
            "Optimize performance",
            "Improve readability",
            "Enhance functionality",
            "Clean up code",
            "Add comments",
            "Minor improvements",
            "Bug fixes",
            "Code improvements",
            "Update dependencies",
            "Fix edge cases",
            "Add tests"
        ]
        
        commit_message = random.choice(commit_messages) + f" - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True)
        print(f"Committed: {commit_message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error committing: {e}")
        return False

def main():
    print("Starting GitHub contribution generator...")
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("Error: Not in a git repository. Please initialize a git repo first.")
        return
    
    # Number of commits to create (between 25 and 30)
    num_commits = random.randint(25, 30)
    print(f"Creating {num_commits} commits...")
    
    # Create dummy file path
    dummy_file = "auto_generated_content.txt"
    
    for i in range(num_commits):
        # Create/update dummy file
        create_dummy_file(dummy_file)
        
        # Commit the changes
        success = commit_changes()
        
        if not success:
            print("Failed to commit changes. Exiting.")
            return
        
        # Small delay between commits to simulate real activity
        import time
        time.sleep(0.5)
    
    print(f"Successfully created {num_commits} commits!")
    print("\nIMPORTANT: Please note that artificially inflating GitHub contributions")
    print("may violate GitHub's Terms of Service and is not recommended. This script")
    print("is for educational purposes only.")

if __name__ == "__main__":
    main()