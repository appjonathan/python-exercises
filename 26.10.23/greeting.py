name = input("Wie heißt du? ").capitalize()
print(f"Hallo {name}, schön dich kennenzulernen!")

länge = len(name)
print(f"Name besteht aus {str(länge)} Zeichen!")

alter = input("Wie alt bist du? ")
print(f"{name}, du wirst nächstes Jahr {str(int(alter) + 1)}")