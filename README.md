````markdown
# Log Learning CLI Tool

A simple command-line tool to track your daily learning progress and automatically push logs to GitHub.

## Features

- Daily learning reflection through guided questions
- Automatic organization of logs by year/month/day
- Git integration for version control and backup
- Simple command-line interface accessible from anywhere

## Installation

### Prerequisites

- Python 3.6+
- Git installed and configured

### Install from source

```bash
# Clone the repository
git clone https://github.com/yourusername/learning-log.git
cd learning-log

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```
````

### Add to PATH

Make sure the Python scripts directory is in your PATH:

**Windows PowerShell:**

```powershell
$env:PATH += ";C:\Path\To\Python\Scripts"
```

**Linux/macOS:**

```bash
export PATH="$PATH:$HOME/.local/bin"
```

## Usage

### First-time setup

Run the tool for the first time to set up your logs repository:

```bash
log-learning
```

You'll be prompted to provide the path to your logs repository. If the repository doesn't exist, it will be created and initialized as a Git repository.

### Daily logging

1. Open any terminal and run:

```bash
log-learning
```

2. Answer the four reflection questions:

   - What did I learn today?
   - How did I apply what I learned?
   - What was challenging or confusing?
   - What's next / What do I want to learn tomorrow?

3. Enter a blank line (press Enter twice) when you're done with each question.

4. Your log will be saved in the format `YYYY/MM/DD.md` and automatically committed to Git.

### GitHub Integration

To push your logs to GitHub:

1. Create a GitHub repository for your logs
2. Add the remote to your local repository:

```bash
cd path/to/your/logs/repository
git remote add origin https://github.com/yourusername/your-logs-repo.git
git push -u origin main
```

After setting up the remote, the tool will automatically push your logs to GitHub.

## Log Format

Logs are stored as Markdown files with the following structure:

```markdown
# Learning Log: YYYY-MM-DD

## What did I learn today?

Your answer here...

## How did I apply what I learned?

Your answer here...

## What was challenging or confusing?

Your answer here...

## What's next / What do I want to learn tomorrow?

Your answer here...
```

## Configuration

Configuration is stored in `~/.config/log-learning/config.ini` and includes:

- `repo_path`: Path to your logs repository

Now you have all the necessary files to push your project to GitHub:

1. Initialize a Git repository in your project folder (if not already done):

```bash
cd C:\Programming Projects\Python\learning-log
git init
```

2. Add all files:

```bash
git add .
```

3. Commit the files:

```bash
git commit -m "Initial commit of log-learning CLI tool"
```

4. Create a new repository on GitHub (without initializing it with README, .gitignore, or license)

5. Add the remote and push:

```bash
git remote add origin https://github.com/yourusername/learning-log.git
git push -u origin main
```

Replace `yourusername` with your actual GitHub username and adjust the repository name if needed.
