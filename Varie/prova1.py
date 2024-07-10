import random

cases = [10, 50, 100, 250, 500, 1000]
for n in cases:
        
    list_input: list[int] = [random.randint(0, 100000) for _ in range(n)]

print(list_input)