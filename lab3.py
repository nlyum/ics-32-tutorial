#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Nathan Lyum
# nlyum@uci.edu
# 63833693

def welcome():
    print("Welcome to PyNote!")

def show_notes():
    print("Here are your notes:\n")
    f = open("pynote.txt", "r+")
    for line in f.readlines():
        print(line)

    f.close()

def begin_writing():
    welcome()
    show_notes()
    f = open("pynote.txt", "a")
    next_line = input("Please enter a new note (enter q to exit): ")
    while next_line != 'q':
        f.write(next_line)
        f.write('\n')
        next_line = input("Please enter a new note (enter q to exit): ")

    f.close()

if __name__ == "__main__":
    begin_writing()