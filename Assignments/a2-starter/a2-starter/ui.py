# Nathan Lyum
# nlyum@uci.edu
# 63833693

# ui.py

WELCOME_ENTER_COMMAND = "Welcome! Create a file with the 'C' command or open a DSU file with the 'O' command: "
ENTER_A_COMMAND = "Please enter a command (use the 'E' command to edit a file, 'P' to print information, or 'Q' to quit): "
ENTER_USERNAME = "Please enter your username: "
ENTER_PASSWORD = "Please enter your password: "
ENTER_BIO = "Please enter your bio: "
ERROR_LOAD_FILE = "ERROR: You must first create a file with the 'C' command or open a DSU file with the 'O' command."
ERROR_UNKNOWN_COMMAND = "ERROR: Command not recognized"
ERROR_C_GUIDE = "ERROR: To create a file, use format \"C <path> <option> <file name>\""
ERROR_D_GUIDE = "ERROR: To delete a file, use format \"D <path>\""
ERROR_R_GUIDE = "ERROR: To read a file, use format \"R <path>\""
ERROR_O_GUIDE = "ERROR: To open a file, use format \"O <path>\""
ERROR_E_GUIDE = "ERROR: To edit a profile, use format \"E <option> <additional arguments>\""
ERROR_P_GUIDE = "ERROR: To print data from a profile, use format \"P <option> <additional arguments>\""
ERROR_P_POSTID_GUIDE = "ERROR: Try format \"P -post <post ID>\""
ERROR_NOT_DSU = "ERROR: Not a DSU file"

TITLE_USERNAME = "Username:"
TITLE_PASSWORD = "Password:"
TITLE_BIO = "Bio:"
TITLE_POSTS = "Posts:"

CLINE_GET_PATH = "Great! Enter the directory you'd like to create the file in: "
CLINE_GET_FILENAME = "Okay, enter the name of the file you'd like to create: "

OLINE_GET_PATH = "Great! Enter the path of the file you'd like to load: "

ELINE_GET_OPTION = "Okay, enter an option to edit, or enter \"-h\" to get a list of options: "
ELINE_GET_USR = "Okay, enter the username you'd like to add: "
ELINE_GET_PWD = "Okay, enter the password you'd like to add: "
ELINE_GET_BIO = "Okay, enter the bio you'd like to add: "
ELINE_GET_ADDPOST = "Okay, enter the post you'd like to add: "
ELINE_GET_DELPOST = "Okay, enter the ID of the post you'd like to delete: "

Q_RECEIVED = "\"Q\" command received, quitting action..."

PLINE_GET_OPTION = "Okay, enter an option to print, or enter \"-h\" to get a list of options: "
PLINE_GET_POST_ID = "Okay, enter the ID of the post you'd like to view: "



def list_e_options():
    print("Enter \"-usr\" to edit the profile's username.")
    print("Enter \"-pwd\" to edit the profile's password.")
    print("Enter \"-bio\" to edit the profile's bio.")
    print("Enter \"-addpost\" to add a post to the profile.")
    print("Enter \"-delpost\" to delete a post from the profile.")
    print()

def list_p_options():
    print("Enter \"-usr\" to print the username of the profile object.")
    print("Enter \"-pwd\" to print the password of the profile object.")
    print("Enter \"-bio\" to print the bio of the profile object.")
    print("Enter \"-posts\" to print all posts stored in the profile.")
    print("Enter \"-post\" to print a specific post in the profile.")
    print("Enter \"-all\" to print all information stored in the profile.")
    print()
