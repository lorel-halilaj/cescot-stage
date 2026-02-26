"""
Scrivi un programma che chieda due numeri all'utente tramite la funzione input
e mostri il più grande tra i due utilizzando la funzione print.

"""
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
if a > b:
    print(str(a) + " è maggiore di " + str(b))
else:
    print(str(b) + " è maggiore di " + str(a))
