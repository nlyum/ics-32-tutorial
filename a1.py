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
    elif user_command == 'D':
        del_file(user_inputs[1])
    elif user_command == 'R':
        read_file(user_inputs[1])
    


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
        print("created your file")


def del_file(input_path):
    file_path = Path(input_path)
    if file_path.suffix == ".dsu":
        try:
            file_path.unlink()
            print(f"{input_path} DELETED")
        except FileNotFoundError:
            print("it's not there bozo")
    else:
        print("ERROR")
        run_file_explorer()


def read_file(input_list):
    pass

if __name__ == "__main__":
    print(Path.cwd())
    run_file_explorer()