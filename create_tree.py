import os
from pathlib import Path
import fnmatch

def load_gitignore_patterns():
    # List of folder/file names to ignore
    return [
        "myvenv_311",
        "myvenv_313",
        "mlruns",
        "venv",
        ".env",
        "__pycache__",
        "Artifacts",
        "logs",
        ".git",
    ]

def is_ignored(path, patterns):
    # Normalize path to use forward slashes for consistency
    normalized_path = path.replace(os.sep, '/')
    
    for pattern in patterns:
        # Ignore if the basename matches any pattern exactly
        if fnmatch.fnmatch(os.path.basename(normalized_path), pattern):
            return True
        # Ignore if the pattern matches the start of the path or is a parent folder in the path
        if fnmatch.fnmatch(normalized_path, f"{pattern}*") or f"/{pattern}/" in f"/{normalized_path}/":
            return True
    return False

def print_tree(path='.', prefix='', max_depth=3, level=0, ignore_patterns=[]):
    if level > max_depth:
        return
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        return

    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        rel_path = os.path.relpath(full_path, '.')
        
        if is_ignored(rel_path, ignore_patterns):
            continue

        connector = "├── " if i < len(entries) - 1 else "└── "
        print(prefix + connector + entry)

        if os.path.isdir(full_path):
            extension = "│   " if i < len(entries) - 1 else "    "
            print_tree(full_path, prefix + extension, max_depth, level + 1, ignore_patterns)

# Load ignore patterns
ignore_patterns = load_gitignore_patterns()

# Print the directory tree, excluding ignored files/folders
print_tree('.', max_depth=3, ignore_patterns=ignore_patterns)
