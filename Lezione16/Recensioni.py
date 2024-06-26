'''
Esercizio: Sistema di Recensioni
Completion requirements
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, 
un film o un libro) e una classe derivata Film che rappresenti specificamente 
un film. 
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere 
valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, 
con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 
5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle 
recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato 
sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si 
avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto 
medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se 
il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto 
specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni 
del media, stampando il titolo, il voto medio, il giudizio e le percentuali di 
ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di 
tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e 
richiami il metodo 
recensione().

'''

class Media :
    def __init__(self,titolo,recensioni) -> None:
         self.titolo = titolo
         self.recensioni = []

    
    def set_title(self,titolo):
         self.titolo = titolo
    
    def get_title(self):
         return self.titolo
    
    def aggiungiValutazione(self,voto):
         for voto in range(1,6):
              self.recensioni.append(voto)
    
    def get_media(self):
         if len(self.recensioni) == 0 :
              return 0
         else:
              return sum(self.recensioni)/len(self.recensioni)
    
    def get_rate(self,voto):
        media = self.get_media()
        if media == 0 :
            return "Nessuna valutazione"
        if media < 1.5 :
             return "Terribile"
        if media < 2.5 :
             return "Brutto"
        if media < 3.5 :
             return "Normale"
        if media < 4.5 :
             return "Bello"
        if media <= 5 :
             return "Grandioso"
        
    def ratePercentage(self, voto):
         for voto in self.recensioni :
              return (self.recensioni.count(voto)/len(self.recensioni)) * 100
         
    def recensione(self):
         print(f"Titolo: {self.set_title}")
         print(f"Voto medio: {self.get_media}")
         print(f"Giudizio: {self.get_rate}")
         print(f"Percentuali voto: {self.ratePercentage}")
         
         

class Film(Media) :
        def __init__(self,titolo):
             super().__init__()
             self.set_title(titolo)


film_1 = Film("The Shawshank Redemption")

lista_voti_film_1 = [3,4,5,4,3,5,4,2,1,1]

for voto in lista_voti_film_1:
     film_1.aggiungiValutazione(voto)

print(film_1.recensione())



'''
class Media:
    def __init__(self, title=""):
        self.title = title
        self.reviews = []
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            print(f"Valutazione {voto} non valida. Deve essere tra 1 e 5.")
    
    def getMedia(self):
        if not self.reviews:
            return 0
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self):
        media = self.getMedia()
        if media < 1.5:
            return "Terribile"
        elif media < 2.5:
            return "Brutto"
        elif media < 3.5:
            return "Normale"
        elif media < 4.5:
            return "Bello"
        else:
            return "Grandioso"
    
    def ratePercentage(self, voto):
        if not self.reviews:
            return 0
        count = self.reviews.count(voto)
        return (count / len(self.reviews)) * 100
    
    def recensione(self):
        print(f"Titolo del Film: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.ratePercentage(1):.2f}%")
        print(f"Brutto: {self.ratePercentage(2):.2f}%")
        print(f"Normale: {self.ratePercentage(3):.2f}%")
        print(f"Bello: {self.ratePercentage(4):.2f}%")
        print(f"Grandioso: {self.ratePercentage(5):.2f}%")

class Film(Media):
    pass

# Creiamo due oggetti di tipo Film
film1 = Film("The Shawshank Redemption")
film2 = Film("The Godfather")

# Aggiungiamo valutazioni ai film
valutazioni_film1 = [5, 4, 4, 5, 5, 4, 5, 3, 4, 5]
valutazioni_film2 = [5, 5, 5, 4, 4, 5, 5, 5, 4, 4]

for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Richiamiamo il metodo recensione per ogni film
print("Recensioni per il primo film:")
film1.recensione()
print("\nRecensioni per il secondo film:")
film2.recensione()

'''

            
                      

    





        