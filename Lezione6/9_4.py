'''
9-4. Number Served: Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change 
this value and print it again. Add a method called set_number_served() that 
lets you set the number of customers that have been served. Call this method 
with a new number and print the value again. Add a method called 
increment_number_served() that lets you increment the number of customers 
who’ve been served. Call this method with any number you like that could 
represent how many customers were served in, say, a day of business. 
'''
class Restaurant:
      def __init__(self,name,cuisine) -> None:
            self.restaurant_name = name
            self.cuisine_type = cuisine
            self.number_served = 0
            self.__private = 19

      def get_p(self): print(self.__private)

      def set_p(self): self.__private+=1

      def set_p2(self, param): 
            if type(param) == str: print("Non valido")
            else: self.__private+=param

      def set_number_served(self,new_number_served):
            self.number_served = new_number_served 

      def increment_number_served(self,additional_customers):
            self.number_served += additional_customers

restaurant = Restaurant("Da Gigio","Romana")
print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Custumers served after change: {restaurant.number_served}")



restaurant.set_number_served(25)
print("Number of customers served after using set_number_served:", restaurant.number_served)

# Use increment_number_served method to increment the number served
restaurant.increment_number_served(40)
print("Number of customers served after incrementing:", restaurant.number_served)
    
restaurant.set_p2(3)
restaurant.get_p()