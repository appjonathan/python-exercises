'''
Aufagbe:
Schreiben Sie eine Funktion print_number_triangle(row), die eine mehrzeilige Ausgabe bis zur übergebenen maximalen Zeilenanzahl wie folgt erzeugt:
'''

def print_number_triangle(row):
    for i in range(1, row+1):
        # Leerzeichen vor den Zahlen drucken, um die Pyramidenform zu erzeugen
        for j in range(row-i):
            print(" ", end=" ")
        
        # Zahlen in aufsteigender Reihenfolge drucken
        for k in range(1, i+1):
            if k % 2 == 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        
        # Zahlen in absteigender Reihenfolge drucken
        for l in range(i-1, 0, -1):
            if l % 2 == 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        
        print()

print_number_triangle(4)
