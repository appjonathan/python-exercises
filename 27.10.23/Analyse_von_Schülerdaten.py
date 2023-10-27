mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

notenverteilung_mathematik = {}
notenverteilung_physik = {}
notenverteilung_chemie = {}

# Notenverteilung in Mathematik erstellen
for note in mathematik:
    if note in notenverteilung_mathematik:
        notenverteilung_mathematik[note] += 1
    else:
        notenverteilung_mathematik[note] = 1

# Notenverteilung in Physik erstellen
for note in physik:
    if note in notenverteilung_physik:
        notenverteilung_physik[note] += 1
    else:
        notenverteilung_physik[note] = 1

# Notenverteilung in Chemie erstellen
for note in chemie:
    if note in notenverteilung_chemie:
        notenverteilung_chemie[note] += 1
    else:
        notenverteilung_chemie[note] = 1

# Ausgabe der Notenverteilung
print("Notenverteilung in Mathematik:", notenverteilung_mathematik)
print("Notenverteilung in Physik:", notenverteilung_physik)
print("Notenverteilung in Chemie:", notenverteilung_chemie)