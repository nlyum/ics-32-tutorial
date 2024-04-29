#lab5.py

# Starter code for lab 5 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Nathan Lyum
# nlyum@uci.edu
# 63833693

# ---------------------
from pathlib import Path

class Note:
    def __init__(self, path):
        self.note_path = path
        f = self.note_path.open("r")
        self.notes_list = f.readlines()
        f.close()

    def read_notes(self):
        return self.notes_list

    def save_note(self, note_to_add):
        f = self.note_path.open("a")
        f.write(note_to_add)
        f.write('\n')
        f.close()

    def remove_note(self, remove_id):
        removed_note = ''
        f = self.note_path.open("w")
        id = 0
        for line in self.notes_list:
            if id == remove_id:
                removed_note = line
            else:
                f.write(line)        
            id += 1
        f.close()
        return removed_note

# ---------------------

def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1

def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def run():
    p = Path("C:/Users/natha/OneDrive/Desktop/UCI/ICS32/Assignments") / "lab5_notes.txt" # hopefully I'm allowed to replace these with my own filepath
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print("Here are your notes: \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    run()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    run()
