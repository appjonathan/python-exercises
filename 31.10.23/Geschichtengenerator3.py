import random

def generiere_zufaellige_geschichte():
    einleitungen = ["In einer fernen Galaxie", "Es war einmal in einem kleinen Dorf", "Auf einem abgelegenen Berggipfel"]
    subjekte = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
    verben = ["tanzt", "fliegt", "lacht über"]
    objekte = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
    orte = ["auf dem Mond", "im Dschungel", "in der Wüste"]
    handlungen = ["entdeckte", "rettete", "erfand"]
    hohepunkte = ["einen außerirdischen Freund", "einen Schatz", "eine geheime Tür"]
    ende = ["und lebte glücklich bis ans Ende seiner Tage.", "und wurde berühmt.", "und fand sein wahres Glück."]
    
    einleitung = random.choice(einleitungen)
    hauptfigur = random.choice(subjekte)
    handlung = random.choice(handlungen)
    hohepunkt = random.choice(hohepunkte)
    abschluss = random.choice(ende)
    
    anzahl_saetze = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))
    
    geschichten = []
    geschichten.append(f"{einleitung} {hauptfigur} {handlung} {random.choice(objekte)} {random.choice(orte)}")
    
    for _ in range(anzahl_saetze-2):
        satz = f"{hauptfigur} {random.choice(verben)} {random.choice(objekte)} {random.choice(orte)}"
        geschichten.append(satz)
    
    geschichten.append(f"{hauptfigur} {hohepunkt} {random.choice(orte)}")
    geschichten.append(f"{hauptfigur} {random.choice(verben)} {random.choice(objekte)} {abschluss}")
    
    with open("generierte_geschichten.txt", "w", encoding="utf-8") as datei:
        for geschichte in geschichten:
            datei.write(geschichte + "\n")
    
    print("Die Geschichten wurden in die Datei 'generierte_geschichten.txt' gespeichert.")
    
    weiter_generieren = input("Weitere Geschichte generieren? (ja/nein): ")
    if weiter_generieren.lower() == "ja":
        generiere_zufaellige_geschichte()
    else:
        print("Vielen Dank für die Verwendung des Zufallsgeschichten-Generators!")
    
print("Willkommen zum Zufallsgeschichten-Generator!")
generiere_zufaellige_geschichte()
print("Auf Wiedersehen!")
