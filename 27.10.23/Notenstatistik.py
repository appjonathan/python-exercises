mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

notenstatistik = []

# Anzahl der Noten über 90 in Mathematik zählen
anzahl_mathematik = len([note for note in mathematik if note >= 90])
notenstatistik.append(anzahl_mathematik)

# Anzahl der Noten über 90 in Physik zählen
anzahl_physik = len([note for note in physik if note >= 90])
notenstatistik.append(anzahl_physik)

# Anzahl der Noten über 90 in Chemie zählen
anzahl_chemie = len([note for note in chemie if note >= 90])
notenstatistik.append(anzahl_chemie)

# Ausgabe der Notenstatistik
print("Notenstatistik:", notenstatistik)