class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name, movies):
        if director_name not in self.catalog:
            self.catalog[director_name] = []
        if isinstance(movies, list):
            self.catalog[director_name].extend(movies)
        else:
            self.catalog[director_name].append(movies)
        return f"Film aggiunti per il regista {director_name}."

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                    return f"Il film '{movie_name}' è stato rimosso e il regista {director_name} non ha più film nel catalogo."
                return f"Il film '{movie_name}' è stato rimosso dal catalogo di {director_name}."
            else:
                return f"Errore: Il film '{movie_name}' non è presente nel catalogo di {director_name}."
        else:
            return f"Errore: Il regista {director_name} non è presente nel catalogo."

    def list_directors(self):
        if self.catalog:
            return "Registi presenti nel catalogo: " + ", ".join(self.catalog.keys())
        else:
            return "Nessun regista presente nel catalogo."

    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return f"Film di {director_name}: " + ", ".join(self.catalog[director_name])
        else:
            return f"Errore: Il regista {director_name} non è presente nel catalogo."

    def search_movies_by_title(self, title):
        results = {}
        for director, movies in self.catalog.items():
            matching_movies = [movie for movie in movies if title.lower() in movie.lower()]
            if matching_movies:
                results[director] = matching_movies
        
        if results:
            output = "Film trovati:\n"
            for director, movies in results.items():
                output += f"{director}: " + ", ".join(movies) + "\n"
            return output
        else:
            return f"Nessun film trovato con il titolo contenente '{title}'."

# Esempio di utilizzo
if __name__ == "__main__":
    catalog = MovieCatalog()

    # Aggiunta dei film al catalogo
    print(catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk"]))
    print(catalog.add_movie("Steven Spielberg", ["Jurassic Park", "Schindler's List", "E.T."]))
    print(catalog.add_movie("Christopher Nolan", "The Dark Knight"))

    # Rimozione di un film dal catalogo
    print(catalog.remove_movie("Christopher Nolan", "Inception"))
    print(catalog.remove_movie("Christopher Nolan", "Memento"))  # Film non presente

    # Elenco di tutti i registi
    print(catalog.list_directors())

    # Ottenere i film di un regista specifico
    print(catalog.get_movies_by_director("Christopher Nolan"))
    print(catalog.get_movies_by_director("Martin Scorsese"))  # Regista non presente

    # Ricerca di film per titolo
    print(catalog.search_movies_by_title("Park"))
    print(catalog.search_movies_by_title("Knight"))  # Titolo parziale
    print(catalog.search_movies_by_title("Matrix"))  # Film non presente
