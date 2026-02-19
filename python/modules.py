import random, math

# Questo programma manda in output 10 numeri pseudo-casuali tra 1 e 50
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

# Radice quadrata
math.sqrt(25) #output 5

# Numero elevato alla potenza
math.pow(10, 2) #output 100

# Esponenziale e^x
math.exp(1)

# Arrotondamento
math.ceil(33.23) #per eccesso
math.floor(23.532) #per difetto

