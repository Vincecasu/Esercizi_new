# Vincenzo Casuccio
# 18/04/2024

print("Hello World!")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name : str = "Mario"

message : str = (f"Ciao {name}, ti va di imparare un pò di python insieme?")

print(message)

#2-4. Name Cases: Use a variable to represent a person’s name, and then 
#print that person’s name in lowercase, uppercase, and title case.

name_lower: str = name.lower()

name_upper: str = name.upper()

name_title: str = name.title()

print(f"{name_lower}, {name_upper}, {name_title}")

