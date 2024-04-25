'''
Scrivi una funzione somma_elementi(x: list[int], y: list[int]) -> list[int] che 
calcola la somma elemento per elemento di due liste x e y e 
restituisce il risultato.
'''
x = [1,1,1]
y = [1,1,1]
z = []
for i in range(len(x),len(y)):
    z = z.append(x[i]+y[i])
print(z)
