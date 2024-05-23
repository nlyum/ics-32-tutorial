from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print(self.name + " barks!")

class Cat(Animal):
    def sound(self):
        print(self.name + " meows!")


def main():
    animal1 = Dog("Jeff")
    animal1.sound()

    animal2 = Animal("Steve")

if __name__ == "__main__":
    main()