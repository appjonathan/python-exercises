gesamtKisten = 1000  # Gesamtanzahl der Kisten
kistenProFahrt = 75  # Anzahl der Kisten, die pro Fahrt transportiert werden

anzahlFahrten = gesamtKisten // kistenProFahrt  # Anzahl der Fahrten berechnen
print('Anzahl der Fahrten: ', anzahlFahrten) # Ausgabe: Anzahl der Fahrten

kistenInLetzterFahrt = gesamtKisten % kistenProFahrt  # Kisten in der letzten Fahrt berechnen
print('Kisten in der letzten Fahrt: ', kistenInLetzterFahrt) # Ausgabe: Kisten in letzter Fahrt