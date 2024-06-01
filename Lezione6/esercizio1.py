'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of
 information, and a method called open_restaurant() that prints a message 
 indicating that the restaurant is open. Make an instance called restaurant 
 from your class. Print the two attributes individually, and then call both
methods.
'''
class Restaurant:
    def __init__(self,name,cuisine, valori_recensini=5) -> None:
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.recensione = valori_recensini

    def describe_restaurant(self):
        print(f"Name: {self.restaurant_name}\nCuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"The Restaurant is open")

restaurant = Restaurant("Al Poetto","Pesce",9)
print(restaurant.cuisine_type,restaurant.restaurant_name)
restaurant.describe_restaurant()
print(restaurant.recensione)
restaurant.open_restaurant()

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() 
for each instance.
'''
ristorante_1 = Restaurant("La Pergola","Internazionale")
ristorante_2 = Restaurant("Da Ciro","Carne")
ristorante_3 = Restaurant("Da Antonio","Vegan")
ristorante_1.describe_restaurant()
ristorante_2.describe_restaurant()
ristorante_3.describe_restaurant()