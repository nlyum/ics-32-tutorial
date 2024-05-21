# Nathan Lyum
# nlyum@uci.edu
# 63833693

# a2.py

from pathlib import Path
from shlex import split
import Profile
import ui

def main():
    try:
        input_string = input(ui.WELCOME_ENTER_COMMAND)
        print()
        user_inputs = split_input(input_string)
        loaded_path = None
        admin_bool = False
    except Exception as ex:
        print(f"ERROR: {ex}")
        main()

    while True:
        try:
            user_command = user_inputs[0]
            user_args = len(user_inputs) - 1

            if user_command == 'C':
                if user_args == 3:
                    loaded_path = create_file(user_inputs[1:], admin_bool)
                else:
                    loaded_path = c_line()
            
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
                    loaded_path = o_line()
            
            elif user_command == 'E':
                if loaded_path:
                    if user_args > 1:
                        edit_file(user_inputs[1:], loaded_path)
                    else:
                        e_line(loaded_path)
                else:
                    print(ui.ERROR_LOAD_FILE)
            
            elif user_command == 'P':
                if loaded_path:
                    if user_args > 0:
                        print_data(user_inputs[1:], loaded_path)
                    else:
                        p_line(loaded_path)
                else:
                    print(ui.ERROR_LOAD_FILE)
                
            
            elif user_command == 'admin':
                enter_admin_mode()
                admin_bool = True
            elif user_command == 'Q':
                break
            else:
                print(ui.ERROR_UNKNOWN_COMMAND)
            
            print()
            if loaded_path:
                print(f"Current profile path loaded: {loaded_path}")
                input_string = input(ui.ENTER_A_COMMAND)
            else:
                print(f"No profile currently loaded")
                input_string = input(ui.WELCOME_ENTER_COMMAND)

            print()
            input_string = input_string.replace('\\', '/')
            user_inputs = split(input_string)
        except Exception as ex:
            print(f"ERROR: {ex}")
    
def split_input(input_string):
    input_string = input_string.replace('\\', '/')
    return split(input_string)

def organize_elem(input_string):
    input_string = input_string.replace('\\', '/')
    return split(input_string)[0]

def c_line():
    c_inputs = ['', '-n', '']
    c_inputs[0] = organize_elem(input(ui.CLINE_GET_PATH))
    if c_inputs[0] == "Q":
        print(ui.Q_RECEIVED)
        return
    c_inputs[2] = organize_elem(input(ui.CLINE_GET_FILENAME))
    if c_inputs[2] == "Q":
        print(ui.Q_RECEIVED)
        return
    return create_file(c_inputs, False)

def o_line():
    o_input = input(ui.OLINE_GET_PATH)
    if o_input == "Q":
        print(ui.Q_RECEIVED)
        return
    return open_file(o_input)

def e_line(path):
    e_inputs = []
    e_inputs.append(input(ui.ELINE_GET_OPTION))
    while True:
        if e_inputs[0] != "-h":
            break
        else:
            ui.list_e_options()
            e_inputs[0] = input(ui.ELINE_GET_OPTION)
    
    if e_inputs[0] == "-usr":
        e_inputs.append(input(ui.ELINE_GET_USR))
    elif e_inputs[0] == "-pwd":
        e_inputs.append(input(ui.ELINE_GET_PWD))
    elif e_inputs[0] == "-bio":
        e_inputs.append(input(ui.ELINE_GET_BIO))
    elif e_inputs[0] == "-addpost":
        e_inputs.append(input(ui.ELINE_GET_ADDPOST))
    elif e_inputs[0] == "-delpost":
        e_inputs.append(input(ui.ELINE_GET_DELPOST))
    elif e_inputs[0] == "Q":
        print(ui.Q_RECEIVED)
        return
    
    if len(e_inputs) > 1:
        if e_inputs[1] == "Q":
            print(ui.Q_RECEIVED)
            return

    edit_file(e_inputs, path)


def p_line(path):
    p_inputs = []
    p_inputs.append(input(ui.PLINE_GET_OPTION))
    while True:
        if p_inputs[0] != "-h":
            break
        else:
            ui.list_p_options()
            p_inputs[0] = input(ui.PLINE_GET_OPTION)
    
    if p_inputs[0] == "-post":
        p_inputs.append(input(ui.PLINE_GET_POST_ID))
    elif p_inputs[0] == "Q":
        print(ui.Q_RECEIVED)
        return
    
    print_data(p_inputs, path)
    

def enter_admin_mode():
    ui.ENTER_A_COMMAND = ""
    ui.ENTER_USERNAME = ""
    ui.ENTER_BIO = ""
    ui.ENTER_PASSWORD = ""


def create_file(input_list, admin_bool):
    try:
        username = ''
        password = ''
        bio = ''
        location = input_list[0]
        option = input_list[1]    
        file_name = input_list[2]

        if option == "-n":
            location_path = Path(location)
            location_path.mkdir(exist_ok = True)
            
            file_path = location_path / (file_name + ".dsu")

            if not admin_bool:
                username = input(ui.ENTER_USERNAME)
                if username == "Q":
                    print(ui.Q_RECEIVED)
                    return
                password = input(ui.ENTER_PASSWORD)
                if password == "Q":
                    print(ui.Q_RECEIVED)
                    return
                bio = input(ui.ENTER_BIO)
                if bio == "Q":
                    print(ui.Q_RECEIVED)
                    return
            new_profile = Profile.Profile(file_name, username, password)
            new_profile.bio = bio
            f = file_path.open("w")
            f.close
            new_profile.save_profile(file_path)

            print(file_path)
            return file_path
        elif option == "Q":
            print(ui.Q_RECEIVED)
            return
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
            print(ui.ERROR_NOT_DSU)
    except IndexError:
        print(ui.ERROR_D_GUIDE)
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
                print(ui.ERROR_NOT_DSU)
        else:
            print("EMPTY")
        f.close()
    except Exception as ex:
        print(f"ERROR: {ex}")


def open_file(input_path):
    try:
        file_path = Path(input_path)
        f = file_path.open("r")
        if file_path.suffix == ".dsu":
            print(f"Successfully loaded file at path {file_path}")
            return file_path
        else:
            print(ui.ERROR_NOT_DSU)
        f.close()
    except Exception as ex:
        print(f"ERROR: {ex}")


def edit_file(input_list, input_path):
    try:
        profile_to_edit = Profile.Profile()
        profile_to_edit.load_profile(input_path)
        if len(input_list) % 2 != 0:
            print(f"ERROR: invalid amount of edit arguments")
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
                post_to_add = Profile.Post(arg)
                profile_to_edit.add_post(post_to_add)
                print(f"Added post: {arg}")
            elif command == "-delpost":
                if not profile_to_edit.del_post(int(arg)):
                    print(f"ERROR: Unable to delete post with ID {arg}, ending edits")
                    break
                else:
                    print(f"Deleted post with ID: {arg}")
            else:
                print(f"ERROR: Command {command} not recognized, ending edits")
                break

        profile_to_edit.save_profile(input_path)
    except Exception as ex:
        print(f"ERROR: {ex}")


def print_data(input_list, input_path):
    try:
        profile_to_scan = Profile.Profile()
        profile_to_scan.load_profile(input_path)
        
        i = 0
        while i < len(input_list):
            command = input_list[i]
            if command == "-usr":
                print(ui.TITLE_USERNAME)
                print(profile_to_scan.username)
            elif command == "-pwd":
                print(ui.TITLE_PASSWORD)
                print(profile_to_scan.password)
            elif command == "-bio":
                print(ui.TITLE_BIO)
                print(profile_to_scan.bio)
            elif command == "-posts":
                print(ui.TITLE_POSTS)
                profile_posts = profile_to_scan.get_posts()
                for i in range(len(profile_posts)):
                    print(f"{i}: {profile_posts[i]["entry"]}")
            elif command == "-post":
                try:
                    if len(input_list) > 1:
                        print(f"Post with ID {input_list[i + 1]}")
                        post_id = int(input_list[i + 1])
                        print(profile_to_scan.get_posts()[post_id]["entry"])
                        i += 1
                    else:
                        print(ui.ERROR_P_POSTID_GUIDE, " - stopping prints")
                        break
                except:
                    print(f"ERROR: post with ID {input_list[1]} not found")
            elif command == "-all":
                print(ui.TITLE_USERNAME, profile_to_scan.username)
                print(ui.TITLE_PASSWORD, profile_to_scan.password)
                print(ui.TITLE_BIO, profile_to_scan.bio)
                print(ui.TITLE_POSTS)
                profile_posts = profile_to_scan.get_posts()
                for i in range(len(profile_posts)):
                    print(f"{i}: {profile_posts[i]["entry"]}")
            else:
                print(f"ERROR: Command {command} not recognized - stopping prints")
                break
            i += 1
        
        

        profile_to_scan.save_profile(input_path)
    except Exception as ex:
        print(f"ERROR: {ex}")


if __name__ == "__main__":
    main()