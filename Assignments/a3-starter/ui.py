# Nathan Lyum
# nlyum@uci.edu
# 63833693

# ui.py

ENTER_A_COMMAND = "Please enter a command (type \"H\" for a list of commands): "

ENTER_ADDRESS = "Enter the IP address: "
ENTER_PORT = "Enter the port: "

ENTER_USERNAME = "Okay, enter your username: "
ENTER_PASSWORD = "Enter your password: "

ENTER_POST_MESSAGE = "Enter the post you'd like to make: "
ENTER_BIO = "Enter a bio: "

SUCCESS_JOIN = "Username and password accepted!"

MUST_JOIN = "Sorry, please join a server first!"
MUST_PORT_NUM = "The port number must be an integer, please try again."

UNKNOWN_COMMAND = "Sorry, command not recognized."

WELCOME_ENTER_COMMAND = "Welcome! Create a file with the 'C' command or open a DSU file with the 'O' command: "
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
ERROR_INDEX_OVER = "ERROR: Listed index out of range"
ERROR_NO_BIO = "ERROR: Bio is all whitespace or does not exist"


TITLE_USERNAME = "Username:"
TITLE_PASSWORD = "Password:"
TITLE_BIO = "Bio:"
TITLE_POSTS = "Posts:"

CLINE_GET_PATH = "Great! Enter the directory you'd like to create the file in: "
CLINE_GET_FILENAME = "Okay, enter the name of the file you'd like to create: "

DLINE_GET_PATH = "Okay, enter the file path of the file you'd like to delete: "

RLINE_GET_PATH = "Okay, enter the file path of the file you'd like to read: "


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

SERVER_MSG = "Message from server: "

def list_commands():
    print("S: Send a post or bio to a server")
    print("C: Create a file")
    print("O: Open a file")
    print("D: Delete a file")
    print("R: Read a file")
    print("E: Edit a file")
    print("P: Print information from a file")
    print("H: Get a list of commands")
    print("Q: Quit program")

def s_line_tutorial():
    print("Enter the command of what you'd like to send to the server, or the number ID of the post you'd like to upload:")
    print("A: Send all posts and bio to server")
    print("B: Send bio to server")
    print("P: Send all posts to server")
    print("Q: Quit and return to the main menu")

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
