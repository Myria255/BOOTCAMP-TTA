# Exercise 1

birthdays = {
    "Albert Einstein": "1879/03/14",
    "Marie Curie": "1867/11/07",
    "Ada Lovelace": "1815/12/10",
    "Alan Turing": "1912/06/23",
    "Isaac Newton": "1643/01/04"
}
print(birthdays)
answer = input("You can look up the birthdays of the people in the list! Give me a person's name: ")

birthday = birthdays[answer]

print("The birthday of " + answer + " is " + birthday)

# Exercise 2

birthdays = {
    "Albert Einstein": "1879/03/14",
    "Marie Curie": "1867/11/07",
    "Ada Lovelace": "1815/12/10",
    "Alan Turing": "1912/06/23",
    "Isaac Newton": "1643/01/04"
}

for name in birthdays:
    print(name)

answer = input("You can look up the birthdays of the people in the list! Give me a person's name: ")
if answer in birthdays:
    birthday = birthdays[answer]
    print("The birthday of " + answer + " is " + birthday)
else:
    print("Sorry, we don’t have the birthday information for " + answer)
    
# Exercise 3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_input = input("What is your name? ")

if user_input in names:
    print(names.index(user_input))

# Exercise 4

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        throws += 1
        if die1 == die2:
            break
    return throws

def main():
    collection = []
    
    for _ in range(100):
        collection.append(throw_until_doubles())
        
    total = sum(collection)
    average = total / 100
    
    print("Total throws: " + str(total))
    print("Average throws to reach doubles: " + str(round(average, 2)))

main()