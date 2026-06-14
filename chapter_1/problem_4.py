# write a python programto print the content of the directory using the os module .
# search online from the function which does that
import os

path = "."

print("Directory contents with details:")

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print("FILE  :", entry.name)
        elif entry.is_dir():
            print("FOLDER:", entry.name)