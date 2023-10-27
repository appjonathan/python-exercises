# Diese Funktion verschlüsselt den eingegebenen Text mit der Caesar-Chiffre
def caesar_verschluesseln(text, schluessel):
    verschluesselter_text = ""  # Initialisierung des verschlüsselten Texts
    for zeichen in text:
        if zeichen.isalpha():  # Überprüft, ob das Zeichen ein Buchstabe ist
            if zeichen.isupper():  # Überprüft, ob es ein Großbuchstabe ist
                # Verschlüsselt den Großbuchstaben und fügt ihn zum verschlüsselten Text hinzu
                verschluesselter_text += chr((ord(zeichen) - ord('A') + schluessel) % 26 + ord('A'))
            else:
                # Verschlüsselt den Kleinbuchstaben und fügt ihn zum verschlüsselten Text hinzu
                verschluesselter_text += chr((ord(zeichen) - ord('a') + schluessel) % 26 + ord('a'))
        else:
            # Fügt das Zeichen unverändert hinzu, falls es kein Buchstabe ist
            verschluesselter_text += zeichen
    return verschluesselter_text  # Gibt den verschlüsselten Text zurück

# Diese Funktion entschlüsselt den verschlüsselten Text
def caesar_entschluesseln(verschluesselter_text, schluessel):
    # Die Entschlüsselung wird durchgeführt, indem der negative Schüssel verwendet wird
    return caesar_verschluesseln(verschluesselter_text, -schluessel)

# Diese Funktion startet das Caesar-Chiffre Programm
def main():
    while True:
        print("Willkommen zur Caesar-Verschlüsselung!")
        text = input("Geben Sie den Text ein: ")  # Benutzer gibt den zu verschlüsselnden Text ein
        schluessel = int(input("Geben Sie den Verschlüsselungsschlüssel ein (-25 bis +25): "))  # Benutzer gibt den Verschlüsselungsschlüssel ein
        modus = input("Wählen Sie den Modus (verschlüsseln/entschlüsseln): ")  # Benutzer wählt den Modus
        
        if modus.lower() == "verschlüsseln":
            # Wenn der Benutzer den Verschlüsselungsmodus auswählt, wird die Verschlüsselungsfunktion aufgerufen
            verschluesselter_text = caesar_verschluesseln(text, schluessel)
            print("Verschlüsselter Text:", verschluesselter_text)
        elif modus.lower() == "entschlüsseln":
            # Wenn der Benutzer den Entschlüsselungsmodus auswählt, wird die Entschlüsselungsfunktion aufgerufen
            entschluesselter_text = caesar_entschluesseln(text, schluessel)
            print("Entschlüsselter Text:", entschluesselter_text)
        else:
            # Falls der Benutzer einen ungültigen Modus eingibt, wird eine Fehlermeldung ausgegeben
            print("Ungültiger Modus!")
        
        weiter = input("Möchten Sie eine weitere Nachricht verschlüsseln oder entschlüsseln? (ja/nein): ")
        if weiter.lower() != "ja":
            # Der Benutzer wird gefragt, ob er weitere Nachrichten verschlüsseln oder entschlüsseln möchte. Wenn nicht, wird die Schleife beendet.
            break

# Die Hauptfunktion wird aufgerufen, um das Programm zu starten
main()