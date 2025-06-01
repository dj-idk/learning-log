#!/usr/bin/env python3
import os
import datetime
import git
import configparser
import sys
from pathlib import Path

def get_config():
    """Get or create configuration for the tool."""
    config_dir = Path.home() / ".config" / "log-learning"
    config_file = config_dir / "config.ini"
    
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    
    config = configparser.ConfigParser()
    
    if config_file.exists():
        config.read(config_file)
    else:
        print("First-time setup for log-learning:")
        repo_path = input("Enter the path to your logs repository: ")
        
        # Convert to absolute path and normalize
        repo_path = os.path.abspath(os.path.expanduser(repo_path))
        
        # Check if it's a git repo or initialize one
        if not os.path.exists(os.path.join(repo_path, '.git')):
            if not os.path.exists(repo_path):
                os.makedirs(repo_path, exist_ok=True)
                print(f"Created directory: {repo_path}")
            
            try:
                print(f"Initializing git repository at {repo_path}...")
                git.Repo.init(repo_path)
                print("Git repository initialized successfully.")
            except Exception as e:
                print(f"Failed to initialize git repository: {e}")
                sys.exit(1)
        
        config['DEFAULT'] = {
            'repo_path': repo_path
        }
        
        with open(config_file, 'w') as f:
            config.write(f)
    
    return config['DEFAULT']

def prompt_questions():
    """Prompt the user with learning reflection questions."""
    questions = [
        "What did I learn today?",
        "How did I apply what I learned?",
        "What was challenging or confusing?",
        "What's next / What do I want to learn tomorrow?"
    ]
    
    answers = []
    print("Daily Learning Log:")
    print("------------------")
    for question in questions:
        print(f"\n{question}")
        print("(Enter a blank line when finished)")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        answers.append("\n".join(lines))
    
    return questions, answers

def create_log_file(repo_path, questions, answers):
    """Create a log file with the given answers."""
    today = datetime.datetime.now()
    year_dir = os.path.join(repo_path, str(today.year))
    month_dir = os.path.join(year_dir, f"{today.month:02d}")
    
    os.makedirs(month_dir, exist_ok=True)
    
    log_file = os.path.join(month_dir, f"{today.day:02d}.md")
    
    # Check if file already exists and handle accordingly
    if os.path.exists(log_file):
        overwrite = input(f"Log file for today already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            sys.exit(0)
    
    with open(log_file, 'w') as f:
        f.write(f"# Learning Log: {today.strftime('%Y-%m-%d')}\n\n")
        for i, (question, answer) in enumerate(zip(questions, answers)):
            f.write(f"## {question}\n\n{answer}\n\n")
    
    return log_file

def commit_and_push(repo_path, log_file):
    """Commit the new log file and push to remote."""
    try:
        repo = git.Repo(repo_path)
        
        # Check if the file is new or modified
        relative_path = os.path.relpath(log_file, repo_path)
        status = repo.git.status('--porcelain', relative_path)
        
        if not status:
            print("No changes to commit.")
            return True
        
        repo.git.add(log_file)
        
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        repo.git.commit(m=f"Add learning log for {today}")
        
        # Check if remote exists before pushing
        try:
            remotes = list(repo.remotes)
            if remotes:
                remote_name = remotes[0].name
                print(f"Pushing to remote '{remote_name}'...")
                repo.git.push(remote_name)
                print(f"\nSuccessfully added log for {today} and pushed to remote!")
            else:
                print("\nLog committed locally but no remote repository found.")
                print("To add a remote repository, use: git remote add origin <repository-url>")
        except git.GitCommandError as e:
            print(f"Failed to push: {e}")
            print("Your changes have been committed locally.")
            return False
        
    except git.GitCommandError as e:
        print(f"Git error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    return True

def main():
    """Main entry point for the CLI tool."""
    try:
        config = get_config()
        repo_path = config['repo_path']
        
        if not os.path.exists(repo_path):
            print(f"Error: Repository path {repo_path} does not exist.")
            sys.exit(1)
        
        questions, answers = prompt_questions()
        
        log_file = create_log_file(repo_path, questions, answers)
        
        commit_and_push(repo_path, log_file)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()