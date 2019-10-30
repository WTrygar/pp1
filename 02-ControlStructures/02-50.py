import math 

liczba = int(input('Podaj liczbę: '))
dwojkowy = []

while True:
    tempLiczba = math.floor(liczba / 2)
    tempReszta = liczba % 2

    dwojkowy.append(str(tempReszta))

    liczba = tempLiczba

    if liczba == 0:
        break

print(''.join(dwojkowy[::-1]))