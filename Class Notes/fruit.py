class Fruit:
    # one problem we might have is that people might put wrong things in our attributes.
    # we can fix this with a constructor!

    # __init__ is a special method. It seemingly doesn't return anything.
    # That was a lie. It actually returns self, aka a reference to the object!
    # __init__ is the constructor for our class! yippee
    def __init__(self, fruit_type, fruit_color, is_seedless) -> None:
        self.fruit_type = fruit_type
        self.fruit_color = fruit_color
        self.is_seedless = is_seedless
        # now we can define our attributes in the constructor!

    def get_condition(self) -> str:
        condition = "unknown"
        if self.age <= 4:
            condition = "unripe"
        elif self.age > 4 and self.age < 10:
            condition = "ripe"
        elif self.age >= 10:
            condition = "rotten"
        return condition

    def __str__(self) -> str: # this is a method we'll be using to display all of the Fruit's information
        str_rep = "Fruit is " + \
                  self.fruit_type + " " + \
                  self.fruit_color
        return str_rep
    # self is a pointer (or object reference) that points to the object invoking the method
    # this __str__ method is stored in the heap

    

if __name__ == "__main__":
    apple = Fruit("apple", "red", False) # constructing a fruit object
    banana = Fruit("banana", "yellow", False) # constructing a fruit object

    # all of these attributes are located in the heap, the stack just has references to the object
    # the object's location in the heap so we can find it

    print(apple) # Python checks if we have an __str__ method, and since we do, it invokes it
    # now returning the object reference returns the contents of the object instead of the address

    print(apple.get_condition())
    print(Fruit.get_condition(apple))
    