def diff_fulcro(l: list[float], index: int) -> float:
    # l = [1,2,3,4,5,6] 
    # devo restituire 3-1-2-4-5-6 = -qulacosa
    if -len(l) <=  index < len (l):  #index < len(l) and index >= -len(l)  
        fulcro = l[index]            #con pop -> fulcro = l.pop(index)
        for i in range(len(l)):         #    for i in range(len(l)):
                                        #        fulcro -= l(i)
            if i != index:      
    #Oppure if i == index
            # continue      
                fulcro_-= l[i]
        return fulcro
    else:
        return 42

