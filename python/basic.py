# questo è un commento
print("Hello world!")

# Inizializziamo una variabile
x = 2
print(x)

# Tipi di dato
val = 123 #int
vir = 3.5 #float
stringa = "Questa è una stringa" #str
vero = True #bool

# Concatenare le stringhe
eggs = "Meglio un uovo oggi..."
bacon = "o una gallina domani?"
frase_intera = eggs + " " + bacon
print(frase_intera)

# Escape delle doppie virgolette
frase1 = "e Dante scrisse: \"Nel mezzo del cammin di nostra vita...\""
#oppure
frase2 = 'e Dante scrisse: "Nel mezzo del cammin di nostra vita..."'
print(frase1)
print(frase2)

# Concatenare due dipi di dato diversi
text = "La mia età è "
age = 26
# text + age darà errore -> TypeError: can only concatenate str (not "int") to str
text + str(age)

# "Trasformare" un tipo di dato
arance_per_sacco = "13" #str

arance_per_sacco * 3 #output '131313'
int(arance_per_sacco) * 3 #output 39
float(age) #output 26.0

# Calcolare la lunghezza di un dato
whetting_your_appetite = """Python is an easy to learn, powerful
programming language. It has efficient high-level data structures and
a simple but effective approach to object-oriented
programming. Python’s elegant syntax and dynamic typing, together with
its interpreted nature, make it an ideal language for scripting and
rapid application development in many areas on most platforms."""

# Enter your code below:
print(len(whetting_your_appetite))

# Operatori numerici
somma = 8 + 5
diff = 8 - 5
molt = 8 * 5
div = 40 / 8
floor = 42 / 5
print(somma)
print(diff)
print(molt)
print(div)
print(floor)

# Calcolo esponenziale 
esp = 3 ** 3
print(esp)

# Divisione intera (floor division)
floor_division = 30 // 7
print(floor_division)

# La funzione isinstance() viene utilizzata per verificare se un oggetto è di un certo tipo o se è una sottoclasse di quel tipo
# isinstance(object, type)
x = 34
isinstance(x, int) #output True
isinstance(x, str) #output False

# Operatori di comparazione
5 == 5 #Uguale
5 != 6 #Non uguale
5 < 6 #Minore di
6 > 5 #Maggiore di
5 <= 6 #Minore o uguale di
6 >= 5 #Maggiore o uguale di

# Operatori Booleani (AND, OR, NOT)
# AND entrambe le parti devono essere VERE per dare TRUE
21 > 1 and 3 < 5 #True
22 == 22 and 1 > 2 #False
2 < 1 and "asd" == "asd" #False
23 == 15 and 33 != 33 #False
# OR almeno una parte deve essere VERA oer dare TRUE
25 >= 25 or 23 <= 25 #True
"io" == "io" or "io" == "robot" #True
4 == 5 or 5 == 6 #False

# NOT se una comparazione risulta non True sarà chiaramente False, e viceversa
not "io" == "robot" #True
not 3 == 3 #False

# IF
if age >= 18:
    print("Sei maggiorenne")

age = 16
if age >= 18:
    print("Sei maggiorenne")

# ELSE
if age >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

# ELSE IF
age = 18
license = False

if age >= 18 and license == True:
    print("Puoi noleggiare un auto!")
elif age >= 18 and license == False:
    print("Fatti prima la patente!")
else:
    print("Ritorna fra qualche anno...")

# Ciclo WHILE
i = 0
while i <= 10:
    print(i)
    i += 1

# Ciclo infinito
#run = True
#while run:
#    print(i)
#    i += 1

# BREAK
run = True
stop = 100
counter = 0

while run:
    print(counter)
    counter += 1
    if counter > stop:
        print("Sto uscendo dal loop...")
        break

# CONTINUE
skip = 5
counter = 0

while counter < 10:
    counter += 1
    if counter == skip:
        print("Skip " + str(skip))
        continue
    print(counter)

# FOR
for i in range (11):
    print(i)

# Funzione range(start, stop, step)
for i in range(2, 11, 2):
    print(i)

for countdouwn in range(10, -1, -1):
    print(countdouwn)

# Funzioni
# Definizione della funzione
def say_my_name():
    name = input("Come ti chiami? ")
    print("Benvenut* ", name)

# Chiamata della funzione
# say_my_name()

def addizione(a, b, c=0):
    """
    Questa funzione prende due o tre argomenti, a, b e c(facoltativa) e restituisce la loro somma.

    :param a: Primo numero da sommare
    :param b: Secondo numero da sommare
    :param c: Terzo numero da sommare (facoltativo)
    Return: 
        Stringa che contiene il risultato della somma dei parametri
    """
    risultato = a + b + c
    print("Il risultato dell'addizione è " + str(risultato))

addizione(51, 3)
