
#Exercise 1: What is the Season?

month=int(input("Please enter a month number(1 to 12): "))

if month>=3 and month<=5:
    print("Spring")
elif month>=6 and month<=8:
    print("Summer")
elif month>=9 and month<=11:
    print("Autumn")
else:
    print("Winter")

#Exercise 2: For Loop

for i in range(1,21):
    print(i);
 
for i in range(1,21):
    if i%2==0:
        print(i);

#Exercice 3 : Boucle While

user_name=""
while user_name =="":
    user_name=str(input("Can you give your name please? "));

#Exercice 4 : Vérifiez l'index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name=str(input("What is your name? "))

if name in names :
    index=names.index(name)
    print(f"{index}")

#Exercise 5: Greatest Number

number1=int(input("Can we enter the first number? "))
number2=int(input("Can we enter the second number? "))
number3=int(input("Can we enter the third number? "))

maxi= max(number1,number2,number3)

print(f"The greatest number is: {maxi}" );

#Exercise 6 : Random number

import random

decision='yes'
score=0
while decision=='yes':
    number=int(input("Can you enter one number between 1 an 9 ?"))
    if number==random.randint(1,9):
        print("Winner")
        score+=1
    else:
        print("Better luck next time.");
    decision=str(input("If you want to continue the game , we can put yes else no "))

print(score)
