import random

a = random.randint(1,6)

b = int(input("Odgadnij liczbę od 1 do 6: "))
if a == b:
    print(True)
else:
    print(False)