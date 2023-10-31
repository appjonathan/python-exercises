import random

# Liste von Wörtern und Phrasen
einführungen = ["In einer fernen Galaxie", "Es war einmal", "Vor langer Zeit"]
subjekte = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
verben = ["tanzt", "fliegt", "lacht über"]
objekte = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
orte = ["auf dem Mond", "im Dschungel", "in der Wüste"]
handlungen = ["entdeckte", "rettete", "erforschte"]
höhepunkte = ["einen außerirdischen Freund", "einen geheimen Schatz", "eine verborgene Welt"]
enden = ["und lebte glücklich bis ans Ende seiner Tage.", "und wurde zum Helden der Galaxie.", "und fand seinen wahren Zweck im Leben."]

# Begrüßung
print("Willkommen zum verbesserten Zufallsgeschichten-Generator!")

while True:
    # Einführung
    einführung = random.choice(einführungen)
    print(einführung)
    
    # Hauptfigur
    subjekt = random.choice(subjekte)
    
    # Handlung
    handlung = random.choice(handlungen)
    
    # Höhepunkt
    höhepunkt = random.choice(höhepunkte)
    
    # Ort
    ort = random.choice(orte)
    
    # Ende
    ende = random.choice(enden)
    
    # Generiere Geschichte
    print(f"{subjekt} {handlung} {objekte[0]} {ort}.")
    print(f"Dann {verben[0]} {subjekt} {höhepunkt} {ort}.")
    print(ende)
    
    # Frage ob weitere Geschichten generiert werden sollen
    weiter = input("Möchtest du weitere Geschichten generieren lassen? (ja/nein): ")
    if weiter.lower() != "ja":
        break
# Verabschiedung
print("Vielen Dank für die Verwendung des verbesserten Zufallsgeschichten-Generators! Auf Wiedersehen!")