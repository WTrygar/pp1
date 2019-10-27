indexX = 0
indexY = 0

while True:
    if indexY <= 2:
        i = range(6, -1, -3)[indexY]
        while True:
            if indexX <= 2:
                j = range(1,4)[indexX]
                print(f' { i + j }', end='')
                indexX += 1
            else:
                indexX = 0
                break
        print()
        indexY += 1
    else:
        break