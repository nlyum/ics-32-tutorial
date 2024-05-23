# this will sit between the model and the view

# from student_model import StudentModel

class StudentController:

    def __init__(self, model) -> None:
        self.model = model

    def register_student(self):
        self.model.register_student()
    
    def remove_student(self):
        self.model.remove_student()


