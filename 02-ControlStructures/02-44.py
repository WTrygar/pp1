a = float(input('Podaj limit prędkości (km/h):' ))
b = float(input('Podaj prędkość pojazdu (km/h): ' ))
c = b - a
if c < 10 and c > 0:
    print("mandat: ", c * 5)
elif c > 10:
    print("mandat: ", c * 15)
