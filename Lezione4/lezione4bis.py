def subtract_all(x: list[float],y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = 5
    # restituisce [-4,-3,-2,-1,0]
    res: list[float] = []
    for i in x:
        diff: float = i - y
        res.append(diff)
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

'''
Esercizio su stringa
'''
s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

def counter (s: str) -> list[int]:

# Questa funzione prende una stringa in input e
# restituisce una lista costruita nel modo seguente:
# 1) Il primo elemento della lista contiene il numero dei caratteri della stringa.
# 2) il secondo elemento della lista contiene il numero di parole nella stringa.
# 3) il terzo elemento della lista contiene il numero di parole distinte nella stringa.
# 4) il quarto elemento della lista contiene il numero di frasi nella stringa.
  
  s = s.lower
  lista: list[int] = []

#Quanti caratteri ha la stringa:
  lista.append(len(s))

  #Quante parole ha la stringa:
  lista.append(len(s.split())) # s = "ciao bello."-> s.split()->["ciao","bello."]

  #Quante parole distinte ha la stringa:
  parole = s.split()
  parole_distinte = set(parole)
  lista.append(len(parole_distinte))
  
  #quante frasi ha la stinga:
  lista.append(len(s.split("."))-1)
  #oppure:
  #lista.append(s.count("."))
  #s = "ciao bello.come stai."
  #s.split(".") -> ["ciao bello","come stai",""]

  return lista




#Adesso faccio un'altra funzione che conta il numero di occorrenza delle parole
#ad esempio se la stringa è "ciao come stai. tutto bene . ciao io sto bene"
#ad esempio {"ciao": 2,"come":1,"stai":1,"tutto":2,"bene":2,"io":1,"sto":1}

def word_count(s: str) -> dict [str,int]:
    s: str = s.replace(".","").replace(",","").replace(";","").replace("!","")
    words : list[str] = s.split()
    
    d:dict [str,int] = dict()
    for word in words :
        if word not in d :
            d[word] = 1
        else:
            d[word] = d[word]+1

# Adesso filtra le parole che compaiono > 1 volta
    d_filtered: dict [str,int] = dict()
    for key , val in d.items():
        if val > 1 :
            d_filtered[key] = val
    return d_filtered

def is_palindrome(s: str) -> bool:

#Restituisce True se s è palindroma; altrimenti restituisce False
#Ad esempio "Amo Roma" è una stringa palindroma
# "Ciao come stai?" non è una stringa palindroma

  s: str = s.lower().replace(" ","")

  i: int = 0
  while i < len(s) // 2:
      j = len(s) - (i + 1)
      if s[i] != s[j]:
          return False
      i += 1
  return True

#Oppure:
def is_palindrome2(s: str) -> bool:
    s1: str = ""
    for i in range(len(s)-1,0,-1):
        s1 += s[i]

    for i in range(len(s)):
        if s[i] != s1[i]:
          return False
    return True

      

 






