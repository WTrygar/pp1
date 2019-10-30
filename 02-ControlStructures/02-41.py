liczby = []

while True:
    temporary = input('Podaj liczbę: ')
    if temporary == '0':
        break
    liczby.append(float(temporary))

suma = sum(liczby)

srednia = suma / len(liczby)
print('REZULTAT: Liczb=', len(liczby), ', Suma=', suma, ', Średnia=', srednia )