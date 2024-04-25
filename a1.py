# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nathan Lyum
# nlyum@uci.edu
# 63833693


from pathlib import Path
from shlex import split

def run_file_explorer():
    user_inputs = split(input("Please input your command: "))
    user_command = user_inputs[0]
    if user_command == 'C':
        create_file(user_inputs[1:])


def create_file(input_list):
    print(input_list)
    location = input_list[0]


def del_file():
    pass

def read_file():
    pass

if __name__ == "__main__":
    run_file_explorer()