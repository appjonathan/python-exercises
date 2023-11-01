import random

# Definition der Funktion generiere_zufaellige_geschichte
def generiere_zufaellige_geschichte():
    # Liste von möglichen Einleitungen
    einleitungen = ["In einer fernen Galaxie", "In in einem kleinen abgelegenen Dorf", "Auf einem abgelegenen Berggipfel"]
    # Liste von möglichen Subjekten
    subjekte = ["Ein kleiner Junge", "Ein freches Mädchen", "Ein furchtloser Schwertkämpfer"]
    # Liste von möglichen Verben (Teil 1)
    verben1 = ["lebte", "wachte", "ruhte"]
    # Liste von möglichen Verben (Teil 2)
    verben = ["kämpfte", "fliegt", "lacht über"]
    # Liste von möglichen Bindewörtern
    bindewort = ["und", "aber"]
    # Liste von möglichen Objekten
    objekte = ["ein Breitschwert", "einen Drachen", "eine Hellebarde"]
    # Liste von möglichen Orten
    orte = ["auf dem Schlachtfeld", "im Dschungel", "in der Wüste"]
    # Liste von möglichen Handlungen
    handlungen = ["entdeckte", "rettete", "erschlug"]
    # Liste von möglichen Höhepunkten
    hohepunkte = ["einen großen Magier", "einen Schatz", "eine geheime Tür"]
    # Liste von möglichen Enden
    ende = ["und lebte glücklich bis ans Ende seiner Tage.", "und wurde berühmt.", "und fand sein wahres Glück."]    
    
    # Eingabe der Anzahl der Sätze in der Geschichte durch den Benutzer
    anzahl_saetze = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))
        
    # Schleife, um die angegebene Anzahl von Sätzen zu generieren
    for _ in range(anzahl_saetze):
        # Erzeugen eines zufälligen Satzes durch Auswahl einer zufälligen Einleitung, eines zufälligen Subjekts, eines zufälligen Bindeworts, eines zufälligen Verbs, eines zufälligen Objekts, eines zufälligen Orts, einer zufälligen Handlung, eines zufälligen Höhepunkts und eines zufälligen Endes
        satz = f"{random.choice(einleitungen)} {random.choice(verben1)} {random.choice(subjekte)} {random.choice(bindewort)} {random.choice(verben)} {random.choice(objekte)} {random.choice(orte)} {random.choice(handlungen)} {random.choice(hohepunkte)} {random.choice(ende)}"
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