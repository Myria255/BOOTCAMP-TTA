#EXERCISE1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

#EXERCISE2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost = 0
for age in family.values():
    if age < 3:
        print(f"Free")
        cost += 0
    elif age >= 3 and age <= 12:
        print("10 $")
        cost += 10
    else:
        print("15 $")
        cost += 15

print(f"Total cost: ${cost}")

#EXERCISE3

brand={}
brand["name"]="Zara"
brand["creation_date"]=1975
brand["creator"]="Amancio Ortega Gaona"
brand["type_of_clothes"]=["men", "women", "children"]
brand["international_competitors"]=["Gap", "H&M", "Benetton"]
brand["number_stores"]=7000
brand["major_color"]={"France": "blue", "Spain": "red", "US": ["pink", "green"]}
#update number of stores
brand["number_stores"]=2
print(brand)
print(f"Zara's clients are: {brand['type_of_clothes']}")
print(f"Zara's international competitors are: {brand['international_competitors']}")
brand["country_creation"]="Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)
del brand["creation_date"]
print(brand)

brand.popitem()
print(brand)

print(f"Last international competitor: {brand['international_competitors'][-1]}")

print(f"the major colors in the US are: {brand['major_color']['US']}")
print(f"the number of keys in the dictionary is: {len(brand)}")
print(f"the dictionary keys are: {brand.keys()}")

#BONUS

more_on_zara={"creation_date":1975, "number_stores":10000}
brand.update(more_on_zara)
print(brand)

#EXERCISE4

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")
    
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

import random

def number(n):
    if n in range(1, 101):
        random_number = random.randint(1, 100)
        if n==random_number:
            print("Success!")
        else:
            print(f"Fail! Your number: {n}, Random number: {random_number}")
    else:
        print("Number is out of range.")

number(int(input("Enter a number between 1 and 100: ")))

#EXERCISE6

def make_shirt(size, text):
     print(f"The shirt size is {size} and the text is '{text}'.")
     
make_shirt("M", "Louis Vuitton")

def make_shirt(size="Large", text="I love Python"):
    print(f"The shirt size is {size} and the text is '{text}'.")

make_shirt("Large")
make_shirt("medium")
make_shirt(text="I love Python")
make_shirt(size="small", text="Hello!")

#EXERCISE7

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The current temperature is {temp}°C.")
    if temp < 0:
        print("Brrr, it's freezing! Wear a coat.")
    elif 0 <= temp < 16:
        print("It's a bit chilly. Wear a jacket.")
    elif 16 <= temp < 23:
        print("The weather is nice. A t-shirt should be fine.")
    elif 23 <= temp < 32:
        print("It's quite warm. Stay hydrated!")
    else:
        print("It's scorching! Stay indoors if possible.")
        
def get_random_temp():
     return int(input("Enter the month (1-12): "))
def main():
    month = get_random_temp()
    if month in [12, 1, 2]:
        print("It's winter. Wear a coat.")
    elif month in [3, 4, 5]:
        print("It's spring. A light jacket should be fine.")
    elif month in [6, 7, 8]:
        print("It's summer. A t-shirt should be fine.")
    elif month in [9, 10, 11]:
        print("It's autumn. A sweater should be fine.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
        

#EXERCISE8

decision=""
garniture=[]
price=10
while decision!="quit":
    topping = input("Enter a pizza topping :")
    print(f"Adding {topping} to your pizza.")
    garniture.append(topping)
    price+=2.5
    decision = input("Do you want to add another topping? (quit) :")

for topping in garniture:
    print(f"- {topping}")
print(f"Total price: {price} $")