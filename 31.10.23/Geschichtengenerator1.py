import random

# Funktion generiere_zufaellige_geschichte
def generiere_zufaellige_geschichte():
    # Liste von möglichen Subjekten
    subjekte = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
    # Liste von möglichen Verben
    verben = ["tanzt", "fliegt", "lacht über"]
    # Liste von möglichen Objekten
    objekte = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
    # Liste von möglichen Orten
    orte = ["auf dem Mond", "im Dschungel", "in der Wüste"]
    
    # Eingabe der Anzahl der Sätze in der Geschichte durch den Benutzer
    anzahl_saetze = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))
    
    print("Generierte Geschichte:")
    # Schleife, um die angegebene Anzahl von Sätzen zu generieren
    for _ in range(anzahl_saetze):
        # Erzeugen eines zufälligen Satzes durch Auswahl eines zufälligen Subjekts, Verbs, Objekts und Orts
        satz = f"{random.choice(subjekte)} {random.choice(verben)} {random.choice(objekte)} {random.choice(orte)}"
        print(satz)
    
    # Abfrage, ob der Benutzer weitere Geschichten generieren möchte
    weiter_generieren = input("Weitere Geschichte generieren? (ja/nein): ")
    if weiter_generieren.lower() == "ja":
        # Wenn ja, rufe die Funktion generiere_zufaellige_geschichte erneut auf
        generiere_zufaellige_geschichte()
    else:
        # Ansonsten, beende das Programm
        print("Vielen Dank für die Verwendung des Zufallsgeschichten-Generators!")
    
# Hauptprogramm
print("Willkommen zum Zufallsgeschichten-Generator!")
generiere_zufaellige_geschichte()
print("Auf Wiedersehen!")