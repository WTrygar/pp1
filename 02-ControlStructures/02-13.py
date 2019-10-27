x = int(input('podaj liczbę całkowitą: '))
y = int(input('podaj liczbę całkowitą: '))

if x > 0 and y > 0:
    print(" Punkt znajduje się w pierwszej ćwiartce układu współrzędnych")

elif x < 0 and y > 0:
    print(" Punkt znajduje się w drugiej ćwiartce układu współrzędnych")

elif x < 0 and y < 0:
    print(" Punkt znajduje się w trzeciej ćwiartce układu współrzędnych")

elif x > 0 and y < 0:
    print(" Punkt znajduje się w czwartej ćwiartce układu współrzędnych")

elif x == 0 and y != 0:
    print(" Punkt znajduje się na osi Y")

elif x != 0 and y == 0:
    print(" Punkt znajduje się na osi X")

else:
    print(" Punkt znajduje się na początku układu współrzędnych")