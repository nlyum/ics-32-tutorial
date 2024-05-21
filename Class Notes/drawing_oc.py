# This design is compliant with the OPC. We can extend class Shape if we want to add more shapes.
# Shapes should be in charge of drawing themselves. Classes should come equipped with all methods one can expect to happen to them.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

class DrawingTool:
    def draw(self, shape):
        shape.draw()

if __name__ == "__main__":
    shape1 = Circle()
    shape2 = Square()
    shape3 = Triangle()
    
    tool = DrawingTool()
    tool.draw(shape1)
    tool.draw(shape2)
    tool.draw(shape3)
    
