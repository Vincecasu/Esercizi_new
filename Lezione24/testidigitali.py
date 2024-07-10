'''
Si definisca una classe Documento che contenga una variabile di tipo stringa 
chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() 
per impostare il testo. Scrivere un metodo isInText() che restituisce True se un 
documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento e che includa le 
variabili per il mittente, il destinatario e il titolo del messaggio.
Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo 
del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di 
testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
Da: alice@example.com, A: bob@example.com
Titolo: Incontro
Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo 
getText() in un file di testo e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento e includa 
una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del 
file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
I contenuti testuali del file dovrebbero essere letti da questo file di testo 
al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo 
tramite un metodo leggiTestoDaFile().
Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e 
il testo, come di seguito:
 
Percorso: nomePercorso/document.txt
Contenuto: Questo e' il contenuto del file.

### Test tramite codice driver:
Creazione degli oggetti:

    Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo 
    del messaggio.
    File: Viene creato un oggetto File specificando il percorso di un file esistente.

Prova dei metodi:

    Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email 
    utilizzando il metodo getText().
    Stampa del testo del file: Viene stampato il contenuto del file utilizzando il 
    metodo getText().

Scrittura del contenuto dell'email su un file:

    Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file 
    chiamato email1.txt utilizzando il metodo writeToFile().

Verifica della presenza di parole chiave:

    Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' 
    è presente nel testo dell'email. Il risultato atteso è True.
    File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è 
    presente nel testo del file. Il risultato atteso è False.

### Test con UnitTest

Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, 
Email e File.
 
I test devono includere:

    Verifica dei metodi getText() e setText() nella classe Documento.
    Verifica del metodo isInText() nella classe Documento.
    Verifica del metodo getText() nella classe Email.
    Verifica del metodo writeToFile() nella classe Email.
    Verifica del metodo isInText() nella classe Email.
    Verifica del metodo getText() nella classe File.
    Verifica del metodo isInText() nella classe File.
'''

class Documento:
    def __init__(self, testo: str):
        self.testo = testo

    def setText(self,testo):
        self.testo = testo

    def getText(self):
        return self.testo
    
    def isInText(self, keyword : str):
        if keyword in self.testo:
            return True
        else:
            return False
        
class Email(Documento):
    def __init__(self, testo : str, mittente: str, destinatario: str , titolo: str):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo
    
    def setMittente(self, mittente: str):
        self.mittente = mittente

    def setDestinatario(self, destinatario: str):
        self.destinatario = destinatario
   
    def setTitolo(self, titolo: str):
        self.titolo = titolo
    
    def getMittente(self, mittente: str):
        return self.mittente
   
    def getDestinatario(self, destinatario: str):
        return self.destinatario
   
    
    def getTitolo(self, titolo: str):
        return self.titolo
    
    def getText(self):
        return f"Da: {self.mittente}, A: {self.destinatario} + \n Titolo: {self.titolo} + \n Messaggio: {self.testo}"
    
    def writeToFile(self, directory):
        with open(directory, "w") as file:
            testo = self.getText()
            file.write(testo)

class File(Documento):
    def __init__(self, testo: str, nome_Percorso: str):
        super().__init__(testo)
        self.nome_Percorso = nome_Percorso
    
    def leggiTestodaFile(self):
        with open(self.nome_Percorso, 'r') as file:
            self.testo = file.read()
    
    def getText(self):
        return f"Percorso: {self.nome_Percorso} + \n Contenuto: {self.testo}"
    

    
     

 
    

