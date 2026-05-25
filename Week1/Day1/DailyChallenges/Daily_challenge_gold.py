day=int(input("Enter the Day: "))

month=int(input("Enter the month: "))

year=int(input("Enter the year: "))

print(f"your birthdate is {day}/{month}/{year}")

age=2026-year

num_candles = str(age)[-1]

if num_candles == "0":
    candles = "     "
elif num_candles == "1":
    candles = "  i  "
elif num_candles == "2":
    candles = " i i "
elif num_candles == "3":
    candles = " i i i"
elif num_candles == "4":
    candles = "iiii "
else:
    candles = "iiiii"

print(f"       ___{candles}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")