liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Liste

# Funktion sum(list)
def summe(lst):
    summe = 0
    for num in lst:
        summe += num
    return summe

ergebnis_summe = summe(liste)  # Gibt die Summe der Liste aus
print(ergebnis_summe)

# Funktion average(list)
def durchschnitt(lst):
    summe = 0
    for num in lst:
        summe += num
    return summe / len(lst)

ergebnis_durchschnitt = durchschnitt(liste)  # Gibt den Durchschnitt der Liste aus
print(ergebnis_durchschnitt)