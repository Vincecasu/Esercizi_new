def subtract_all(x: list[float],y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = 5
    # restituisce [-4,-3,-2,-1,0]
    res: list[float] = []
    for i in x:
        c = i-y
        res.append(c)
    return res


mylist: list[float]=[1,2,3,4,5]
y : float = 10
result = subtract_all(mylist,y)
print(f"Il risultato dopo la sottrazione è{result}")

def subtract_list(x: list[float],y: float) -> list[float]:
    new_list = []
    for l in range(len(x)) :
        z = x[l]-y[l]
        new_list.append(z)
    return(new_list)

mylist: list[float]=[1,2,3,4,5]
y : list[float] = [2,3,4,5,6]
result = subtract_list(mylist,y)

print(f"La differenza secondo la posizione è {result}")

s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

def counter (s: str) -> list[int]:

# Questa funzione prende una stringa in input e
# restituisce una lista costruita nel modo seguente:
# 1) Il primo elemento della lista contiene il numero dei caratteri della stringa.
# 2) il secondo elemento della lista contiene il numero di parole nella stringa
# 3) il terzo elemento della lista contiene il numero di parole distinte nella stringa
# 49 il quarto elemento della lista contiene il numero di frasi nella stringa
  s = s.lower

  lista: list[int] = []

#Quanti caratteri ha la stringa:
  lista.append(len(s))

  #Quante parole
  lista[1] = len(s.split())

  #Quante parole distinte ha la stringa







