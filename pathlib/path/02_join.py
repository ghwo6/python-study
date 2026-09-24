import os
from pathlib import Path

dir_name = "dir"
sub_dir_name = "sub_dir_name"
file_name = "file"

# os.path
file = os.path.join(dir,sub_dir_name,file_name)

# pathlib
dir = Path(dir_name)
# file = dir / sub_dir_name / file

file :Path= Path(dir_name) / sub_dir_name / file
