#CHALLENGES 1

number=int(input("Can you give one number ?"))
length=int(input("Can you give the length ?"))

list=[]

for i in range(1,length+1):
    list.append(number*i);
print(list)

#CHALLENGE 2

user_word=str(input("Enter the word. "))

if user_word:
    clean_string=user_word[0]
    for char in user_word[1:]:
        if char != clean_string[-1]:
            clean_string += char
else:
    clean_string=""     

print(clean_string)   
