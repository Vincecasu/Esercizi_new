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
for n in range(1,1001):
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

'''
4-6. Odd Numbers: Use the third argument of the range() function 
to make a list of the odd numbers from 1 to 20. Use a for loop to print 
each number.

'''
num_dispari: list = []
for dispari in range(1,21,2):
    num_dispari.append(dispari)
print(num_dispari)

'''
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
Use a for loop to print the numbers in your list.
'''
l1: list = []
for threes in range(3,31,3):
    l1.append(threes)
print(l1)

#Oppure :

multi_tre = list(range(3, 31, 3))

for multi in multi_tre:
    print(multi)

'''
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. Make a list of the
first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube.
'''
cubi: list = []
for cubo in range(1,11):
    cubi.append(cubo**3)
print(cubi)

'''
4-9. Cube Comprehension: Use a list comprehension to generate a list of 
the first 10 cubes.
'''
cubes = [x ** 3 for x in range(1, 11)]

print(cubes)

'''
4-10. Slices: Using one of the programs you wrote in this chapter, 
add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. 
Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. 
Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. 
Then use a slice to print the last three items in the list.
'''

