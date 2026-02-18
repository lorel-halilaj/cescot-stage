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
text + age #Risulterà errore -> TypeError: can only concatenate str (not "int") to str
text + str(age)

# "Trasformare" un tipo di dato
arance_per_sacco = "13" #str

arance_per_sacco * 3 #output '131313'
int(arance_per_sacco) * 3 #output 39
float(age) #output 26.0

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
