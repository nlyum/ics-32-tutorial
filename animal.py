class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def move(self):
        print("Animal's move")

    def sound(self):
        print("Animal's sound")
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def sound(self):
        print(f"{self.name} meows!")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def sound(self):
        print(f"{self.name} barks!")


if __name__ == "__main__":
    animal1 = Animal("Some Animal")
    cat1 = Cat("Fluffy")
    dog1 = Dog("Spot")

    animal1.sound()
    cat1.move()
    dog1.sound()

