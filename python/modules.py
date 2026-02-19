import random # questo programma manda in output 10 numeri pseudo-casuali tra 1 e 50

ran = random.random()
print(ran)

# Genera un numero intero casuale compreso tra i valori a e b (con a e b inclusi)
for numero in range(10):
    val = random.randint(1, 50)
    print(val)

# Metodo randrange(start, stop[, step])
num_pari = random.randrange(0, 11, 2)
num_dispari = random.randrange(1, 11, 2)

# Metodo choice(seq)
lista = ['Italia', 'Francia', 'Spagna', 'Portogallo']

ran_state = random.choice(lista)
print(ran_state)
