"""
Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.

"""
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
if a > b:
    print(str(a) + " è maggiore di " + str(b))
else: 
    print(str(b) + " è maggiore di " + str(a))