#EXERCISE1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Shadow", 3)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")

#EXERCISE2

class Dog:
    def __init__(self,name ,height):
        self.name = name
        self.height = height
    def bark(self):
        print("self.name goes woof!")
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")
        
davids_dog = Dog("Rex", 50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()   

def compare(dog1, dog2):
    if dog1.height > dog2.height:
       return f"{dog1.name}"
    elif dog1.height < dog2.height:
       return f"{dog2.name}"
    else:
        return "Both dogs are the same height!"
print(compare(davids_dog, sarahs_dog))

#EXERCISE3

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 
            
stairway = Song(["There’s a lady who's sure"," all that glitters is gold","And she’s buying a stairway to heaven"])

#Exercise 4

class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        print(f"{new_animal} added to the zoo.")
    def get_animals(self):
        return self.animals
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        print(f"{animal_sold} sold.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        for key in sorted_animals:
            sorted_animals[key].sort()
        print(sorted_animals)
    def get_groups(self):
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        print(groups)
    
    #Bonus
    def add_animals(self,*args):
        for animal in args:
            if animal not in self.animals:
                self.animals.append(animal)
        print(f"{animal} added to the zoo.")
    
# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()



