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
