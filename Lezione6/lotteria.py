'''
Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list and print a message saying 
that any ticket matching these 4 numbers or letters wins a prize.
'''
import random

# List containing 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Function to select 4 random items from the list
def select_lottery_numbers(pool):
    return random.sample(pool, 4)


# Select 4 random items from the lottery pool
winning_ticket = select_lottery_numbers(lottery_pool)

# Print the winning message
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")
