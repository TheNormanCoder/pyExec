##########################################
# 1. VARIABILI E TIPI DI DATI PRIMITIVI #
##########################################

# Interi (int)
età = 25
temperatura = -5
numero_grande = 2**100
print("\n--- Interi ---")
print(f"età: {età}")
print(f"temperatura: {temperatura}")
print(f"numero_grande: {numero_grande}")

# Decimali (float)
peso = 70.5
temperatura_decimale = -3.8
scientifico = 3.14e-10
print("\n--- Decimali ---")
print(f"peso: {peso}")
print(f"temperatura_decimale: {temperatura_decimale}")
print(f"scientifico: {scientifico}")

# Stringhe (str)
nome = "Mario"
cognome = 'Rossi'
testo_lungo = """Questo è
un testo su più
righe"""
print("\n--- Stringhe ---")
print(f"nome: {nome}")
print(f"cognome: {cognome}")
print(f"testo_lungo:\n{testo_lungo}")

# Booleani (bool)
is_studente = True
is_docente = False
print("\n--- Booleani ---")
print(f"is_studente: {is_studente}")
print(f"is_docente: {is_docente}")

######################################
# 4. OPERATORI #
######################################

print("\n--- Operatori Aritmetici ---")
somma = 5 + 3
sottrazione = 5 - 3
moltiplicazione = 5 * 3
divisione = 5 / 3
divisione_intera = 5 // 3
modulo = 5 % 3
potenza = 5 ** 3

print(f"somma (5 + 3): {somma}")
print(f"sottrazione (5 - 3): {sottrazione}")
print(f"moltiplicazione (5 * 3): {moltiplicazione}")
print(f"divisione (5 / 3): {divisione}")
print(f"divisione_intera (5 // 3): {divisione_intera}")
print(f"modulo (5 % 3): {modulo}")
print(f"potenza (5 ** 3): {potenza}")

print("\n--- Operatori di Confronto ---")
maggiore = 5 > 3
minore = 5 < 3
uguale = 5 == 3
diverso = 5 != 3
magg_uguale = 5 >= 3
min_uguale = 5 <= 3

print(f"5 > 3: {maggiore}")
print(f"5 < 3: {minore}")
print(f"5 == 3: {uguale}")
print(f"5 != 3: {diverso}")
print(f"5 >= 3: {magg_uguale}")
print(f"5 <= 3: {min_uguale}")

print("\n--- Operatori Logici ---")
and_logico = True and False
or_logico = True or False
not_logico = not True

print(f"True and False: {and_logico}")
print(f"True or False: {or_logico}")
print(f"not True: {not_logico}")

####################################
# 5. TYPE CASTING E CONVERSIONI #
####################################

print("\n--- Type Casting ---")
# Da stringa a numero
numero_da_stringa = int("123")
decimale_da_stringa = float("3.14")
print(f"int('123'): {numero_da_stringa}")
print(f"float('3.14'): {decimale_da_stringa}")

# Da numero a stringa
stringa_da_numero = str(123)
stringa_da_float = str(3.14)
print(f"str(123): {stringa_da_numero}")
print(f"str(3.14): {stringa_da_float}")

# Conversioni booleane
bool_da_numero = bool(1)
bool_da_stringa = bool("Ciao")
print(f"bool(1): {bool_da_numero}")
print(f"bool('Ciao'): {bool_da_stringa}")