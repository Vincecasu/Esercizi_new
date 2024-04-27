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

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said,
#“A person who never made a mistake never tried anything new.”

famous_person: str = "Albert Einstein"
quotation_mark: str = "A person who never made a mistake never tried anything new."

print(f'{famous_person} once said :"{quotation_mark}"')

#2-8. File Extensions: Python has a removesuffix() method that works exactly 
#like removeprefix(). Assign the value 'python_notes.txt' to a variable 
#called filename. Then use the removesuffix() method to display the filename 
#without the file extension, like some file browsers do.

filename: str = "python_notes.txt"
file_new:str = filename.removesuffix(".txt")
print(file_new)

#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names: list = ["Aldo","Giovanni","Giacomo"]
for n in names:
 print(n)

#3-2. Greetings: Start with the list you used in Exercise 3-1, 
#but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be 
#personalized with the person’s name.

for s in names:
 print(f"Ciao {s},come stai?")

#3-3. Your Own List: Think of your favorite mode of transportation, such as 
#a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as 
#“I would like to own a Honda motorcycle.”

moto: list = ["Ducati","Bmw","Aprilia"]
statements: list = ["Adoro girare con la mia","Mi piacerebbe provare una",\
                    "Non ho mai guidato un'"]
for i in range(len(statements)):
 print(f"{statements[i]} {moto[i]}")

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, 
#who would you invite? Make a list that includes at least three people you’d 
#like to invite to dinner. Then use your list to print a message to each person, 
#inviting them to dinner.

guest_list: list = ["Pippo","Pluto","Topolino"]
message: str = ", ti va di venire a cena?"
for m in range(len(guest_list)):
 print(f"Ciao {guest_list[m]}{message}")

#3-5. Changing Guest List: You just heard that one of your guests can’t make 
#the dinner, so you need to send out a new set of invitations. You’ll have to 
#think of someone else to invite.
#Start with your program from Exercise 3-4. Add a print() call at the end of 
#your program, stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with 
#the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still 
#in your list.
print(f"Purtroppo {guest_list[-1]} non sarà dei nostri..")
guest_list.pop(-1)
print(f"{guest_list}")
guest_list.append("Paperino")
print(f"{guest_list}")
for invito in range(len(guest_list)):
 print(f"Ciao caro {guest_list[invito]}{message}")

#3-6. More Guests: You just found a bigger dinner table, so now more space is 
#available. Think of three more guests to invite to dinner.
#Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
#end of your program, informing people that you found a bigger table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.
print(f"Allora guys, abbiamo a disposizione un tavolo piu grande,\
saremo in sette.")
guest_list.insert(0,"Aldo")
print(guest_list)
guest_list.insert(3,"Giovanni")
guest_list.append("Giacomo")
print(guest_list)
messaggio: str = "ti aspetto per cena mi raccomando"
for invite in range(len(guest_list)):
 print(f"{guest_list[invite]} {messaggio}.")

#3-7. Shrinking Guest List: You just found out that your new dinner table 
#won’t arrive in time for the dinner, and now you have space for only two guests.
#Start with your program from Exercise 3-6. Add a new line that prints a message 
#saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names 
#remain in your list. Each time you pop a name from your list, print a message 
#to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know 
#they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list.
#Print your list to make sure you actually have an empty list at the end 
#of your program.
print(f"Spiacente ragazzi ma il tavolo nuovo non arriverà, per cui \
saremo solo in 3.")
print(f"Mi spiace {guest_list[-1]}, sarà per la prossima volta. Saluti.")
guest_list.pop(5)
print(f"Mi spiace {guest_list[-1]}, sarà per la prossima volta. Saluti.")
guest_list.pop(4)
print(f"Mi spiace {guest_list[-1]}, sarà per la prossima volta. Saluti.")
guest_list.pop(3)
print(f"Mi spiace {guest_list[-1]}, sarà per la prossima volta. Saluti.")
guest_list.pop(2)
print(f"Mi spiace {guest_list[-1]}, sarà per la prossima volta. Saluti.")
print(guest_list)
new_mess: str = "ci si vede questa sera!Ciao."
for last in range(len(guest_list)):
 print(f"Ok {guest_list[last]} {new_mess}")
del guest_list [:]
print(guest_list) 







 






