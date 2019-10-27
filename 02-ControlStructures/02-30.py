PIN = "0805"

x = str(input("Podaj kod pin: "))
if x == "0805":
    print("PIN prawidłowy")
else:
    print("PIN niepoprawny")
    x = str(input("Podaj kod pin: "))
    if x == "0805":
        print("PIN prawidłowy")
    else:
        print("PIN niepoprawny")
        x = str(input("Podaj kod pin: "))
        if x == "0805":
            print("PIN prawidłowy")
        else:
            print("PIN niepoprawny, karta płatnicza zablokowana")