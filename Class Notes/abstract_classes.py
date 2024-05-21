
#Class Animal is useful as it gives us a hierarchy! It allows us to define the behavior for all its child 
#classes, as well as have some shared data.

#However, it does not make sense to instantiate class Animal, because it represents an abstract concept! 

#Therefore, class Animal needs to be an abstract class!

#Q1) What is an abstract class? 

#Answer: A class that has at least one or more abstract methods 

#Q2) What is an abstract method?

#Answer: A mthod that has a docration, but NO implementation! 

#Important notes about inheriting from an abstract class.
#If a class inherits from an abstract class, it must implement ALL its abstract methods, OR
#it will be considered abstract itself!! 

from abc import ABC, abstractmethod

#Animal is an abstract class, because it has at least one method which is an abstract method 
class Animal(ABC):

    def __init__(self, name) -> None:
        self.name = name

    #abstract method example: 
    @abstractmethod
    def make_sound(self):
        pass


class Dog (Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print(self.name + " Barking!")


class Cat (Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print(self.name + " Meowing!")

class Snake(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print(self.name + " hsssssssss!")

class Toy_Duck(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print ("No sound")

class Goldfish(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        pass

if __name__ == "__main__":

    #a = Animal("Some animal")
    #The line above does not work, because Animal is an abstract class and as such, it can NOT be instantiated! 

    #Important question! Why do we need method make_sound in the parent class (i.e. Animal) if it's going to be abstract anyways??
    #Answer: Because by having an abstract method make_sound in the parent class, we define the requirment for all child classes of 
    #Animal, to have and implement a make_sound method! 
    d = Dog("Spot")
    d.make_sound()
    c = Cat("Fluffy")
    c.make_sound()

    s = Snake("Hissss")


#Liscov's substitution principle: It's a principle developed by Barbra Liskov that is used to evaluate inheritance!!
#It states: A base class should be able to be substituted for any of its derived classes! 