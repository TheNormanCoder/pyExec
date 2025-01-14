# Errori comuni in Python
print("\n--- Errori Comuni in Python ---")

# 1. Divisione per zero
x = 5/0  # ZeroDivisionError

# 2. Operazioni tra tipi incompatibili
y = "5" + 5  # TypeError: can't concat str to int

# 3. Indice fuori range
lista = [1, 2, 3]
elemento = lista[5]  # IndexError: list index out of range

# 4. Chiave non esistente in dizionario
dict = {"a": 1}
valore = dict["b"]  # KeyError: 'b'

# 5. Conversione non valida
numero = int("ciao")  # ValueError: invalid literal for int()