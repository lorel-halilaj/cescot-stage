"""
Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

"""

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
c = input("Inserisci il terzo numero: ")
maggiore = max(a, b, c)

print("Il numero maggiore è " + str(maggiore))