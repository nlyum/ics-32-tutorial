import tkinter as tk


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class StudentRegistrationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Student Registration")

        # Label and entry for student name
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        # Label and entry for student course
        self.course_label = tk.Label(master, text="Course:")
        self.course_label.grid(row=1, column=0, sticky=tk.W)
        self.course_entry = tk.Entry(master)
        self.course_entry.grid(row=1, column=1)

        # Button for registering a student
        self.register_button = tk.Button(
            master, text="Register", command=self.register_student
        )
        self.register_button.grid(row=2, column=0, columnspan=2)

        # Button for removing a student
        self.remove_button = tk.Button(
            master, text="Remove Student", command=self.remove_student
        )
        self.remove_button.grid(row=3, column=0, columnspan=2)

        # Text box for displaying registered students
        self.registered_textbox = tk.Text(master, height=10, width=40)
        self.registered_textbox.grid(row=4, column=0, columnspan=2)

        # List to store registered students
        self.registered_students = []

    # Method to register a student
    def register_student(self):
        name = self.name_entry.get()
        course = self.course_entry.get()

        # Check if the student is already registered
        if self.is_duplicate(name, course):
            # Display error message if student is duplicate
            self.display_error("Student is already registered!")
        else:
            new_student = Student(name, course)
            self.registered_students.append(new_student)
            self.display_registration(new_student)

    # Method to remove a student
    def remove_student(self):
        if self.registered_students:
            removed_student = self.registered_students.pop()
            self.display_removal(removed_student)

    # Method to check for duplicate student
    def is_duplicate(self, name, course):
        for student in self.registered_students:
            if student.name == name and student.course == course:
                return True
        return False

    # Method to display registration details
    def display_registration(self, student):
        registration_message = (
            f"Student Registered:\nName: {student.name}\nCourse: {student.course}"
        )
        self.registered_textbox.insert(tk.END, registration_message + "\n")

    # Method to display removal details
    def display_removal(self, student):
        removal_message = (
            f"Student Removed:\nName: {student.name}\nCourse: {student.course}"
        )
        self.registered_textbox.insert(tk.END, removal_message + "\n")

    # Method to display error message
    def display_error(self, message):
        error_message = f"Error: {message}"
        self.registered_textbox.insert(tk.END, error_message + "\n")
        self.registered_textbox.tag_add("error", "end-1l", "end")
        self.registered_textbox.tag_config("error", foreground="red")


if __name__ == "__main__":
    root = tk.Tk()
    gui = StudentRegistrationGUI(root)
    root.mainloop()
