import random


def g():
    return random.randint(1,51)
    
losowa_liczba = lambda: random.randint(1,51)

x = 0
for i in range(1001):
    a = losowa_liczba()
    if a % 2 != 0:
        x += 1
    
print("Procent liczb nieparzystych: ", x / 10,"%")
print("Procent liczb parzystych: ", 100 - (x / 10),"%")
# 1. fragment sprawdzający czy wygenerowane liczby są parzyste
