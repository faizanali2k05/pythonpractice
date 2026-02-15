#!/usr/bin/env python3
"""
Daily Programming Activity Tracker - app.py
---------------------------------------
Tracks daily coding practice and progress visualization using GitHub APIs
Made with ✨❤✨ for #GitHub octocat
"""

import os
import json
import datetime
import subprocess
import random
from pathlib import Path

# Configuration
PROJECT_NAME = "Daily-Coding-Practice"
DAILY_GOALS = [
    "Solved 3 coding problems",
    "Implemented 2 algorithms",
    "Refactored existing code",
    "Added unit tests",
    "Fixed 2 bugs",
    "Learned new Python concepts",
    "Built a small utility tool",
    "Reviewed code documentation",
    "Optimized code performance",
    "Practiced data structures"
]

def initialize_project():
    """Initialize the coding practice project structure"""
    # Create project directory
    project_dir = Path(PROJECT_NAME)
    project_dir.mkdir(exist_ok=True)
    
    # Create necessary files
    files_to_create = {
        "README.md": f"""# {PROJECT_NAME}

## Daily Coding Practice Log

This repository tracks my daily programming practice and learning journey.

### Goals:
- Practice coding daily
- Learn new concepts regularly
- Build practical skills
- Document progress

### Daily Activities:
{chr(10).join([f"- {goal}" for goal in DAILY_GOALS])}

### Progress Tracking:
- ✅ Daily commits
- 📊 Learning milestones
- 🎯 Skill development

Started on: {datetime.date.today().strftime('%B %d, %Y')}
""",
        "progress_tracker.json": json.dumps({
            "start_date": str(datetime.date.today()),
            "total_days": 0,
            "streak": 0,
            "last_commit_date": None,
            "activities": []
        }, indent=2),
        "daily_log.txt": f"Daily Coding Practice Log\nStarted: {datetime.date.today()}\n{'='*50}\n"
    }
    
    # Create files
    for filename, content in files_to_create.items():
        filepath = project_dir / filename
        if not filepath.exists():
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    # Initialize git repo if not exists
    if not (project_dir / '.git').exists():
        os.chdir(project_dir)
        subprocess.run(['git', 'init'], check=True, capture_output=True)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit: Setup coding practice tracker'], 
                      check=True, capture_output=True)
        os.chdir('..')
    
    return project_dir

def log_daily_activity(project_dir):
    """Log today's coding activity"""
    today = datetime.date.today()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Read progress tracker
    tracker_file = project_dir / 'progress_tracker.json'
    with open(tracker_file, 'r') as f:
        tracker = json.load(f)
    
    # Check if already committed today
    if tracker['last_commit_date'] == str(today):
        print("Already committed today. Skipping...")
        return False
    
    # Generate daily activity
    activity = random.choice(DAILY_GOALS)
    practice_time = random.randint(30, 120)  # 30-120 minutes
    
    # Update log file
    log_file = project_dir / 'daily_log.txt'
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{today} - {timestamp}\n")
        f.write(f"Activity: {activity}\n")
        f.write(f"Practice time: {practice_time} minutes\n")
        f.write(f"Progress: Day {tracker['total_days'] + 1}\n")
        f.write("-" * 30 + "\n")
    
    # Update progress tracker
    tracker['total_days'] += 1
    tracker['last_commit_date'] = str(today)
    
    # Update streak logic
    if tracker['streak'] == 0:
        tracker['streak'] = 1
    else:
        last_date = datetime.datetime.strptime(tracker['last_commit_date'], '%Y-%m-%d').date()
        yesterday = today - datetime.timedelta(days=1)
        if last_date == yesterday:
            tracker['streak'] += 1
        else:
            tracker['streak'] = 1  # Reset streak if missed a day
    
    tracker['activities'].append({
        'date': str(today),
        'activity': activity,
        'minutes': practice_time,
        'timestamp': timestamp
    })
    
    # Save updated tracker
    with open(tracker_file, 'w') as f:
        json.dump(tracker, f, indent=2)
    
    return True

def create_daily_commit(project_dir):
    """Create a meaningful daily commit"""
    today = datetime.date.today()
    activities = [
        f"Daily coding practice - {today}",
        f"Progress update for {today.strftime('%B %d, %Y')}",
        f"Learning session - {today}",
        f"Code practice - {today}",
        f"Programming workout - {today}"
    ]
    
    activity = random.choice(activities)
    
    # Change to project directory
    original_dir = os.getcwd()
    os.chdir(project_dir)
    
    try:
        # Stage changes
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Create commit
        commit_msg = f"{activity} | Practice time: {random.randint(30, 120)}min"
        subprocess.run(['git', 'commit', '-m', commit_msg], 
                      check=True, capture_output=True)
        print(f"✅ Committed: {commit_msg}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Commit failed: {e}")
        return False
    finally:
        os.chdir(original_dir)

def main():
    print("🚀 Daily Coding Practice Tracker")
    print("=" * 40)
    
    # Initialize project
    print("📦 Initializing project structure...")
    project_dir = initialize_project()
    print(f"✅ Project initialized at: {project_dir}")
    
    # Log today's activity
    print("📝 Logging daily activity...")
    if log_daily_activity(project_dir):
        print("✅ Daily activity logged")
        
        # Create commit
        print("💾 Creating commit...")
        if create_daily_commit(project_dir):
            print("🎉 Daily contribution completed successfully!")
        else:
            print("❌ Failed to create commit")
    else:
        print("ℹ️  No activity to log (already committed today)")
    
    # Show progress
    tracker_file = project_dir / 'progress_tracker.json'
    with open(tracker_file, 'r') as f:
        tracker = json.load(f)
    
    print(f"\n📊 Current Progress:")
    print(f"   Total Days: {tracker['total_days']}")
    print(f"   Current Streak: {tracker['streak']} days")
    print(f"   Last Commit: {tracker['last_commit_date']}")
    
    print(f"\n🎯 Next Steps:")
    print(f"   1. Make this repository public on GitHub")
    print(f"   2. Push to your GitHub account: git push origin main")
    print(f"   3. Run this script daily to maintain your streak!")

if __name__ == "__main__":
    main()