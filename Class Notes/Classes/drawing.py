
# This doesn't follow the open-closed principle! It's not open to extension. How do we fix this...

# This design doesn't follow the open-closed principle because we must modify class DrawingTool to add more shapes!

class Shape:
    def __init__(self, shape_type) -> None:
        self.shape_type = shape_type

class DrawingTool:
    def __init__(self) -> None:
        pass

    def draw(self, shape):
        if shape.shape_type == "Circle":
            self.draw_circle()
        elif shape.shape_type == "Square":
            self.draw_square()
        else:
            raise ValueError("Unknown shape type")
    
    def draw_circle(self):
        print("Drawing a Circle!")
    
    def draw_square(self):
        print("Drawing a Square!")

if __name__ == "__main__":
    shape1 = Shape('Circle')
    shape2 = Shape('Triangle')
    
    tool = DrawingTool()
    tool.draw(shape1)
    tool.draw(shape2)
    

