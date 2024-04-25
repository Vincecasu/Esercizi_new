def subtract_all(x: list[float],y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = 5
    # restituisce [-4,-3,-2,-1,0]
    res: list[float] = []
    for i in x:
        diff: float = i - y
        res.append(diff)
    return res
#Oppure:
#   for i in range(len(x)):
#       x[i] -= y
#   return x
# Anche se in questo modo vado a modificare la lista di partenza.
# Quindi dopo diventa:
#my_list: list[float] = [1,2,3,4,5]
#y: float = 10
#subtract_all(my_list,y)
#print(f"Il risultato della sottrazione è {mylist}")
#Questo si chiama un SideEffect in Python
my_list: list[float] = [1,2,3,4,5]
y: float = 10
result = subtract_all(my_list,y)
print(f"Il risultato della sottrazione è {result}")