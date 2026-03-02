'''
Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

'''

numeri = [23, 12, 11, 34, 76, 54, 67, 89, 71, 22, 45, 98]
risultato = 0
for i in numeri:
    risultato += i
print("La somma dei numeri della lista è " + str(risultato))
