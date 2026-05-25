#EXERCISE 1

class Circle():
    def __init__(self, radius=1.0):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def area(self):
        return 3.14 * self.radius ** 2
    def get_perimeter(self):
        return self.perimeter()

#EXERCISE 2
import random

class MyList():
    def __init__(self, my_list):
        self.my_list = my_list
    def get_reversed_list(self):
        return self.my_list[::-1]
    def get_sorted_list(self):
        return sorted(self.my_list)
    def get_second_list(self):
        list2 = []
        for i in range(1, len(self.my_list)):
           list2.append(random.randint(1, 100)) 
        return list2

Your= MyList([5, 2, 9, 1, 5, 6])

print(Your.get_second_list())

            
        
   