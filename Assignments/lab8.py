# lab8v2.py

# Starter code for lab 8 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME: Nathan Lyum
# EMAIL: nlyum@uci.edu
# STUDENT ID: 63833693


from abc import ABC, abstractmethod
import random


class Appetite:
    LOW = 3
    MEDIUM = 4
    HIGH = 5

class Dog(ABC):
    def __init__(self, name, age, appetite: Appetite = Appetite.MEDIUM):
        self._name = name
        self._age = age
        self.hunger_clock = 0
        self.appetite = appetite
    
    @abstractmethod
    def breed(self):
        return "No breed assigned"

    def name(self):
        return self._name

    def age(self):
        return self._age

    def hungry(self):
        """
        The hungry method will check the hungry clock to see if some time has
        passed since the last feeding. If clock is greater than breed typical
        appetite, hunger assessment is randomly selected,
        otherwise hunger clock increases
        """
        if self.hunger_clock > self.appetite:
            return bool(random.getrandbits(1))
        else:
            self.hunger_clock += 1
            return False

    def feed(self):
        """
        Feeds the dog. Hunger clock is reset
        """
        self.hunger_clock = 0


class GermanShepherd(Dog):
    def __init__(self, name, age, appetite: Appetite = Appetite.MEDIUM):
        super().__init__(name, age, appetite)

    def breed(self):
        return "German Shepherd"


class Pomeranian(Dog):
    def __init__(self, name, age, appetite: Appetite = Appetite.LOW):
        super().__init__(name, age, appetite)

    def breed(self):
        return "Pomeranian"


class GreatDane(Dog):
    def __init__(self, name, age, appetite: Appetite = Appetite.HIGH):
        super().__init__(name, age, appetite)

    def breed(self):
        return "Great Dane"


if __name__ == "__main__":
    dog = None
    breed_num = 0

    while not (0 < breed_num < 4):
        print("What breed of dog would you like? (Enter a number)")
        print("1: German Shepherd")
        print("2: Pomeranian")
        print("3: Great Dane")
        try:
            breed_num = int(input())
        except:
            print("Please enter an integer from 1 to 3.")
    
    print("What is your dog's name?")
    dog_name = input()

    dog_age = -1
    while dog_age < 0:
        print("What is your dog's age?")
        try:
            dog_age = int(input())
        except:
            print("Please enter a nonnegative integer.")

    app_num = 0

    # I was originally going to have the uesr select the appetite level,
    # but I decided to have the dog breed determine the appetite instead

    # while not (0 < app_num < 4):
    #     print("What is your dog's appetite level? (Enter a number)")
    #     print("1: Low")
    #     print("2: Medium")
    #     print("3: High")
    #     try:
    #         app_num = int(input())
    #     except:
    #         print("Please enter an integer from 1 to 3.")
    # 
    # if app_num == 1:
    #     dog_appetite = Appetite.LOW
    # elif breed_num == 2:
    #     dog_appetite = Appetite.MEDIUM
    # elif breed_num == 3:
    #     dog_appetite = Appetite.HIGH
    
    if breed_num == 1:
        dog = GermanShepherd(dog_name, dog_age)
    elif breed_num == 2:
        dog = Pomeranian(dog_name, dog_age)
    elif breed_num == 3:
        dog = GreatDane(dog_name, dog_age)

    breed = dog.breed()
    name = dog.name()

    q_flag = False
    while not q_flag:
        h_text = ""
        if not dog.hungry():
            h_text = "not "
        print(f"Your {breed}, {name} is {h_text}hungry.")
        feed = input(f"Would you like to feed {name}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            q_flag = True
