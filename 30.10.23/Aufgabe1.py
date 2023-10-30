produkte = [
    ("Laptop", 899.99, 4.6, True),
    ("Smartphone", 549.99, 4.2, True),
    ("Tablet", 299.99, 3.9, False),
    ("Kopfhörer", 149.99, 4.8, True),
    ("Maus", 19.99, 4.1, True),
]

# Aufagbe1: Liste die nur die Namen der Produkte enthält, die derzeit verfügbar sind
verfuegbare_produkte = [produkt[0] for produkt in produkte if produkt[3]]

# Aufgabe2: Liste von Produkten die einen Preis von weniger als 50 Euro und eine Bewertung von mindestens 4 von 5 Sternen haben
gewuenschte_produkte = [produkt[0] for produkt in produkte if produkt[1] < 50 and produkt[2] >= 4]

# Aufgabe3: Berechne den Durchschnittspreis aller Produkte
durchschnittspreis = sum(produkt[1] for produkt in produkte) / len(produkte)

# Aufgabe4: Finde das teuerste Produkt in der Liste
teuerstes_produkt = max(produkte, key=lambda produkt: produkt[1])

# Ausgabe Aufgabe1
print("Aufgabe1: Verfügbare Produkte: ", verfuegbare_produkte) 
# Ausgabe Aufgabe2
print("Aufgabe2: Produkte unter 50€ mit 4+ Bewertung: ", gewuenschte_produkte) 
# Ausgabe Aufgabe3
print("Aufgabe3: Durchschnittspreis der Produkte: ", durchschnittspreis)
# Ausgabe Aufgabe4
print("Aufgabe4: Teuerstes Produkt: ", teuerstes_produkt)