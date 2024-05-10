# Nathan Lyum
# nlyum@uci.edu
# 63833693

# a2.py

from pathlib import Path
from shlex import split
import Profile
import ui

def main():
    input_string = input(ui.WELCOME_ENTER_COMMAND)
    input_string = input_string.replace('\\', '/')
    user_inputs = split(input_string)
    loaded_path = None
    
    while True:
        user_command = user_inputs[0]
        user_args = len(user_inputs) - 1

        if user_command == 'C':
            if user_args == 3:
                loaded_path = create_file(user_inputs[1:])
            else:
                print(ui.ERROR_C_GUIDE)
        
        elif user_command == 'D':
            if user_args == 1:
                del_file(user_inputs[1])
            else:
                print(ui.ERROR_D_GUIDE)
        
        elif user_command == 'R':
            if user_args == 1:
                read_file(user_inputs[1])
            else:
                print(ui.ERROR_R_GUIDE)
        
        elif user_command == 'O':
            if user_args == 1:
                loaded_path = open_file(user_inputs[1])
            else:
                print(ui.ERROR_O_GUIDE)
        
        elif user_command == 'E':
            if user_args in (2, 3):
                if loaded_path:
                    edit_file(user_inputs[1:], loaded_path)
                else:
                    print(ui.ERROR_LOAD_FILE)
            else:
                print(ui.ERROR_E_GUIDE)
        
        elif user_command == 'P':
            if user_args in (1, 2):
                if loaded_path:
                    print_data(user_inputs[1:], loaded_path)
                else:
                    print(ui.ERROR_LOAD_FILE)
            else:
                print(ui.ERROR_P_GUIDE)
            
        
        elif user_command == 'admin':
            enter_admin_mode()
        elif user_command == 'Q':
            break
        else:
            print(ui.ERROR_UNKNOWN_COMMAND)
        
        if loaded_path:
            print(f"Current profile path loaded: {loaded_path}")
        else:
            print(f"No profile currently loaded")
        
        input_string = input(ui.ENTER_A_COMMAND)
        input_string = input_string.replace('\\', '/')
        user_inputs = split(input_string)

def enter_admin_mode():
    ui.ENTER_A_COMMAND = ""
    ui.ENTER_USERNAME = ""
    ui.ENTER_BIO = ""
    ui.ENTER_PASSWORD = ""

def create_file(input_list):
    try:
        location = input_list[0]
        option = input_list[1]    
        file_name = input_list[2]

        if option == "-n":
            location_path = Path(location)
            location_path.mkdir(exist_ok = True)
            
            file_path = location_path / (file_name + ".dsu")

            
            username = input(ui.ENTER_USERNAME)
            password = input(ui.ENTER_PASSWORD)
            bio = input(ui.ENTER_BIO)
            new_profile = Profile.Profile(file_name, username, password)
            new_profile.bio = bio
            f = file_path.open("w")
            f.close
            new_profile.save_profile(file_path)

            print(file_path)
            return file_path
        else:
            print(f"ERROR: option \"{option}\" not recognized, use \"-n\" to create a file")
    except Exception as ex:
        print(f"ERROR: {ex}")

def del_file(input_path):
    try:
        file_path = Path(input_path)
        if file_path.suffix == ".dsu":
            file_path.unlink()
            print(f"{file_path} DELETED")
        else:
            print("ERROR: not dsu")
    except IndexError:
        print(f"ERROR: Wrong number of inputs, try using format \"D <path>\"")
    except Exception as ex:
        print(f"ERROR: {ex}")


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
                print(f"ERROR: not dsu")
        else:
            print("EMPTY")
        f.close()
    except Exception as ex:
        print(f"ERROR: {ex}")

def open_file(input_path):
    try:
        file_path = Path(input_path)
        f = file_path.open("r")
        if f.read(1):
            f.close()
            f = file_path.open("r")
            if file_path.suffix == ".dsu":
                return file_path
            else:
                print(f"ERROR: not a DSU file")
        else:
            print("EMPTY")
        f.close()
    except Exception as ex:
        print(f"ERROR: {ex}")

def edit_file(input_list, input_path):
    try:
        profile_to_edit = Profile.Profile()
        profile_to_edit.load_profile(input_path)
        if len(input_list) % 2 != 0:
            print(f"ERROR: odd number of edit arguments")
            return
        command_list = []
        for i in range(len(input_list) // 2):
            command_list.append([input_list[2 * i], input_list[2 * i + 1]])
        
        for command_pair in command_list:
            command = command_pair[0]
            arg = command_pair[1]
            if command == "-usr":
                profile_to_edit.username = arg
                print(f"Username changed to: {arg}")
            elif command == "-pwd":
                profile_to_edit.password = arg
                print(f"Password changed to: {arg}")
            elif command == "-bio":
                profile_to_edit.bio = arg
                print(f"Bio changed to: {arg}")
            elif command == "-addpost":
                post_to_add = Profile.Post("arg")
                profile_to_edit.add_post(post_to_add)
                print(f"Added post: {arg}")
            elif command == "-delpost":
                if not profile_to_edit.del_post(int(arg)):
                    print(f"ERROR: Unable to delete post #{arg}, continuing edits")
                else:
                    print(f"Deleted post with id: {arg}")
            else:
                print(f"ERROR: Command {command} not recognized, continuing edits")
                continue

        profile_to_edit.save_profile(input_path)
    except Exception as ex:
        print(f"ERROR: {ex}")

def print_data(input_list, input_path):
    try:
        profile_to_scan = Profile.Profile()
        profile_to_scan.load_profile(input_path)
        command = input_list[0]
        
        if command == "-usr":
            print(profile_to_scan.username)
        elif command == "-pwd":
            print(profile_to_scan.password)
        elif command == "-bio":
            print(profile_to_scan.bio)
        elif command == "-posts":
            profile_posts = profile_to_scan.get_posts()
            for i in range(len(profile_posts)):
                print(f"{i}: {profile_posts[i]["entry"]}")
        elif command == "-post":
            try:
                if len(input_list) > 1:
                    post_id = int(input_list[1])
                    print(profile_to_scan.get_posts()[post_id])
                else:
                    print(f"ERROR: Try format \"P -post <post ID>\"")
            except:
                print(f"ERROR: post with ID {input_list[1]} not found")
        else:
            print(f"ERROR: Command {command} not recognized, continuing actions")

        profile_to_scan.save_profile(input_path)
    except Exception as ex:
        print(f"ERROR: {ex}")

if __name__ == "__main__":
    main()