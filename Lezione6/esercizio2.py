'''
9-3. Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints 
a summary of the user’s information. Make another method called greet_user() 
that prints a personalized greeting to the user. Create several instances 
representing different users, and call both methods for each user.
'''
class User:

    def __init__(self,nome,cognome,residenza) -> None:
        self.nome = nome
        self.cognome = cognome
        self.residenza = residenza
    
    def greet_user(self):
        print(f"Ciao {self.nome} {self.cognome} felice di vederti.")

