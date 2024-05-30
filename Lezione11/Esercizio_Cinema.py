class Film:
    def __init__(self, titolo, durata):
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero, film, posti_totali):
        self.numero = numero
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0
    
    def prenota_posti(self, num_posti):
        if self.posti_disponibili() >= num_posti:
            self.posti_prenotati += num_posti
            return f"Prenotazione confermata per {num_posti} posti per il film '{self.film.titolo}' nella sala {self.numero}."
        else:
            return f"Errore: Non ci sono abbastanza posti disponibili per il film '{self.film.titolo}' nella sala {self.numero}."
    
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati

class Cinema:
    def __init__(self):
        self.sale = []
    
    def aggiungi_sala(self, sala):
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Errore: Film '{titolo_film}' non trovato in nessuna sala."

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione dei film
    film1 = Film("Inception", 148)
    film2 = Film("The Matrix", 136)

    # Creazione delle sale
    sala1 = Sala(1, film1, 100)
    sala2 = Sala(2, film2, 150)

    # Creazione del cinema
    cinema = Cinema()

    # Aggiunta delle sale al cinema
    cinema.aggiungi_sala(sala1)
    cinema.aggiungi_sala(sala2)

    # Prenotazioni
    print(cinema.prenota_film("Inception", 50))  # Prenotazione confermata
    print(cinema.prenota_film("Inception", 60))  # Errore: Non ci sono abbastanza posti disponibili
    print(cinema.prenota_film("The Matrix", 100))  # Prenotazione confermata
    print(cinema.prenota_film("Avatar", 10))  # Errore: Film non trovato
