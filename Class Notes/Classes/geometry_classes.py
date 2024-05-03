class Rectangle:
    number_of_rectangles = 0
    def __init__(self, rec_len, rec_width) -> None:
        self.rec_len = rec_len
        self.rec_width = rec_width
        Rectangle.number_of_rectangles += 1
    def calculate_area(self):
        return self.rec_width * self.rec_len
    def calculate_prem(self):
        return 2 * self.rec_width + 2 * self.rec_len

def calculate_area(l, w):
    return l * w

if __name__ == "__main__":
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(10, 20)

    print(rect1.calculate_area())
    print(calculate_area(rect1.rec_len, rect1.rec_width)) # NEVER DO THIS ONE, this should be something you implement in your classes
    print(f"Number of rectangles: {rect1.number_of_rectangles}")
    print(f"Number of rectangles: {Rectangle.number_of_rectangles}")