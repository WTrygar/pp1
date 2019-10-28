a = int(input("Podaj wartość w zł: "))
x = 0
while x != a:
    if((a-x)%5 == 0):
        x = x + 5
        print("5zł")
    elif((a-x)%5 == 2 or (a-x)%5 == 4):
        x = x+2
        print("2zł")
    else:
        x = x+1
        print("1zł")