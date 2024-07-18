def diff_cum(l: list[float]) -> float:
    # l = [1,2,3,4,5,6]
    # deve restituire -1-2-3-4-5-6 = - qualcosa
    diff: float = l[0]
    for i in range(1,len(l)):
        diff -= l[i]
    return diff
    # Oppure si può fare cosi :
    #for i in l[1:]: -> [1:] perchè dobbiamo considerare
    # a partire dal secondo elemento della lista,
    # perchè sennò farebbe 1(primo elemento - se stesso, 
    # che è una condizione che abbiamo escluso).
    #    diff -= i
    #return diff
l = [1,2,3,4,5,6]
result = diff_cum(l)
print(result)
