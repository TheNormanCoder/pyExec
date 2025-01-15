print("\n=== CONCETTI FONDAMENTALI AGGIUNTIVI PYTHON ===")

#########################################
# 1. ASSEGNAZIONE MULTIPLA
#########################################
print("\n--- Assegnazione Multipla ---")
# Assegnazione multipla di variabili
a, b = 1, 2
x = y = z = 0

print(f"a: {a}, b: {b}")
print(f"x: {x}, y: {y}, z: {z}")

#########################################
# 2. OPERATORI DI ASSEGNAZIONE COMPOSTI
#########################################
print("\n--- Operatori di Assegnazione Composti ---")
x = 5
print(f"Valore iniziale di x: {x}")

x += 3
print(f"Dopo x += 3: {x}")  # 8

x -= 2
print(f"Dopo x -= 2: {x}")  # 6

x *= 4
print(f"Dopo x *= 4: {x}")  # 24

x /= 2
print(f"Dopo x /= 2: {x}")  # 12.0

#########################################
# 3. CARATTERI SPECIALI NELLE STRINGHE
#########################################
print("\n--- Caratteri Speciali nelle Stringhe ---")
testo = "Riga 1\nRiga 2\tTabulazione"
percorso = r"C:\cartella\nome"  # raw string
print("Testo con caratteri speciali:")
print(testo)
print("Raw string (r-string):")
print(percorso)

#########################################
# 4. DELIMITATORI DI STRINGA
#########################################
print("\n--- Delimitatori di Stringa ---")
stringa1 = 'testo con apici singoli'
stringa2 = "testo con apici doppi"
stringa3 = '''testo
su più
righe'''

print(f"Apici singoli: {stringa1}")
print(f"Apici doppi: {stringa2}")
print("Stringa multilinea:")
print(stringa3)

#########################################
# 5. PRIORITÀ DEGLI OPERATORI
#########################################
print("\n--- Priorità degli Operatori ---")
risultato1 = 5 + 3 * 2
print(f"5 + 3 * 2 = {risultato1}")  # prima la moltiplicazione

risultato2 = (5 + 3) * 2
print(f"(5 + 3) * 2 = {risultato2}")  # le parentesi hanno precedenza

#########################################
# 6. FORMATTAZIONE DELLE STRINGHE
#########################################
print("\n--- Formattazione delle Stringhe ---")
nome = "Mario"
età = 30

# Vecchi metodi di formattazione
print("Con %%: Nome %s, Età %d" % (nome, età))           # % formatting
print("Con .format(): Nome {}, Età {}".format(nome, età))  # str.format()
print("Con parametri: Nome {n}, Età {e}".format(n=nome, e=età))  # named formatting
print(f"Con f-string: Nome {nome}, Età {età}")           # f-strings (moderno)

#########################################
# 7. CARATTERI DI ESCAPE
#########################################
print("\n--- Caratteri di Escape ---")
print("1. Virgolette: \"dentro\" una stringa")
print('2. Apice: \'dentro\' una stringa')
print("3. Backslash: \\")
print("4. Tabulazione:\tDopo tab")
print("5. Nuova riga:\nNuova riga")

#########################################
# 8. CONTROLLO DEL TIPO
#########################################
print("\n--- Controllo del Tipo ---")
x = 5
y = 3.14
z = "Hello"

print(f"1. Tipo di x: {type(x)}")
print(f"2. x è un intero? {isinstance(x, int)}")
print(f"3. y è un float? {isinstance(y, float)}")
print(f"4. z è una stringa? {isinstance(z, str)}")
print(f"5. x è un numero? {isinstance(x, (int, float))}")

print("\n=== FINE DEI CONCETTI FONDAMENTALI AGGIUNTIVI ===")