#EXERCISE1

print("Hello world \n"*4)

#EXERCISE2

print((99**3)*8)

#EXERCISE3

print(5 < 3)
#False because 5 is'nt less than 3

print(3 == 3)
#True because 3 is equal to 3

print(3 == "3")
#False because 3 is not equal to "3"("" is string and 3 is an integer)

"3" > 3
#It's an error because we can't compare a string with an integer

print("Hello" == "hello")
#False because "Hello" is not equal to "hello" (H is different from h)

#EXERCISE4

computer_brand=str(input("What is your computer brand? "))
print("I have a " + computer_brand + " computer")

#EXERCISE5

name ="Debohi"
age = 21
shoe_size = 40
info="My name is " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
print(info)

#EXERCISE6
a=3
b=6
if a > b:
    print("Hello World");

#EXERCISE7

Number=int(input("Can you give me a number? "))
if Number % 2 == 0:
    print("Your number is even");
else:
    print("Your number is odd");

#EXERCISE8

user_input=str(input("Please enter your name: "))
my_name="Debohi"
if user_input == my_name:
    print("hello my twin");
else:
    print("Hello " + user_input);

#EXERCISE9

number=int(input("Please give me your height in cm: "))
if number < 145:
    print("You are tall enough to ride.");
else :
    print("You need to grow some more to ride.");