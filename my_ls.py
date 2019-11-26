import os
from pprint import pprint
from pathlib import Path

def take_path():
    path = input("Choose directory to inspect. If current pass 'current'.")

    if path.lower() == 'current':
        abs = Path().absolute()
        dirlist = os.listdir(abs)
    else:
        dirlist = os.listdir(path)
    pprint(dirlist)

while True:
    take_path()