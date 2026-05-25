#CHALLENGE 1

word = input("Enter a word: ")
word = word.lower()
dictionary_word={}
for index, letter in enumerate(word):
    if letter in dictionary_word:
        dictionary_word[letter].append(index)
    else:
        dictionary_word[letter]=[index]
print(dictionary_word)

#CHALLENGE 2

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

wallet_amount = float(wallet.replace("$", "").replace(",", ""))
basket = []

for item, price_str in items_purchase.items():
    price = float(price_str.replace("$", "").replace(",", ""))
    if price <= wallet_amount:
        basket.append(item)
        wallet_amount -= price

print(sorted(basket) if basket else "Nothing can be bought.")