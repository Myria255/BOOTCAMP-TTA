#EXERCICE1

car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

manufacturers = car_string.split(", ")

print("There are " + str(len(manufacturers)) + " manufacturers in the list.")

reversed_manufacturers = sorted(manufacturers, reverse=True)
print(reversed_manufacturers)

count_o = len([name for name in manufacturers if "o" in name.lower()])
print(count_o)

count_no_i = len([name for name in manufacturers if "i" not in name.lower()])
print(count_no_i)

duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_list = list(set(duplicates_list))

print(", ".join(unique_list), end="")
print()
print("There are now " + str(len(unique_list)) + " companies in the list.")

bonus_list = sorted(manufacturers)
reversed_letters = [name[::-1] for name in bonus_list]
print(reversed_letters)

# Exercise 2

def get_full_name(first_name, last_name, middle_name=""):
    if middle_name == "":
        full_name = first_name + " " + last_name
    else:
        full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

# Exercise 3

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..'
}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def english_to_morse(text):
    words = text.upper().split(" ")
    morse_words = []
    for word in words:
        morse_letters = []
        for letter in word:
            if letter in MORSE_CODE_DICT:
                morse_letters.append(MORSE_CODE_DICT[letter])
        morse_words.append(" ".join(morse_letters))
    return " / ".join(morse_words)

def morse_to_english(morse):
    morse_words = morse.split(" / ")
    english_words = []
    for word in morse_words:
        letters = word.split(" ")
        english_letters = []
        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                english_letters.append(REVERSE_MORSE_DICT[letter])
        english_words.append("".join(english_letters))
    return " ".join(english_words)


coded = english_to_morse("HELLO WORLD")
print(coded)

decoded = morse_to_english(coded)
print(decoded)