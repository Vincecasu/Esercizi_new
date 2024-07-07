# test_die.py

from dice import Die

def roll_die_multiple_times(die, rolls=10):
    results = []
    for _ in range(rolls):
        result = die.roll_die()
        results.append(result)
    return results

def main():
    # Create a 6-sided die and roll it 10 times
    die_6 = Die(6)
    results_6 = roll_die_multiple_times(die_6)
    print("6-sided die rolls:", results_6)

    # Create a 10-sided die and roll it 10 times
    die_10 = Die(10)
    results_10 = roll_die_multiple_times(die_10)
    print("10-sided die rolls:", results_10)

    # Create a 20-sided die and roll it 10 times
    die_20 = Die(20)
    results_20 = roll_die_multiple_times(die_20)
    print("20-sided die rolls:", results_20)

if __name__ == "__main__":
    main()
