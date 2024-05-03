# class example 1

class Fruit:
    # these are the attributes of the Fruit class
    fruit_type: str
    color: str
    is_seedless: bool
    condition: str

    #
    def __str__(self):
        str_rep = "Fruit: " + self.condition + " " + \
                  self.color + " " + self.fruit_type
        return str_rep


if __name__ == "__main__":
    apple = Fruit() # this is the constructor that created the object
    # the line above is an instantiation of the Fruit class

    apple.fruit_type = "apple"
    apple.color = "green"
    apple.is_seedless = False

    print(apple)
    # this prints the address of the object, which is the content of the object reference.

    # let's check the color of what we've just made.
    print(apple.color)

# if we were to draw a memory diagram, somefruit would be an object reference in the stack that
# points to the object of type fruit in the heap.
# cool, right?
