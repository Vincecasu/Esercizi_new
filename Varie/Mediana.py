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
   l = sorted(l)

   mid = len(l) // 2
   mediana: float = 0
   if len(l) % 2 == 1 : # dispari
    print("La mia lista ha lunghezza dispari")
    mediana = l[mid]
   else : # pari
    print("La mia lia ha lunghezza pari")
    mediana = (l[mid] + l[mid-1]) / 2

    return mediana
l = [9,0,-1,25,2,4,6]
mediana = median(l)
print(f"La mediana della lista {l} è {mediana}")
