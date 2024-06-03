'''
9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 or 
Exercise 9-5. Add an attribute, privileges, that stores a list of strings 
like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method.
'''
import es9_5
'''
9-8. Privileges: Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in ù
Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges
instance as an attribute in the Admin class. Create a new instance of Admin 
and use your method to show its privileges.
'''

class Privileges():
    def __init__(self) -> None:
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"]
        
    def show_privileges(self):
        print(f"I privilegi sono: {','.join(self.privileges)}")

class Admin(es9_5.User,Privileges):

    def __init__(self,nome,cognome) -> None:
        super().__init__(nome,cognome)
        Privileges.__init__(self)
        
vincenzo = Admin("Vincenzo","Casuccio")
vincenzo.show_privileges()

