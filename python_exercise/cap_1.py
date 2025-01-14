##########################################
# 1. VARIABILI E TIPI DI DATI PRIMITIVI #
##########################################

# Interi (int)
età = 25                  # Numero intero positivo
temperatura = -5          # Numero intero negativo
numero_grande = 2**100    # Python gestisce automaticamente numeri grandi

# Decimali (float)
peso = 70.5              # Numero decimale positivo
temperatura = -3.8       # Numero decimale negativo
scientifico = 3.14e-10   # Notazione scientifica

# Stringhe (str)
nome = "Mario"           # Con doppi apici
cognome = 'Rossi'        # Con apici singoli
testo_lungo = """Questo è
un testo su più
righe"""                 # Con tripli apici

# Booleani (bool)
is_studente = True       # Valore booleano vero
is_docente = False       # Valore booleano falso

# None
valore_nullo = None      # Rappresenta l'assenza di valore

################################
# 2. COMMENTI E DOCUMENTAZIONE #
################################

# Questo è un commento su una linea

"""
Questo è un commento 
su più righe (docstring)
"""

def calcola_media(numeri):
    """
    Calcola la media di una lista di numeri.

    Args:
        numeri (list): Lista di numeri
    Returns:
        float: Media dei numeri
    """
    return sum(numeri) / len(numeri)

#########################
# 3. INPUT/OUTPUT BASE #
#########################

# Output base
print("Hello World!")                    # Stampa semplice
print("Nome:", nome, "Età:", età)        # Stampa multipla
print(f"Mi chiamo {nome} e ho {età} anni")  # f-string (consigliato)

# Input base
nome = input("Come ti chiami? ")         # Input come stringa
età = int(input("Quanti anni hai? "))    # Input convertito in intero

######################################
# 4. OPERATORI (aritmetici, confronto, logici) #
######################################

# Operatori Aritmetici
somma = 5 + 3           # 8
sottrazione = 5 - 3     # 2
moltiplicazione = 5 * 3 # 15
divisione = 5 / 3       # 1.6666... (restituisce sempre float)
divisione_intera = 5 // 3  # 1 (parte intera della divisione)
modulo = 5 % 3          # 2 (resto della divisione)
potenza = 5 ** 3        # 125 (5 elevato a 3)

# Operatori di Confronto
maggiore = 5 > 3        # True
minore = 5 < 3          # False
uguale = 5 == 3         # False
diverso = 5 != 3        # True
magg_uguale = 5 >= 3    # True
min_uguale = 5 <= 3     # False

# Operatori Logici
and_logico = True and False  # False
or_logico = True or False   # True
not_logico = not True      # False

####################################
# 5. TYPE CASTING E CONVERSIONI #
####################################

# Da stringa a numero
numero_da_stringa = int("123")      # 123
decimale_da_stringa = float("3.14") # 3.14

# Da numero a stringa
stringa_da_numero = str(123)        # "123"
stringa_da_float = str(3.14)        # "3.14"

# Conversioni booleane
bool_da_numero = bool(1)            # True (0 è False, tutti gli altri numeri True)
bool_da_stringa = bool("Ciao")      # True (stringa vuota è False, tutte le altre True)

# Verifica del tipo
print(type(123))        # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("ciao"))     # <class 'str'>
print(type(True))       # <class 'bool'>