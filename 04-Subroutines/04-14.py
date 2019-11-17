x = int(input("Podaj liczbę: "))
tab = [15, 38, 7, 23, 14]
def f(x, tab):
    if x in tab:
        print("Podana liczba występuje w tablicy")
    else:
        print("Podana liczba nie występuje w tablicy")

f(x, tab)
