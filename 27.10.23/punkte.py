'''
Aufgabe:
Schreiben Sie eine Funktion, die einen Punktestand daraufhin prüft, ob dieser einen neuen Highscore darstellt.
Das trifft dann zu, wenn die aktuelle Punktzahl größer als der momentane Highscore ist.
In dem Fall soll eine Meldung auf der Konsole ausgegeben werden.
'''

points = float(input("Geben Sie ihre Punkte ein: ")) # Punkte eingeben 
highscore = 100 # Highscore

def check_highscore(points, highscore):
    # Überprüfen, ob die Punktzahl größer als der aktuelle Highscore ist
    if points > highscore:
        # Wenn ja, geben wir eine Glückwunschmeldung aus
        print("Herzlichen Glückwunsch, dies ist ein neuer Highscore!")

check_highscore(points, highscore)