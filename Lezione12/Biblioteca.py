class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.prestato = False  # Stato del prestito, inizialmente disponibile
    
    def __str__(self):
        stato = "Disponibile" if not self.prestato else "Prestato"
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Stato: {stato}"

class Biblioteca:
    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.prestato:
                    libro.prestato = True
                    return f"Il libro '{titolo}' è stato prestato."
                else:
                    return f"Errore: Il libro '{titolo}' è già prestato."
        return f"Errore: Il libro '{titolo}' non è disponibile nel catalogo."

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.prestato:
                    libro.prestato = False
                    return f"Il libro '{titolo}' è stato restituito."
                else:
                    return f"Errore: Il libro '{titolo}' non era prestato."
        return f"Errore: Il libro '{titolo}' non è disponibile nel catalogo."

    def mostra_libri_disponibili(self):
        disponibili = [libro.titolo for libro in self.catalogo if not libro.prestato]
        if disponibili:
            return "Libri disponibili: " + ", ".join(disponibili)
        else:
            return "Nessun libro disponibile per il prestito."

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione della biblioteca
    biblioteca = Biblioteca()

    # Aggiunta dei libri al catalogo
    libro1 = Libro("Il Nome della Rosa", "Umberto Eco")
    libro2 = Libro("1984", "George Orwell")
    libro3 = Libro("Brave New World", "Aldous Huxley")

    print(biblioteca.aggiungi_libro(libro1))  # Libro 'Il Nome della Rosa' aggiunto al catalogo.
    print(biblioteca.aggiungi_libro(libro2))  # Libro '1984' aggiunto al catalogo.
    print(biblioteca.aggiungi_libro(libro3))  # Libro 'Brave New World' aggiunto al catalogo.

    # Prestito di un libro
    print(biblioteca.presta_libro("1984"))  # Il libro '1984' è stato prestato.
    print(biblioteca.presta_libro("1984"))  # Errore: Il libro '1984' è già prestato.

    # Visualizzazione dei libri disponibili
    print(biblioteca.mostra_libri_disponibili())  # Libri disponibili: Il Nome della Rosa, Brave New World

    # Restituzione di un libro
    print(biblioteca.restituisci_libro("1984"))  # Il libro '1984' è stato restituito.
    print(biblioteca.restituisci_libro("1984"))  # Errore: Il libro '1984' non era prestato.

    # Visualizzazione aggiornata dei libri disponibili
    print(biblioteca.mostra_libri_disponibili())  # Libri disponibili: Il Nome della Rosa, Brave New World, 1984
