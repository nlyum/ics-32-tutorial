# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693

# a3.py

import ds_client
import ds_protocol
import ui

from pathlib import Path
from shlex import split
import Profile

def main():
    main_loop()

def _get_port(): # get in a loop until the user inputs a port number
    try:
        print(ui.ENTER_PORT)
        port = int(input())
        return port
    except ValueError:
        print(ui.MUST_PORT_NUM)
        return _get_port()

def main_loop(username = '', password = '', address = '', port = 0, loaded_path = ''):
    while True:
        if loaded_path:
            print(f"Current profile path loaded: {loaded_path}")
        else:
            print(f"No profile currently loaded")

        print()
        print(ui.ENTER_A_COMMAND)
        user_command = input()
        
        if loaded_path:
            loaded_profile = Profile.Profile()
            loaded_profile.load_profile(loaded_path)
            address = loaded_profile.dsuserver
            username = loaded_profile.username
            password = loaded_profile.password
            bio = loaded_profile.bio
            port = 3021
            
        if user_command == "S":
            if loaded_path:
                s_line(address, port, loaded_path)
            else:
                print(ui.ERROR_LOAD_FILE)

        
        elif user_command == "M": # user tries to make a post
            if loaded_path:
                # send a message
                m_line(address, port, username, password)
            else:
                print(ui.ERROR_LOAD_FILE) # if the user hasn't opened a file yet, do that
                

        elif user_command == "B": # user tries to add/change a bio
            if loaded_path:
                # make a bio
                b_line(address, port, username, password)
            else:
                print(ui.ERROR_LOAD_FILE) # if the user hasn't opened a file yet, do that
        
        elif user_command == 'C':
            loaded_path = c_line()
        
        elif user_command == 'D':
            d_line()
        
        elif user_command == 'R':
            r_line()

        elif user_command == 'O':
            loaded_path = o_line()
        
        elif user_command == 'E':
            if loaded_path:
                e_line(loaded_path)
            else:
                print(ui.ERROR_LOAD_FILE)
        
        elif user_command == 'P':
            if loaded_path:
                p_line(loaded_path)
            else:
                print(ui.ERROR_LOAD_FILE)

        elif user_command == 'H':
            ui.list_commands()
        
        elif user_command == 'Q':
            break
        else:
            print(ui.ERROR_UNKNOWN_COMMAND)
            
        print()
        



    
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

def s_line(address, port, input_path):
    profile_to_scan = Profile.Profile()
    profile_to_scan.load_profile(input_path)
    
    print_profile_info(profile_to_scan)
    ui.s_line_tutorial()
    s_input = input()
    profile_posts = profile_to_scan.get_posts()
    username = profile_to_scan.username
    password = profile_to_scan.password
    bio = profile_to_scan.bio

    if s_input == "A":
        for i in range(len(profile_posts)):
            ds_client.send(address, port, username, password, profile_posts[i].get_entry())
        ds_client.send(address, port, username, password, '', bio)
    elif s_input == "B":
        if bio:
            ds_client.send(address, port, username, password, '', bio)
        else:
            print(ui.ERROR_NO_BIO)
    elif s_input == "P":
        for i in range(len(profile_posts)):
            ds_client.send(address, port, username, password, profile_posts[i].get_entry())
    elif s_input == "Q":
        print(ui.Q_RECEIVED)
        return
    else:
        try:
            post_id = int(s_input)
            ds_client.send(address, port, username, password, profile_posts[post_id].get_entry())
        except ValueError:
            print(ui.ERROR_INDEX_OVER)
        except:
            print(ui.UNKNOWN_COMMAND)


def b_line(address, port, username, password):
    print(ui.ENTER_BIO)
    bio = input()
    ds_client.send(address, port, username, password, '', bio)

def m_line(address, port, username, password):
    print(ui.ENTER_POST_MESSAGE)
    post_message = input()
    ds_client.send(address, port, username, password, post_message)

def d_line():
    delete_path = ''
    while True:
        print(ui.DLINE_GET_PATH)
        delete_path = input()
        if delete_path:
            if delete_path == "Q":
                return
            else:
                break
    del_file(delete_path)


def r_line():
    read_path = ''
    while True:
        print(ui.RLINE_GET_PATH)
        read_path = input()
        if read_path:
            if read_path == "Q":
                return
            else:
                break
    read_file(read_path)

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
    


def create_file(input_list, admin_bool):
    try:
        username = ''
        password = ''
        bio = ''
        dsuserver = ''
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
                dsuserver = input(ui.ENTER_ADDRESS)
                if dsuserver == "Q":
                    print(ui.Q_RECEIVED)
                    return
                
            new_profile = Profile.Profile(dsuserver, username, password)
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
    print()


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
                print_profile_info(profile_to_scan)
            else:
                print(f"ERROR: Command {command} not recognized - stopping prints")
                break
            i += 1
        
        

        profile_to_scan.save_profile(input_path)
    except Exception as ex:
        print(f"ERROR: {ex}")

def print_profile_info(profile: Profile.Profile):
    print(ui.TITLE_USERNAME, profile.username)
    print(ui.TITLE_PASSWORD, profile.password)
    print(ui.TITLE_BIO, profile.bio)
    print(ui.TITLE_POSTS)
    profile_posts = profile.get_posts()
    for i in range(len(profile_posts)):
        print(f"{i}: {profile_posts[i]["entry"]}")

    
if __name__ == "__main__":
    main()