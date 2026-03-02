"""
Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.

"""
numeri = [2, 4, 6, 8, 10]
risultato = 1
for i in numeri:
    risultato *= i
print("Il risultato della moltiplicazione tra tutti i numeri della lista è " + str(risultato))
