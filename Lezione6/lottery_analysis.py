'''
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
Write a loop that keeps pulling numbers until your ticket wins. Print a message 
reporting how many times the loop had to run to give you a winning ticket.
'''
import random

# Lista contenente 10 numeri e 5 lettere
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Funzione per selezionare 4 elementi casuali dalla lista usando random.sample
def select_lottery_numbers(pool):
    return random.sample(pool, 4)

# Il mio biglietto della lotteria
my_ticket = [1, 'A', 3, 'B']

# Contatore dei tentativi
attempts = 0
winning_ticket = []

# Loop per trovare il biglietto vincente
while winning_ticket != my_ticket:
    winning_ticket = select_lottery_numbers(lottery_pool)
    attempts += 1

# Stampa il risultato
print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to get a winning ticket.")
