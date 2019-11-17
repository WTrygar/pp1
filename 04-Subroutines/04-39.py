def f(x,y,n):
    if n > x and n < y:
        print("Liczba mieści się w podanym zbiorze")
    else:
        print("Podana liczba nie mieści się w zbiorze")

f(x = float(input("Podaj dolną granicę zbioru")) , y = float(input("Podaj dolną granicę zbioru")), n = float(input("Podaj liczbę")))
