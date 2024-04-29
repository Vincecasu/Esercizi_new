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
lista_numeri: list = []
for nums in range(1,21):
    lista_numeri.append(nums)
print(f"I primi 3 numeri della lista sono:{lista_numeri[0:3]}")
print(f"I numeri al centro della lista sono:{lista_numeri[8:11]}")
print(f"Gli ultimi numeri della lista sono:{lista_numeri[-3:]}")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
#Make a copy of the list of pizzas, and call it friend_pizzas. 
#Then, do the following:
#Add a new pizza to the original list.
#Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. 
#Print the message My favorite pizzas are:, and then use a for loop to print 
#the first list. Print the message My friend’s favorite pizzas are:, and then 
#use a for loop to print the second list. Make sure each new pizza is stored 
#in the appropriate list.

friend_pizzas: list[str] = pizzas.copy()
pizzas.append("Capricciosa")
friend_pizzas.append("Boscaiola")
print(pizzas)
print(friend_pizzas)
print(f"Le mie pizze preferite sono:")
for p in pizzas:
    print("-" , p)
print()
print(f"Le pizze preferite dei miei amici sono:")
for p in friend_pizzas:
    print("-",p)
print()

'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
'''

# Test 1
number = 10
print("Is number == 10? I predict True.")
print(number == 10)

# Test 2
name = 'John'
print("\nIs name == 'John'? I predict True.")
print(name == 'John')

# Test 3
age = 25
print("\nIs age < 30? I predict True.")
print(age < 30)

# Test 4
animal = 'cat'
print("\nIs animal != 'dog'? I predict True.")
print(animal != 'dog')

# Test 5
fruit = 'apple'
print("\nIs fruit == 'orange'? I predict False.")
print(fruit == 'orange')

# Test 6
temperature = 20
print("\nIs temperature > 30? I predict False.")
print(temperature > 30)

# Test 7
height = 180
print("\nIs height <= 200? I predict True.")
print(height <= 200)

# Test 8
language = 'Python'
print("\nIs language.lower() == 'python'? I predict True.")
print(language.lower() == 'python')

# Test 9
day = 'Monday'
print("\nIs day == 'Friday'? I predict False.")
print(day == 'Friday')

# Test 10
weather = 'sunny'
print("\nIs weather != 'rainy'? I predict True.")
print(weather != 'rainy')

'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''
# Equality and inequality with strings
string1 = 'hello'
string2 = 'HELLO'
print("Is string1 == string2? I predict False.")
print(string1 == string2)

# Tests using the lower() method
word = 'HELLO'
print("\nIs word.lower() == 'hello'? I predict True.")
print(word.lower() == 'hello')

# Numerical tests
num1 = 10
num2 = 20
print("\nIs num1 != num2? I predict True.")
print(num1 != num2)

print("\nIs num1 < num2? I predict True.")
print(num1 < num2)

print("\nIs num1 >= num2? I predict False.")
print(num1 >= num2)

print("\nIs num1 <= num2? I predict True.")
print(num1 <= num2)

# Tests using the and keyword and the or keyword
age = 25
height = 180
print("\nIs age > 20 and height < 200? I predict True.")
print(age > 20 and height < 200)

print("\nIs age > 30 or height < 170? I predict False.")
print(age > 30 or height < 170)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

# Test whether an item is not in a list
colors = ['red', 'green', 'blue']
print("\nIs 'yellow' not in colors? I predict True.")
print('yellow' not in colors)

'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 
'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. 
If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another 
that fails. (The version that fails will have no output.)
'''

alien_color: str = "Green"
if alien_color == "Green":
    print(f"You have just earned 5 points")


'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, 
and write an if-else chain.
If the alien’s color is green, print a statement that the player just earned 
5 points for shooting the alien.
If the alien’s color isn’t green, print a statement that the player just earned
10 points.
Write one version of this program that runs the if block and another that runs
the else block.
'''
alien_color = "green"
if alien_color == "green":
    print(f"You have just earned 5 points")

alien_color = "red"

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    print("Congratulations! You just earned 10 points.")

'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an 
if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed 
for the appropriate color alien.
'''
#se l'alieno è di colore verde:

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

#Se è di colore giallo:

alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

#Se è di colore rosso:

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")




