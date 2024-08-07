'''
Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima 
chiave che corrisponde a quel valore, o None se il valore non è presente.
'''
def trova_chiave(dizionario, valore):
    for chiave, valore_diz in dizionario.items():
        if valore_diz == valore:
            return chiave
    return None
'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. 
Se ci sono valori duplicati, scarta i duplicati.
'''
def inverti_dizionario(dizionario):
    dizionario_invertito = {}
    for chiave, valore in dizionario.items():
        if valore not in dizionario_invertito:
            dizionario_invertito[valore] = chiave
    return dizionario_invertito

'''
Scrivi una funzione che determina se un numero è 'magico'. Un numero è 
considerato magico se è divisibile per 4 ma non per 6.
'''
def e_magico(numero):
    return numero % 4 == 0 and numero % 6 != 0

'''
Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei 
numeri che sono divisibili sia per 2 che per 3.
'''
def funzione(lista_numeri):
    somma = 0
    for i in lista_numeri:
        if i % 2 == 0 and i % 3 == 0:
            somma += i
    return somma
            
numeri = [1, 2, 3, 6, 12, 18, 20, 24]
somma = funzione(numeri)
print(somma)
    
'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo 
superiore a 20, scontati del 10%.
''' 
def prodotti_scontati(dizionario_prodotti):
    dizionario_scontato = {}
    for prodotto, prezzo in dizionario_prodotti.items():
        if prezzo > 20:
            dizionario_scontato[prodotto] = prezzo * 0.9  # Applica uno sconto del 10%
    return dizionario_scontato

'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano
voti di studenti e aggrega i voti per studente in un nuovo dizionario.
'''
def aggrega_voti(lista_voti):
    dizionario_aggregato = {}
    for voto in lista_voti:
        studente = voto['studente']
        voto_valore = voto['voto']
        if studente in dizionario_aggregato:
            dizionario_aggregato[studente].append(voto_valore)
        else:
            dizionario_aggregato[studente] = [voto_valore]
    return dizionario_aggregato

# Esempio di utilizzo
voti_studenti = [
    {'studente': 'Alice', 'voto': 8},
    {'studente': 'Bob', 'voto': 7},
    {'studente': 'Alice', 'voto': 9},
    {'studente': 'Bob', 'voto': 6},
    {'studente': 'Charlie', 'voto': 10}
]

voti_aggregati = aggrega_voti(voti_studenti)
print(voti_aggregati)
# Output: {'Alice': [8, 9], 'Bob': [7, 6], 'Charlie': [10]}

'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati 
in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e 
il numero di volte che devono essere rimossi come valori.
'''

def rimuovi_elementi(lista, elementi_da_rimuovere):
    for elemento, conteggio in elementi_da_rimuovere.items():
        for _ in range(conteggio):
            if elemento in lista:
                lista.remove(elemento)
    return lista 

'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un 
dizionario. Se la chiave è già presente, aggiungi il valore alla lista di 
valori già associata alla chiave.
'''

def converti_in_dizionario(lista_tuples):
    dizionario = {}
    for chiave, valore in lista_tuples:
        if chiave in dizionario:
            dizionario[chiave].append(valore)
        else:
            dizionario[chiave] = [valore]
    return dizionario

'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che 
classifica i numeri in liste separate per numeri pari e dispari.
'''
def classifica_pari_dispari(lista_numeri):
    dizionario_classificato = {'pari': [], 'dispari': []}
    for numero in lista_numeri:
        if numero % 2 == 0:
            dizionario_classificato['pari'].append(numero)
        else:
            dizionario_classificato['dispari'].append(numero)
    return dizionario_classificato

# Esempio di utilizzo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dizionario_classificato = classifica_pari_dispari(numeri)
print(dizionario_classificato)

'''
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e 
viceversa a seconda del parametro. Utilizza il concetto di parametri opzionali.
'''

def converti_temperatura(temperatura, scala='C'):
    """
    Converte una temperatura da Celsius a Fahrenheit e viceversa.
    
    Args:
    temperatura (float): La temperatura da convertire.
    scala (str): La scala di destinazione. 'C' per Celsius, 'F' per Fahrenheit. Default è 'C'.
    
    Returns:
    float: La temperatura convertita.
    """
    if scala == 'C':
        # Converti da Fahrenheit a Celsius
        return (temperatura - 32) * 5 / 9
    elif scala == 'F':
        # Converti da Celsius a Fahrenheit
        return (temperatura * 9 / 5) + 32
    else:
        raise ValueError("La scala deve essere 'C' per Celsius o 'F' per Fahrenheit.")

# Esempio di utilizzo
temperatura_celsius = 25
temperatura_fahrenheit = converti_temperatura(temperatura_celsius, scala='F')
print(f"{temperatura_celsius}°C = {temperatura_fahrenheit}°F")

temperatura_fahrenheit = 77
temperatura_celsius = converti_temperatura(temperatura_fahrenheit, scala='C')
print(f"{temperatura_fahrenheit}°F = {temperatura_celsius}°C")

'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono 
maggiori di un dato valore intero definito threshold.
'''
def somma_maggiori(lista_interi, valore):
    somma = 0
    for i in lista_interi:
        if i > valore:
            somma += i
    return somma

'''
 Scrivi una funzione che, data una lista, ritorni un dictionary che mappa 
 ogni elemento alla sua frequenza nella lista.
'''
def frequenza(lista):
    dizionario = {}
    for i in lista:
        if i in dizionario:
            dizionario[i] += 1
        else:
            dizionario[i] = 1

    return dizionario
lista1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
dict = frequenza(lista1)
print(dict)

'''
Scrivi una funzione che ritorna un dizionario che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.
'''

def unisci_dizionari(dizionario1, dizionario2):
    dizionario_unito = dizionario1.copy()  # Crea una copia del primo dizionario
    for chiave, valore in dizionario2.items():
        if chiave in dizionario_unito:
            dizionario_unito[chiave] += valore  # Somma i valori se la chiave è presente in entrambi i dizionari
        else:
            dizionario_unito[chiave] = valore  # Aggiunge la nuova chiave e valore
    return dizionario_unito   

'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da 
rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
'''
def rimuovi(lista1,lista2):
    nuova_lista = lista1.copy()
    for i in lista2:
        if i in nuova_lista:
            nuova_lista.remove(i)
    return nuova_lista

lista1 = {1, 2, 3, 4, 5, 6}
lista2 = [2, 4, 6]

nuova_lista = rimuovi(lista1, lista2)
print(nuova_lista)

'''
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una 
lista di numeri interi.
'''
def statistiche_lista(lista):
    if not lista:
        return None, None, None
    
    massimo = max(lista)
    minimo = min(lista)
    media = sum(lista) / len(lista)
    
    return massimo, minimo, media

# Esempio di utilizzo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

massimo, minimo, media = statistiche_lista(numeri)
print(massimo,minimo,media)

#se volessi calcolare il massimo , il minimo e la media con un for ?

def statistiche_lista_con_for(lista):
    if not lista:
        return None, None, None
    
    massimo = lista[0]
    minimo = lista[0]
    somma = 0
    
    for numero in lista:
        if numero > massimo:
            massimo = numero
        if numero < minimo:
            minimo = numero
        somma += numero
    
    media = somma / len(lista)
    
    return massimo, minimo, media

# Esempio di utilizzo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

massimo, minimo, media = statistiche_lista_con_for(numeri)
print(f"Massimo: {massimo}, Minimo: {minimo}, Media: {media}")
# Output: Massimo: 10, Minimo: 1, Media: 5.5

'''
Scrivi una funzione che calcola la media di una lista di numeri e 
ritorna il valore arrotondato all'intero più vicino.
'''
def media_arrotondata(lista):
    if not lista:
        return None
    
    somma = 0
    for numero in lista:
        somma += numero
    
    media = somma / len(lista)
    
    # Arrotonda all'intero più vicino
    media_arrotondata = round(media)
    
    return media_arrotondata

# Esempio di utilizzo
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media_arrotondata_valore = media_arrotondata(numeri)
print(f"Media arrotondata: {media_arrotondata_valore}")
# Output: Media arrotondata: 6

'''
18. Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
'''

def rimuovi_duplicati(lista):
    elementi_unici = []
    insieme_visti = set()
    for elemento in lista:
        if elemento not in insieme_visti:
            elementi_unici.append(elemento)
            insieme_visti.add(elemento)
    return elementi_unici

# Esempio di utilizzo
lista = [1, 2, 3, 1, 4, 2, 5, 'a', 'b', 'a', 'c']
lista_senza_duplicati = rimuovi_duplicati(lista)
print(lista_senza_duplicati)
# Output: [1, 2, 3, 4, 5, 'a', 'b', 'c']

'''
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un 
numero specificato k di posizioni. La rotazione verso sinistra significa che 
ciascun elemento della lista viene spostato a sinistra di una posizione e 
l'elemento iniziale viene spostato alla fine della lista. Per la rotazione 
utilizzare lo slicing e gestire il caso in cui il numero specificato di 
posizioni sia maggiore della lunghezza della lista.
'''

def ruota_sinistra(lista, k):
    if not lista:
        return lista  # Verifica se la lista è vuota. Se lo è, ritorna 
                      # la lista così com'è.

    lunghezza = len(lista)
    k = k % lunghezza  # Gestisce il caso in cui k sia maggiore della lunghezza della lista
    
    return lista[k:] + lista[:k]

# Esempio di utilizzo
lista = [1, 2, 3, 4, 5, 6, 7]
k = 3
lista_ruotata = ruota_sinistra(lista, k)
print(lista_ruotata)
# Output: [4, 5, 6, 7, 1, 2, 3]


'''
Scrivi una funzione che accetti tre parametri: username, password e status 
di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo 
se il nome utente è "admin", la password corrisponde a "12345" e l'account è 
attivo.
'''

def accesso(username, password, status):
    # Verifica se il nome utente è "admin"
    if username == "admin":
        # Verifica se la password corrisponde a "12345"
        if password == "12345":
            # Verifica se lo status è "attivo"
            if status == "attivo":
                return "Accesso consentito"
            else:
                return "Account non attivo"
        else:
            return "Password errata"
    else:
        return "Nome utente errato"

# Esempio di utilizzo
username = "admin"
password = "12345"
status = "attivo"

esito = accesso(username, password, status)
print(esito)  # Output: Accesso consentito

'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
è soddisfatta per procedere con un'operazione. L'operazione può procedere 
solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
'''
def verifica_condizioni(A, B, C):
    if A or (B and C):
        return "Operazione consentita"
    else:
        return "Operazione non consentita"
    
'''
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da 
quel numero a zero.
'''

def conto_alla_rovescia(numero):
    if numero < 0:
        print("Il numero deve essere maggiore o uguale a zero.")
        return
    
    for i in range(numero, -1, -1):
        print(i)

'''
Scrivi una funzione che, dato un numero intero, determina se è un 
"numero magico". Un numero magico è definito come un numero che contiene il 
numero 7.'''

def e_numero_magico(numero):
    # Converte il numero in una stringa
    numero_str = str(numero)
    # Controlla se la stringa '7' è presente nella rappresentazione in stringa del numero
    if '7' in numero_str:
        return True
    else:
        return False

'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono 
bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi 
che chiude.'''

def parentesi_bilanciate(s):
    # Inizializza un contatore per tenere traccia delle parentesi aperte
    bilanciamento = 0
    
    # Itera attraverso ogni carattere nella stringa
    for char in s:
        # Incrementa il contatore per ogni parentesi aperta
        if char == '(':
            bilanciamento += 1
        # Decrementa il contatore per ogni parentesi chiusa
        elif char == ')':
            bilanciamento -= 1
            
        # Se il contatore è negativo, significa che c'è una parentesi chiusa senza la corrispondente parentesi aperta
        if bilanciamento < 0:
            return False
    
    # Alla fine, il contatore dovrebbe essere zero se tutte le parentesi sono bilanciate
    return bilanciamento == 0

# Esempio di utilizzo
print(parentesi_bilanciate("(())"))  # Output: True
print(parentesi_bilanciate("((())"))  # Output: False
print(parentesi_bilanciate(")("))  # Output: False
print(parentesi_bilanciate("()()"))  # Output: True


'''
Scrivi una funzione che conta quante volte un elemento appare isolato in una 
lista di numeri interi. Un elemento è considerato isolato se non è affiancato 
da elementi uguali.'''


def conta_isolati(lista):
    if not lista:
        return 0

    count = 0
    lunghezza = len(lista)

    for i in range(lunghezza):
        if (i == 0 or lista[i] != lista[i - 1]) and (i == lunghezza - 1 or lista[i] != lista[i + 1]):
            count += 1

    return count

'''
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe 
restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", 
telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 
'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo 
da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 
'telefono': 123456789}'''

def create_contact(nome_cognome, email=None, telefono=None):
    contatto = {'profile': nome_cognome}
    if email:
        contatto['email'] = email
    if telefono:
        contatto['telefono'] = telefono
    return contatto

def update_contact(dizionario_contatto, nome_cognome, email=None, telefono=None):
    if dizionario_contatto['profile'] == nome_cognome:
        if email:
            dizionario_contatto['email'] = email
        if telefono:
            dizionario_contatto['telefono'] = telefono
    return dizionario_contatto

# Esempi di utilizzo
# Creazione di un contatto
contatto = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)
print(contatto)
# Output: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 69876543}

# Aggiornamento di un contatto
contatto = update_contact(contatto, "Mario Rossi", telefono=123456789)
print(contatto)
# Output: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}







        




