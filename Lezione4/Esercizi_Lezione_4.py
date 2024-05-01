'''
8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
'''
def display_message():
    message: str = "In questo capitolo sto imparando ad usare le fuzioni."
    print(message)

display_message()

'''
8-2. Favorite Book: Write a function called favorite_book() that accepts 
one parameter, title. The function should print a message, such as 
"One of my favorite books is Alice in Wonderland". Call the function, 
making sure to include a book title as an argument in the function call.
'''
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")

'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and 
the text of a message that should be printed on the shirt. The function 
should print a sentence summarizing the size of the shirt and the message 
printed on it. Call the function once using positional arguments to make 
a shirt. Call the function a second time using keyword arguments
'''
def make_shirt(size,text):
    print(f"Sulla t-shirt taglia {size} c'è scritto '{text}'.")

make_shirt("L","I love you")
make_shirt(size="M",text="Woopwoopydo")

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and 
a medium shirt with the default message, and a shirt of any size with a 
different message.
'''
def make_shirt(size="L",text="I love Python"):
    print(f"Sulla t-shirt taglia {size} c'è scritto '{text}'.")
make_shirt()
make_shirt(size="M")
make_shirt(size="S",text="~Coca-Cola")

'''
8-5. Cities: Write a function called describe_city() that accepts the name 
of a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country a default 
value. Call your function for three different cities, at least one of which is 
not in the default country.
'''
def describe_city(city,country="Sconosciuto"):

    print(f"{city} si trova in {country}")

describe_city("Los Angeles","America")
describe_city("Tokyo","Giappone")
describe_city("Parigi")

'''
8-6. City Names: Write a function called city_country() that takes 
in the name of a city and its country. The function should return a 
string formatted like this: "Santiago, Chile". Call your function with at least
three city-country pairs, and print the values that are returned.
'''
def city_country(city, country):
    """Ritorna una stringa formattata tipo: 'city, country'."""
    return f"{city}, {country}"

# Call the function with city-country pairs and print the returned values
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))

'''
8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and 
an album title, and it should return a dictionary containing these two pieces 
of information. Use the function to make three dictionaries representing 
different albums. Print each return value to show that the  dictionaries 
are storing the album information correctly. Use None to add an optional 
parameter to make_album() that allows you to store the number of songs on 
an album. If the calling line includes a value for the number of songs, 
add that value to the album’s dictionary. Make at least one new function call
 that includes the number of songs on an album.
'''
def make_album(artist_name, album_title, num_songs=None):
    """Builds a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if num_songs:
        album['num_songs'] = num_songs
    return album

# Create dictionaries representing different albums
album1 = make_album("Artist 1", "Album 1")
album2 = make_album("Artist 2", "Album 2", num_songs=12)
album3 = make_album("Artist 3", "Album 3")

# Print each return value to show that the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

'''
8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input 
and print the dictionary that’s created. Be sure to include a quit value 
in the while loop.
'''

def make_album(artist_name, album_title):
    """Builds a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album

while True:
    artist = input("Enter the artist's name (or 'q' to quit): ")
    if artist.lower() == 'q':
        break
    
    title = input("Enter the album title (or 'q' to quit): ")
    if title.lower() == 'q':
        break

    album_info = make_album(artist, title)
    print(album_info)

'''
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text 
message.
'''
def show_messages():
    messaggi: list[str] = ["Ciao, come stai?","Fin qui tutto bene?",\
                           "L'importante è arrivare come si deve."]
    print(f"{messaggi[0]}")
    print(f"{messaggi[1]}")
    print(f"{messaggi[2]}")
show_messages()

#Oppure :

def show_messages(messages):
    """Prints each text message in the list."""
    for message in messages:
        print(message)

# Define a list of text messages
text_messages = [
    "Hello!",
    "How are you?",
    "I'm fine, thank you.",
    "Have a great day!"
]

# Call the show_messages() function with the list of messages
show_messages(text_messages)

'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and 
moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages 
were moved correctly.
'''
def show_messages(messages):
    """Prints each text message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Prints each text message, moves it to sent_messages, and prints sent_messages."""
    while messages:
        message = messages.pop(0)
        print("Sending message:", message)
        sent_messages.append(message)

# Define a list of text messages
text_messages = [
    "Hello!",
    "How are you?",
    "I'm fine, thank you.",
    "Have a great day!"
]

# Create an empty list to store sent messages
sent_messages = []

# Call the send_messages() function to send and move messages
send_messages(text_messages, sent_messages)

# Print both lists to make sure the messages were moved correctly
print("\nOriginal messages:")
show_messages(text_messages)
print("\nSent messages:")
show_messages(sent_messages)

'''
Archived Messages: Start with your work from Exercise 8-10. Call the function 
send_messages() with a copy of the list of messages. After calling the function, 
print both of your lists to show that the original list has retained 
its messages.
'''
def show_messages(messages):
    """Prints each text message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Prints each text message, moves it to sent_messages, and prints sent_messages."""
    while messages:
        message = messages.pop(0)
        print("Sending message:", message)
        sent_messages.append(message)

# Define a list of text messages
text_messages = [
    "Hello!",
    "How are you?",
    "I'm fine, thank you.",
    "Have a great day!"
]

# Create an empty list to store sent messages
sent_messages = []

# Call the send_messages() function with a copy of the text_messages list
send_messages(text_messages[:], sent_messages)

# Print both lists to show that the original list has retained its messages
print("\nOriginal messages:")
show_messages(text_messages)
print("\nSent messages:")
show_messages(sent_messages)

'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants
 on a sandwich. The function should have one parameter that collects 
 as many items as the function call provides, and it should print a summary 
 of the sandwich that’s being ordered. Call the function three times, 
 using a different number of arguments each time.
'''
def make_sandwich(*items):
    print("Fare un panino con i seguenti ingredienti:")
    for item in items:
        print("-" + item)

make_sandwich("prosciutto","formaggio","pomodoro")
print()
make_sandwich("porchetta")
print()
make_sandwich("pomodoro","mozzarella","basilico")

'''
8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that 
describe you. All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown,
weight 67".
'''
def build_profile(nome, cognome, età, peso, altezza):
    """Builds a profile of a person."""
    profilo = f"{nome} {cognome}, età {età}, peso {peso}, altezza {altezza}"
    return profilo

# Call the build_profile() function with your information
mio_profilo = build_profile("Vincenzo", "Casuccio", 46, 95, "1,75")

# Print the profile
print(mio_profilo)

#Oppure avrei potuto costruire un dizionario:

def build_profile(first_name, last_name, age, hair_color, weight):
    """Builds a profile of a person."""
    profile = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "hair_color": hair_color,
        "weight": weight
    }
    return profile

# Call the build_profile() function with your information
my_profile = build_profile("John", "Doe", 30, "brown", 75)

# Print the profile
print(my_profile)

'''
8-14. Cars: Write a function that stores information about a car in a dictionary.
 The function should always receive a manufacturer and a model name. 
 It should then accept an arbitrary number of keyword arguments. 
 Call the function with the required information and two other name-value pairs,
such as a color or an optional feature. Your function should work for a call 
like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information 
was stored correctly. 
'''
def make_car(marca,modello,colore,versione,optional):
    info_car: dict[str,str] = {
        "marca": marca,
        "modello": modello,
        "colore": colore,
        "verione": versione,
        "optional": optional 
        }
    return info_car

my_car = make_car("Audi","Q8","Grigio Scuro","Rs","Full Optional")
print(my_car)
        
