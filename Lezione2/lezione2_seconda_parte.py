#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 
#Print each piece of information stored in your dictionary.

persona_1: dict[str, int] = {
    "Nome": "Mario",
    "Cognome":"Rossi",
    "Età":30,
    "Città":"Milano"
    }

print(persona_1["Nome"])
print(persona_1["Cognome"])
print(persona_1["Età"])
print(persona_1["Città"])

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value 
#in your dictionary. Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers: dict[str,int] = {
    "Anna":1,
    "Gianna":2,
    "Maria":3,
    "Laura":4,
    "Paola":5
}
print(f"Il numero preferito di Anna è {favorite_numbers['Anna']}")
print(f"Il numero preferito di Gianna è {favorite_numbers['Gianna']}")
print(f"Il numero preferito di Maria è {favorite_numbers['Maria']}")
print(f"Il numero preferito di Laura è {favorite_numbers['Laura']}")
print(f"Il numero preferito di Paola è {favorite_numbers['Paola']}")

#oppure con un for:

for person, number in favorite_numbers.items():
    print(f"Il numero preferito di {person} è {number}")

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters.
#Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on 
#a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.

# Dizionario per memorizzare parole di programmazione e i loro significati
glossario = {
    "variabile": "Una posizione di memorizzazione denominata in memoria che può contenere dati.",
    "funzione": "Una sequenza di istruzioni denominata che esegue un compito.",
    "lista": "Una collezione ordinata di elementi, che possono essere di tipi diversi.",
    "ciclo": "Una struttura di controllo che ripete un blocco di codice fino a quando una determinata condizione non viene soddisfatta.",
    "dizionario": "Una collezione di coppie chiave-valore, dove ogni chiave mappa a un valore specifico."
}

# Stampa ogni parola e il suo significato
for parola, significato in glossario.items():
    print(f"{parola.capitalize()}:")
    print(significato)
    print()  # Inserisce una riga vuota tra ogni coppia parola-significato

#6-7. People: Start with the program you wrote for Exercise 6-1. 
#Make two new dictionaries representing different people, 
#and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, 
#print everything you know about each person.

persona_1: dict[str, int] = {
    "Nome": "Mario",
    "Cognome":"Rossi",
    "Età":30,
    "Città":"Milano"
    }
persona_2: dict[str,int] = {
    "Nome": "Luca",
    "Cognome":"Bianchi",
    "Età":25,
    "Città":"Roma"
    
}
persona_3: dict[str,int] = {
    "Nome": "Dario",
    "Cognome":"Verdi",
    "Età":45,
    "Città":"Firenze"
}
people: list[dict] = [persona_1,persona_2,persona_3]
for persona in people:
    print(f'Nome: {persona["Nome"]}')
    print(f'Cognome: {persona["Cognome"]}')
    print(f'Età: {persona["Età"]}')
    print(f'Città: {persona["Città"]}')
    print()

# Lista di liste contenenti le informazioni su ogni persona
people = [
    ["John", "Doe", 30, "New York"],
    ["Alice", "Smith", 25, "Los Angeles"],
    ["Bob", "Johnson", 35, "Chicago"]
]

# Stampare le informazioni su ciascuna persona
for person in people:
    print("First Name:", person[0])
    print("Last Name:", person[1])
    print("Age:", person[2])
    print("City:", person[3])
    print()  # Inserisce una riga vuota tra le informazioni di ogni persona

#6-8. Pets: Make several dictionaries, where each dictionary represents 
#a different pet. In each dictionary, include the kind of animal and 
#the owner’s name. Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know 
#about each pet.

# Creo dei dizionari che rappresentano diversi animali domestici
pet1 = {"tipo": "Cane", "Proprietario": "Alfonso"}
pet2 = {"tipo": "Gatto", "Proprietario": "Roberto"}
pet3 = {"tipo": "Pappagallo", "Proprietario": "Carlo"}
pet4 = {"tipo": "Scimmia", "Proprietario": "Andrea"}

# Memorizza questi dizionari in una lista chiamata pets
pets = [pet1,pet2,pet3,pet4]

# Itera attraverso la lista di animali e 
# stampa tutte le informazioni conosciute su ciascun animale
for animale in pets:
    print("Tipo di Animale:", animale["tipo"])
    print("Nome del Proprietario:", animale["Proprietario"])
    print()  # Inserisce una riga vuota tra le informazioni di ciascun animale












