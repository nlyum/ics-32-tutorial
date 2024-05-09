# Nathan Lyum
# nlyum@uci.edu
# 63833693

# a2.py

from pathlib import Path
from shlex import split
import Profile

ENTER_A_COMMAND = "Please enter a command: "
ENTER_USERNAME = "Please enter your username: "
ENTER_PASSWORD = "Please enter your password: "
ENTER_BIO = "Please enter your bio: "

def main():
    input_string = input(ENTER_A_COMMAND)
    input_string = input_string.replace('\\', '/')
    user_inputs = split(input_string)
    
    
    while True:
        user_command = user_inputs[0]
        if user_command == 'C':
            create_file(user_inputs[1:])
        elif user_command == 'D':
            del_file(user_inputs[1])
        elif user_command == 'R':
            read_file(user_inputs[1])
        elif user_command == 'O':
            open_file(user_inputs[1])
        elif user_command == 'Q':
            break
        else:
            print("ERROR: command not recognized")
        input_string = input(ENTER_A_COMMAND)
        input_string = input_string.replace('\\', '/')
        user_inputs = split(input_string)

def create_file(input_list):
    location = input_list[0]
    # print(f"File location: {location}")
    option = input_list[1]    
    file_name = input_list[2]
    # print(f"File name: {file_name}")

    if option == "-n":
        location_path = Path(location)
        location_path.mkdir(exist_ok = True)
        
        file_path = location_path / (file_name + ".dsu")

        f = file_path.open("w")
        f.close
        username = input(ENTER_USERNAME)
        password = input(ENTER_PASSWORD)
        bio = input(ENTER_BIO)
        new_profile = Profile.Profile(file_name, username, password)
        new_profile.save_profile(file_path)

        print(file_path)
    else:
        print("ERROR: command not recognized")

def del_file(input_path):
    file_path = Path(input_path)
    if file_path.suffix == ".dsu":
        file_path.unlink()
        print(f"{file_path} DELETED")
    else:
        print("ERROR: not dsu")


def read_file(input_path):
    file_path = Path(input_path)
    f = file_path.open("r")
    if f.read(1):
        f.close()
        f = file_path.open("r")
        if file_path.suffix == ".dsu":
            for line in f.readlines():
                print(line, end = '')
        else:
            print(f"ERROR: not dsu")
    else:
        print("EMPTY")
    f.close()

def open_file(input_path):
    pass

if __name__ == "__main__":
    main()