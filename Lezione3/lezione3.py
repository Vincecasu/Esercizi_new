'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
such as I really love pizza!

'''
pizzas: list = ["Marinara","Margherita","Funghi"]
frasi: list  = ["Mi piace molto la ","Adoro la ","Preferisco a tutte la "]

for p in pizzas:
    print(f"{p}")

for frase , p in zip( frasi , pizzas):
    print(frase , p)

for f in range(len(frasi)):
    print(f"{frasi[f]}{pizzas[f]}")

print(f"I really love pizza!")

''''
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence,
such as Any of these animals would make a great pet!
'''
animali: list = ["dog","cat","monkey"]
for i in animali :
    print(i)
for c in animali:
    print(f"A {c} would make a great pet.")
print(f"All of those animals are lovely!")

'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
'''
for num in range(1,21):
    print(num)

'''
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

'''
numeri:list = []
for n in range(1,1000001):
    numeri.append(n)
print(numeri)

'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make 
sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python 
can add a million numbers.
'''
minimo: int = min(numeri)
print(minimo)
massimo: int = max(numeri)
print(massimo)
somma: int = sum(numeri)
print(somma)
