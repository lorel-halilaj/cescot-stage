"""
Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

"""
def maggiore(a, b, c):
    """
    Questa funzione chiede all'utente tre numeri (a, b e c) e restituisce il maggiore.

    :param a: Primo numero
    :param b: Secondo numero
    :param c: Terzo numero
    
    """
    a = input("Inserisci il primo numero: ")
    b = input("Inserisci il secondo numero: ")
    c = input("Inserisci il terzo numero: ")
    maggiore = max(a, b, c)
    return maggiore

print("Il numero maggiore è " + maggiore)