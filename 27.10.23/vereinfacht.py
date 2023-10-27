'''
Aufgabe:
Vereinfache folgende Funktion >>>
def do_something (x, y) :
if x> 0 and x < 100 and y > 10 and y < 20:
print ("VALID RANGE" )
'''

def do_something(x, y):
    # Prüfen, ob x im Bereich von 0 bis 100 liegt und y im Bereich von 10 bis 20 liegt
    if 0 < x < 100 and 10 < y < 20:
        # Wenn die Bedingung erfüllt ist, geben wir "GÜLTIGER BEREICH" aus
        return "VALID RANGE"
    return "NO VALID RANGE"

# In der vereinfachten Version der Funktion wurden die einzelnen Bedingungen zu einer einzigen Bedingung kombiniert.
# Statt mehrere Vergleichsoperatoren zu verwenden, wurde die Bedingung mit dem Bereichsoperator x < y < z zusammenfassen.

# Eingabe für x
eingabe_x = float(input("Geben Sie den Wert für x ein: "))

# Eingabe für y
eingabe_y = float(input("Geben Sie den Wert für y ein: "))

# Aufruf der Funktion do_something mit den eingegebenen Werten
ergebnis = do_something(eingabe_x, eingabe_y)

# Ausgabe des Ergebnisses
print(ergebnis)