plik = open('numbersinrows.txt')
lista = []

suma = 0
liczba = 0

for line in plik:
    x = line.split(",")
    liczba += len(x)
    for i in x:
        suma += int(i)

print(liczba)
print(suma)
    
plik.close()