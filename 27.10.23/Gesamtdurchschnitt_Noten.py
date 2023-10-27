mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# Summe aller Noten berechnen
summe = sum(mathematik) + sum(physik) + sum(chemie)

# Anzahl der Noten berechnen
anzahl_noten = len(mathematik)  + len(physik) + len(chemie)

# Gesamtdurchschnitt berechnen
gesamtdurchschnitt = summe / anzahl_noten

# Ausgabe des Gesamtdurchschnitts
print(f"Gesamtdurchschnitt: {gesamtdurchschnitt}")