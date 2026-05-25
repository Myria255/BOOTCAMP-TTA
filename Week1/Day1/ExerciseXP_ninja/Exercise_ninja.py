#EXERCISE1

3 <= 3 < 9
#true
3 == 3 == 3
#true
bool(0)
#False
bool(5 == "5")
#False
bool(4 == 4) == bool("4" == "4")
#True
bool(bool(None))
#false
x = (1 == True)

y = (1 == False)

a = True + 4

b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#EXERCISE2

max_length = 0

while True:
    user_sentence = input("Enter the longest sentence you can without the character 'A': ")
    
    if "a" in user_sentence.lower():
        print("Your sentence contains the letter 'A'. Try again!")
        continue
        
    current_length = len(user_sentence)
    
    if current_length > max_length:
        max_length = current_length
        print(f"Congratulations! You set a new record with {max_length} characters.")
    else:
        print(f"Valid sentence, but not longer than your current record of {max_length} characters.")


#EXERCISE 3
text_paragraph = "Technology is evolving at an incredible pace, and artificial intelligence is at the forefront of this digital revolution. Learning to code opens up endless possibilities for innovation and problem solving. Every programmer starts with a simple program, but consistency builds great systems. The journey of learning is just as important as the final destination."

characters_count = len(text_paragraph)

sentences_count = text_paragraph.count(".") + text_paragraph.count("!") + text_paragraph.count("?")

words_list = text_paragraph.lower().replace(".", "").replace("!", "").replace("?", "").split()
words_count = len(words_list)

unique_words_count = len(set(words_list))

print("TEXT ANALYSIS REPORT")

print(f"Total characters : {characters_count}")
print(f"Total sentences  : {sentences_count}")
print(f"Total words      : {words_count}")
print(f"Unique words     : {unique_words_count}")
print("-" * 40)