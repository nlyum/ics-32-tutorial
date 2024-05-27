# lab8v2.py

# Starter code for lab 8 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID


from abc import ABC, abstractmethod
import random


class Appetite:
    LOW = 3
    MEDIUM = 4
    HIGH = 5


class GermanShepherd:
    def __init__(self, name, age, appetite: Appetite = Appetite.MEDIUM):
        self._name = name
        self._age = age
        self.hunger_clock = 0
        self.appetite = appetite

    def breed(self):
        return "German Shepherd"

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


if __name__ == "__main__":
    dog = GermanShepherd("Dylan", 3, Appetite.HIGH)
    breed = dog.breed()
    name = dog.name()


    q_flag = False
    while q_flag == False:
        h_text = ""
        if not dog.hungry():
            h_text = "not "
        print(f"Your {breed}, {name} is {h_text}hungry.")
        feed = input(f"Would you like to feed {name}? (y/n/q): ")

        if feed == "y":
            dog.feed()
        elif feed == "q":
            q_flag = False
