mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

beste_noten = []
schlechteste_noten = []

# Beste und schlechteste Note in Mathematik
beste_mathematik = max(mathematik)
schlechteste_mathematik = min(mathematik)
beste_noten.append(beste_mathematik)
schlechteste_noten.append(schlechteste_mathematik)

# Beste und schlechteste Note in Physik
beste_physik = max(physik)
schlechteste_physik = min(physik)
beste_noten.append(beste_physik)
schlechteste_noten.append(schlechteste_physik)

# Beste und schlechteste Note in Chemie
beste_chemie = max(chemie)
schlechteste_chemie = min(chemie)
beste_noten.append(beste_chemie)
schlechteste_noten.append(schlechteste_chemie)

# Ausgabe der besten und schlechtesten Noten
print("Beste Noten:", beste_noten)
print("Schlechteste Noten:", schlechteste_noten)