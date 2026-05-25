#Old MacDonald’s Farm

class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    def add_animal(self, animal_type, count=1):
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
    def get_info(self):
        print(f"{self.name} Farm")
        print("Animal\t\tCount")
        print("------\t\t-----")
        for animal, count in self.animals.items():
            print(f"{animal}\t\t{count}")
        print("\nE-I-E-I-0!")
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        return f"McDonald’s farm has {', '.join(self.get_animal_types())}."
    def add_animals(self, **kwargs):
        for animal_type, count in kwargs.items():
            self.add_animal(animal_type, count)

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())

