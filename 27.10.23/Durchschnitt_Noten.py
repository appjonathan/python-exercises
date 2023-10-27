mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

durchschnitt_noten = []

# Durchschnittsnote in Mathematik berechnen
durchschnitt_mathematik = sum(mathematik) / len(mathematik)
durchschnitt_noten.append(durchschnitt_mathematik)

# Durchschnittsnote in Physik berechnen
durchschnitt_physik = sum(physik) / len(physik)
durchschnitt_noten.append(durchschnitt_physik)

# Durchschnittsnote in Chemie berechnen
durchschnitt_chemie = sum(chemie) / len(chemie)
durchschnitt_noten.append(durchschnitt_chemie)

# Ausgabe der Durchschnittsnoten
print("Durchschnittsnote in Mathematik:", durchschnitt_mathematik)
print("Durchschnittsnote in Physik:", durchschnitt_physik)
print("Durchschnittsnote in Chemie:", durchschnitt_chemie)
print("Durchschnittsnoten:", durchschnitt_noten)