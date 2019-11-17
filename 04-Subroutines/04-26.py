def podatek(dochód):
    if dochód < 5000:
        print(dochód * 0.17)
    elif dochód > 5000:
        print((5000 * 0.17) + ((dochód - 5000) * 0.32))

podatek(int(input("podaj swój dochód")))