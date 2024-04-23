

def rewrite_dict(d: dict[str,int]) -> dict [str , int] :

    somma = sum (list(d.values()))

    out = {}
    for key in d:
        out[key]= d[key]/sum
    return out


def substract (a: float,b: float):
    

    c = a-b 
    return c

diff = substract(5, 3)
print(f"La differenza è {diff}")

#Questa funzione prende in input una lista di valori reali e restituisce 
#la mediana di questa lista.
'''
Ad esempio :
l = [2,9,0,-1,25,2,4,3] (lunghezza pari)
l ordinata: -1 0 2 2 3 4 9 25
mediana = (2 + 3)/ 2 = 2.5

l = [2,9,0,-1,25,2,4] (lunghezza dispari)
l ordinata: -1 0 2 2 4 9 25
mediana = 2 perchè 2 è l'elemento centrale

'''


def median (l: list[float]) -> float:

    l.sort()
    if len(l) % 2 == 1:
        mid = len(l) // 2
        mediana = l[mid]
    else:
        mid = len(l) // 2 
        mid1 = mid-1
        mediana = (l[mid]+ l[mid1]) / 2
        return mediana
    
s_input: str = input("Inserisci dei numeri delimitati da spazi: ")
l: list[str] = s_input.split()
l1: list[float]= []
for elem in l:
    l1.append(float(elem))
print(l)
print(l1)
mediana = median(l1)
print(f"La mediana dela lista è: {mediana}")


#Funzione differenza comulativa
