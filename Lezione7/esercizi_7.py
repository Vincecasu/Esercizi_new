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






