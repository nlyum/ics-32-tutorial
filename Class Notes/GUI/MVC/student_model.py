# the model contains the data. the model encapsulates the data!
# such that it performs that it performs all necessary operations
# needed by the data
# so it adds students and remove students, because those are
# operations needed by the data

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
class StudentModel:
    def __init__(self) -> None:
        self.registered_student = []

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
    
    def remove_student(self):
        if self.registered_student: # if the list isn't empty, remove the last one
            self.register_student.pop()
        


