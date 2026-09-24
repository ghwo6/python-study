import os

from pathlib import Path

file_path_string = './path/to/file'

if os.path.exists(file_path_string):
    ...
p = Path(file_path_string)

if p.exists():
    ...

