# In Python:
print("\n--- Comportamenti dei tipi in Python ---")

# 1. Divisioni per zero
try:
    x = 5/0
except ZeroDivisionError:
    print("In Python: Errore divisione per zero")  # Genera un errore chiaro

# 2. Conversioni tra tipi sono esplicite
numero = 5
stringa = "10"
# print(numero + stringa)    # Questo darebbe errore in Python
print(f"Conversione esplicita: {numero + int(stringa)}")  # Devi convertire esplicitamente

# 3. Confronti sono prevedibili
print(f"1 == '1': {1 == '1'}")         # False (tipi diversi)
print(f"True == 1: {True == 1}")       # True (questo è uno dei pochi casi speciali)
print(f"False == 0: {False == 0}")     # True (questo è uno dei pochi casi speciali)

# 4. None è unico (simile a null in JS)
print(f"None == 0: {None == 0}")       # False
print(f"None == False: {None == False}")# False

# 5. Bool conversioni sono chiare
print("\n--- Valori che sono False in Python ---")
print(f"bool(0): {bool(0)}")           # False
print(f"bool(''): {bool('')}")         # False
print(f"bool([]): {bool([])}")         # False
print(f"bool(None): {bool(None)}")     # False