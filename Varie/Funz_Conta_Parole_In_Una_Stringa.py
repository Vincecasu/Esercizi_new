s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

#Adesso faccio un'altra funzione che conta il numero di occorrenza delle parole
# di una stringa.
#ad esempio se la stringa è "ciao come stai. tutto bene . ciao io sto bene"
#ad esempio {"ciao": 2,"come":1,"stai":1,"tutto":2,"bene":2,"io":1,"sto":1}

def word_count(s: str) -> dict [str,int]:
    s: str = s.replace(".","").replace(",","").replace(";","").replace("!","").replace("?","")
    words : list[str] = s.split()

#Ora devo vedere quante volte le parole compaiono in words.
    
    d:dict [str,int] = dict()
    for word in words :
        if word not in d :
            d[word] = 1
        else:
            d[word] = d[word]+1

    return d

# Adesso filtra le parole che compaiono > 1 volta.

    d_filtered: dict [str,int] = dict()
    for key in d:
        if d[key] > 1:
          d_filtered[key] = d[key]
        return d_filtered

                    #Oppure posso fare :

    d_filtered: dict [str,int] = dict()
    for k , v in d.items:
        if val > 1 :
            d_filtered[key] = val
        return d_filtered