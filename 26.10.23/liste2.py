liste = [1, 2, 3, 2, 4, 4, 4, 4] # Liste

# Funktion summe(liste)
def summe(liste):
    summe = 0
    for element in liste:
        summe += element
    return summe

ergebnis_summe = summe(liste)  # Gibt die Summe der Liste aus
print(ergebnis_summe)

# Funktion durchschnitt(liste)
def durchschnitt(liste):
    summe_der_liste = summe(liste)
    anzahl_der_elemente = len(liste)
    durchschnitt = summe_der_liste / anzahl_der_elemente
    return durchschnitt

ergebnis_durchschnitt = durchschnitt(liste)  # Gibt den Durchschnitt der Liste aus
print(ergebnis_durchschnitt)

# Funktion wahrscheinlichkeiten(liste)
def wahrscheinlichkeiten(liste):
    anzahl_der_elemente = len(liste)
    unique_elemente = list(set(liste))
    for element in unique_elemente:
        anzahl_element = liste.count(element)
        wahrscheinlichkeit = anzahl_element / anzahl_der_elemente
        print(f"{element}: == {wahrscheinlichkeit*100}%")

wahrscheinlichkeiten(liste)  # Gibt die Wahrscheinlichkeiten für die einzelnen Listeneinträge aus