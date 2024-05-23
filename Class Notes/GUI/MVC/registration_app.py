# learn about MV
# MVC stands for model-view-controller
# three elements in your program, very famous design pattern

# Model means data - in this case, the student

# View - the GUI 

# Controller - Everything in between

# What is the benefit of the MVC system? Answer: separations of concerns


from student_model import StudentModel
from student_controller import StudentController
from student_view import StudentView

if __name__ == "__main__":
    model = StudentModel()
    controller = StudentController(model)
    view = StudentView(controller)


