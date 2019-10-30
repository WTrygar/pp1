from random import randrange

jeden = dwa = trzy = cztery = pięć = sześć = 0

for x in range(100):
    rzut = randrange(1,7)
    if(rzut == 1):
        jeden += 1
    elif(rzut == 2):
        dwa += 1
    elif(rzut == 3):
        trzy += 1
    elif(rzut == 4):
        cztery += 1
    elif(rzut == 5):
        pięć += 1
    elif(rzut == 6):
        sześć += 1
print(f"Szóstka: {sześć}\nPiątka: {pięć}\nCzwórka: {cztery}\nTrójka: {trzy}\nDwójka: {dwa}\nJedynka: {jeden}")