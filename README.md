# Project C

Private repository that uses Project A and Project B as git submodules.

## Structure

```
project-c/
├── main.py                    # Main program using A and B
├── project-a/                 # Git submodule
├── project-b/                 # Git submodule
└── output/
    └── result.json            # Generated content
```

## Workflow

1. GitHub Actions triggers daily at 3:00 AM UTC
2. Updates submodules to latest commits
3. Runs `main.py` to generate new content
4. Commits generated result back to repository

## Manual Setup

```bash
# Clone with submodules
git clone --recursive https://github.com/YOUR_USERNAME/project-c.git

# Update submodules
git submodule update --remote --merge

# Run locally
python main.py
```
