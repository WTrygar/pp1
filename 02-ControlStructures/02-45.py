  
ilość = int(input("Podaj ilość liczb: "))
x = 2
spr = 0
if(ilość == 1):
    print("Liczby pierwsze: 2")
elif(ilość == 2):
    print("Liczby pierwsze: 2 3")

elif(ilość < 3):
    print("Liczby pierwsze: 2 3 5")
else:
    x = 3
    print("Liczby pierwsze: 2", end = " ")
    while ilość - 1 > 0: 
        y = 2
        while (y <= x ** (1/2)):
            if( x % y == 0):
                spr = 1
                y = x
            else:
                y += 1
        if spr == 0:
            print(x,end = " ")
            spr = 0
            x += 2
            ilość -= 1
        else:
            x += 2
            spr = 0