login = "Marek"
hasło = "m-123"

login = input("Wprowadź login: ")
hasło = input("Wprowadź hasło: ")

if (login == "Marek" and hasło == "m-123"):
    print("Dane poprawne, witaj")
else:
    print("Błędne hasło lub login, proszę spróbować ponownie")