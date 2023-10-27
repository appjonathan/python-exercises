'''
Aufgabe:
Nehmen wir an, wir hätten eine Spedition. Wir bekommen einen Großauftrag und müssen 1.000 Kisten ausliefern.
In unseren Lkw passen pro Fahrt jedoch nur 75 Kisten. Berechnen Sie, wie oft wir fahren müssen und wie viele Kisten in der letzten Fahrt transportiert werden.
'''

gesamtKisten = 1000  # Gesamtanzahl der Kisten
kistenProFahrt = 75  # Anzahl der Kisten, die pro Fahrt transportiert werden

anzahlFahrten = gesamtKisten // kistenProFahrt + 1  # Anzahl der Fahrten berechnen
print('Anzahl der Fahrten: ', anzahlFahrten) # Ausgabe: Anzahl der Fahrten

kistenInLetzterFahrt = gesamtKisten % kistenProFahrt  # Kisten in der letzten Fahrt berechnen
print('Kisten in der letzten Fahrt: ', kistenInLetzterFahrt) # Ausgabe: Kisten in letzter Fahrt