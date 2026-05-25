#Exercise1

from random import choice
import random



  


#Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} goes woof!"
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight!"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"
    
# Step 2: Create dog instances
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

#Exercise 3

class PetDog(Dog):
    def __init__(self, name, age, weight): 
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs = ", ".join(args)
        print(f"{self.name} is playing with {dogs}")

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

#EXERCISE4

class Person():
    def __init__(self,first_name, age):
        self.first_name = first_name
        self.last_name = ""
        self.age = age
    def is_18(self):
        return self.age >= 18

class Family():
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []
    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)
    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                    if member.is_18():
                        print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                    else:
                        print("Sorry, you are not allowed to go out with your friends.")
                        
    def family_presentation(self):
        print(f"Family {self.last_name} includes:")
        for member in self.members:
            print(f"{member.first_name}, age {member.age}")

my_family = Family("Smith")
my_family.born("Alice", 20)
my_family.born("Bob", 15)
my_family.family_presentation()
my_family.check_majority("Alice")
my_family.check_majority("Bob")


    