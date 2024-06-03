'''
Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity 
to 65 if it isn’t already. Make an electric car with a default 
battery size, call get_range() once, and then call get_range() 
a second time after upgrading the battery. You should see an 
increase in the car’s range.
'''

class Battery():
    def __init__(self) -> None:
        self.battery_size = 20
    
    def upgrade_battery(self):
        self.battery_size = 65

class Electric_car(Battery):
    def __init__(self,modello_in_input) -> None:
        super().__init__()
        self.modello = modello_in_input

    def get_range(self):
        print(self.battery_size)

tesla = Electric_car("Model 3")
tesla.get_range()
tesla.upgrade_battery()
tesla.get_range()
