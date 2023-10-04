# This script is only a testing...
from pathlib import Path

PROJECT_NAME = 'py-edge-detect-image'

def get_rootProject(path: Path = Path.cwd()) -> Path:
    if str(path).endswith(PROJECT_NAME): return path
    return get_rootProject(path.parent)

print(get_rootProject())