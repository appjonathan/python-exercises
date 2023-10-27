# Funktion from_to(start, end)
def from_to(start, end):
    for i in range(start, end):
        print(i)

from_to(1, 101)  # Gibt die Zahlen von 1 bis 100 aus

# Funktion div_by6()
def div_by6():
    for i in range(1, 101):
        if i % 6 == 0:
            print(i)

div_by6()      # Gibt die Zahlen von 1 bis 100 aus, die durch 6 teilbar sind

# Funktion fizzbuzz()
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()     # Gibt die Zahlen von 1 bis 100 aus, wobei bestimmte Bedingungen erfüllt sind