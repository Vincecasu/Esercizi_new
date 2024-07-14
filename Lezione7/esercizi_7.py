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
