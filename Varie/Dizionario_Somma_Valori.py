'''
Questa funzione prende in output un dizionario
(e.s. d = {"ciao":2,"hello":3}) e restituisce
un nuovo dizionario fatto così:
d1 = {"ciao":2/5,"hello":3/5} dove 5 è la somma dei valori
di d , ossia 2 + 3 = 5
'''
def rewrite_dict(d: dict[str,int]) -> dict [str , float]:

    print(f"Il dizionario di input è {d}")

    somma = sum(list(d.values()))

    print(f"La somma è {somma}")

# Oppure con un ciclo for:
#   somma = 0
#   for key in d :
#      somma += d[key]

    out = {}
    for key in d:
        out[key]= d[key]/somma
    return out

d = {"ciao":2,"hello":3}

output = rewrite_dict(d)

print(f"Il nuovo output è {output}")







