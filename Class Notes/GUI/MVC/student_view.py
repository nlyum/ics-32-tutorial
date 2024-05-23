import tkinter as tk

class StudentView:
    def __init__(self, controller) -> None:
        self.controller = controller
        self.master = tk.Tk()
        self.master.title("Student Registration")

        # Label and entry for student name
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        # Label and entry for student course
        self.course_label = tk.Label(self.master, text="Course:")
        self.course_label.grid(row=1, column=0, sticky=tk.W)
        self.course_entry = tk.Entry(self.master)
        self.course_entry.grid(row=1, column=1)

        # Button for registering a student
        self.register_button = tk.Button(
            self.master, text="Register", command=self.controller.register_student
        )
        self.register_button.grid(row=2, column=0, columnspan=2)

        # Button for removing a student
        self.remove_button = tk.Button(
            self.master, text="Remove Student", command=self.controller.remove_student
        )
        self.remove_button.grid(row=3, column=0, columnspan=2)

        # Text box for displaying registered students
        self.registered_textbox = tk.Text(self.master, height=10, width=40)
        self.registered_textbox.grid(row=4, column=0, columnspan=2)

        # List to store registered students
        self.registered_students = []


        self.master.mainloop()