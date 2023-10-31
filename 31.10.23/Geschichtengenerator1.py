import random

# Liste von Wörtern und Phrasen
subjekte = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
verben = ["tanzt", "fliegt", "lacht über"]
objekte = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
orte = ["auf dem Mond", "im Dschungel", "in der Wüste"]

# Begrüßung
print("Willkommen zum Zufallsgeschichten-Generator!")

while True:
    # Anzahl der Sätze in der Geschichte vom Benutzer eingeben lassen
    anzahl_sätze = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))
    
    # Generiere zufällige Geschichten
    print("Hier ist deine zufällige Geschichte:")
    for _ in range(anzahl_sätze):
        subjekt = random.choice(subjekte)
        verb = random.choice(verben)
        objekt = random.choice(objekte)
        ort = random.choice(orte)
        satz = f"{subjekt} {verb} {objekt} {ort}."
        print(satz)
    
    # Frage ob weitere Geschichten generiert werden sollen
    weiter = input("Möchtest du weitere Geschichten generieren lassen? (ja/nein): ")
    if weiter.lower() != "ja":
        break

# Grußformel am Ende
print("Vielen Dank für die Verwendung des Zufallsgeschichten-Generators! Auf Wiedersehen!")