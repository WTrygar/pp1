tablica = [[1, 2, 0],
        [0, 0, 3],
        [5, 1, 1]]

def myprint(tab):
    print(tab[0][0], tab[0][1], tab[0][2])
    print(tab[1][0], tab[1][1], tab[1][2])
    print(tab[2][0], tab[2][1], tab[2][2])

myprint(tablica)
print()
def transpozycja(tab):
    temp = [[0 for y in range(3)] for x in range(3)]
    for y in range(len(tab)):
        for x in range(len(tab[0])):
            temp[y][x] = tab[x][y]
    return temp
    
myprint(transpozycja(tablica))