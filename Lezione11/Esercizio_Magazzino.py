class Prodotto:
    def __init__(self, nome, quantità):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def __init__(self):
        self.prodotti = []
    
    def aggiungi_prodotto(self, prodotto):
        for p in self.prodotti:
            if p.nome == prodotto.nome:
                p.quantità += prodotto.quantità
                return
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None
    
    def verifica_disponibilità(self, nome):
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            return f"Il prodotto '{nome}' è disponibile con quantità: {prodotto.quantità}."
        else:
            return f"Il prodotto '{nome}' non è disponibile in magazzino."

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione dei prodotti
    prodotto1 = Prodotto("Latte", 30)
    prodotto2 = Prodotto("Pane", 20)
    prodotto3 = Prodotto("Uova", 50)

    # Creazione del magazzino
    magazzino = Magazzino()

    # Aggiunta dei prodotti al magazzino
    magazzino.aggiungi_prodotto(prodotto1)
    magazzino.aggiungi_prodotto(prodotto2)
    magazzino.aggiungi_prodotto(prodotto3)

    # Test case
    print(magazzino.verifica_disponibilità("Latte"))  # Il prodotto 'Latte' è disponibile con quantità: 30.
    print(magazzino.verifica_disponibilità("Pane"))  # Il prodotto 'Pane' è disponibile con quantità: 20.
    print(magazzino.verifica_disponibilità("Uova"))  # Il prodotto 'Uova' è disponibile con quantità: 50.
    print(magazzino.verifica_disponibilità("Burro"))  # Il prodotto 'Burro' non è disponibile in magazzino.

    # Aggiunta di un prodotto esistente
    magazzino.aggiungi_prodotto(Prodotto("Latte", 20))
    print(magazzino.verifica_disponibilità("Latte"))  # Il prodotto 'Latte' è disponibile con quantità: 50.
