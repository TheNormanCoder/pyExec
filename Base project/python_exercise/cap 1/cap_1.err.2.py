print("\n--- 1. Divisione per zero ---")
try:
    x = 5/0
except ZeroDivisionError as e:
    print(f"Errore: {e}")

print("\n--- 2. Operazioni tra tipi incompatibili ---")
try:
    y = "5" + 5
except TypeError as e:
    print(f"Errore: {e}")

print("\n--- 3. Indice fuori range ---")
try:
    lista = [1, 2, 3]
    elemento = lista[5]
except IndexError as e:
    print(f"Errore: {e}")

print("\n--- 4. Chiave non esistente ---")
try:
    dict = {"a": 1}
    valore = dict["b"]
except KeyError as e:
    print(f"Errore: {e}")

print("\n--- 5. Conversione non valida ---")
try:
    numero = int("ciao")
except ValueError as e:
    print(f"Errore: {e}")