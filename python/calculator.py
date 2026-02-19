from math import sqrt

welcome_message = "Benvenuto/a! Questa è un'applicazione che ti permetterà di fare calcoli come una calcolatrice. \nSeleziona una delle seguenti voci: \nPer effettuare un'Addizione, digita 1 \nPer effettuare una Sottrazione, digita 2 \nPer effettuare una Moltiplicazione, digita 3 \nPer effettuare una Divisione, digita 4 \nPer effettuare un Calcolo Esponenziale, digita 5 \nPer effettuare una Radice Quadrata, digita 6 \nPer uscire dal programma, digitare ESC"

while True:
    print(welcome_message)
    action = input("\nDigita la voce desiderata: ")

    if action == "1":
        print("\nHai selezionato Addizione")
        a = float(input("Inserisci il Primo numero: "))
        b = float(input("Inserisci il Secondo numero: "))
        print("Il risultato è: " + str(a+b))

    elif action == "2":
        print("\nHai selezionato Sottrazione")
        a = float(input("Inserisci il Primo numero: "))
        b = float(input("Inserisci il Secondo numero: "))
        print("Il risultato è: " + str(a-b))

    elif action == "3":
        print("\nHai selezionato Moltiplicazione")
        a = float(input("Inserisci il Primo numero: "))
        b = float(input("Inserisci il Secondo numero: "))
        print("Il risultato è: " + str(a*b))

    elif action == "4":
        print("\nHai selezionato Divisione")
        a = float(input("Inserisci il Primo numero: "))
        b = float(input("Inserisci il Secondo numero: "))
        print("Il risultato è: " + str(a/b))

    elif action == "5":
        print("\nHai selezionato Calcolo Esponenziale")
        a = float(input("Inserisci la Base: "))
        b = float(input("Inserisci l'Esponente: "))
        print("Il risultato è: " + str(a**b))
    
    elif action == "6":
        print("\nHai selezionato Radice Quadrata")
        a = float(input("Inserisci il Numero: "))
        print("Il risultato è: " + str(sqrt(a)))

    elif action == "ESC" or action == "esc":
        print("Applicazione in chiusura. Arrivederci!")
        break

    new_action = input("\nDesideri continuare ad utilizzare l'Applicazione? S/N ")
    
    if new_action == "S" or new_action == "s":
        print("Sto tornando al menù principale!\n")
        continue
    else:
        print("A presto!\n")
        break

