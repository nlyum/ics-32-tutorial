# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nathan Lyum
# nlyum@uci.edu
# 63833693


from pathlib import Path
from shlex import split
from re import sub

def main():
    try:
        input_string = input()
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
            elif user_command == 'Q':
                break
            else:
                print("ERROR")
            input_string = input()
            input_string = input_string.replace('\\', '/')
            user_inputs = split(input_string)

    except:
        print("ERROR")
        main()

    


def create_file(input_list):
    try:
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
            print(file_path)
        else:
            print("ERROR")
    except:
        print("ERROR")

def del_file(input_path):
    try:
        file_path = Path(input_path)
        if file_path.suffix == ".dsu":
            file_path.unlink()
            print(f"{file_path} DELETED")
        else:
            print("ERROR")
    except:
        print("ERROR")


def read_file(input_path):
    try:
        file_path = Path(input_path)
        f = file_path.open("r")
        if f.read(1):
            f.close()
            f = file_path.open("r")
            if file_path.suffix == ".dsu":
                for line in f.readlines():
                    print(line, end = '')
            else:
                print(f"ERROR")
        else:
            print("EMPTY")
        f.close()
    except:
        print(f"ERROR")
    

if __name__ == "__main__":
    main()