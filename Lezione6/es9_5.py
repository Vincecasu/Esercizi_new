'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class 
from Exercise 9-3. Write a method called increment_login_attempts() that 
increments the value of login_attempts by 1. Write another method called 
reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() 
several times. Print the value of login_attempts to make sure it was 
incremented properly, and then call reset_login_attempts(). Print login_attempts
again to make sure it was reset to 0.
'''
class User:

    def __init__(self,nome,cognome,residenza) -> None:
        self.nome = nome
        self.cognome = cognome
        self.residenza = residenza
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

vincenzo = User("Vincenzo","Casuccio","Roma")
vincenzo.increment_login_attempts()
vincenzo.increment_login_attempts()
vincenzo.increment_login_attempts()

print(vincenzo.login_attempts)

vincenzo.reset_login_attempts()
print(vincenzo.login_attempts)
        

    
