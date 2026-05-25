#Challenge1

def sort_list(lst):
    return sorted(lst)

sorted_list = sort_list(["without", "hello", "bag", "world"])
print(sorted_list) 

#challenge2

def longest_word(lst):
    words = lst.split(" ")
    print(max(words, key=len))

longest_word("Margaret's toy is a pretty doll.") 

longest_word("A thing of beauty is a joy forever.") 

longest_word("Forgetfulness is by all means powerless!")
