"""
Scrivi un programma che chieda all'utente una stringa composta da un
solo carattere e dica se si tratta di una vocale oppure no.

"""

vocals = ["a", "e", "i", "o", "u"]
# oppure vocals = "aeiou"
user_letter = input("Inserisci una lettera: ").lower()
if len(user_letter) > 1:
    print("Hai inserito più di una lettera.")
else:
    if user_letter in vocals:
        print("La lettera " + user_letter.upper() + " è una vocale.")
    else:
        print("La lettera " + user_letter.upper() + " non è una vocale.")
