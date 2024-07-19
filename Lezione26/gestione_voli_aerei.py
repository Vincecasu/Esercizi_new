'''
Si vuole progettare un sistema in Python per la gestione delle prenotazioni aeree. Il sistema dovrà gestire diverse tipologie di voli, tra cui voli commerciali e 
voli charter.
 
Classe astratta Volo:
Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di volo, come il codice del volo (stringa) e la capacità massima di 
posti disponibili sul volo (numero intero) che sono attributi passati come argomenti in input. Inoltre, la classe deve avere un attributo chiamato prenotazioni, 
il quale non deve essere passato come argomento del costruttore; il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili().

Classe VoloCommerciale:
Estende la classe Volo e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. Il costruttore deve inoltre gestire i seguenti 
attributi interi: posti_economica, posti_business, e posti_prima; i quali consentono di stabilire quanti posti sono stati riservati alla classe economica, 
quanti alla classe business e quanti alla prima classe su ogni volo. Il costruttore non deve ricevere in input questi argomenti, ma assegnare loro un valore 
iniziale tale che la somma di questi tre valori interi sia uguale al numero dei posti disponibili sul volo. Si può pensare di riservare il 70% dei posti alla 
classe economica, il 20% dei posti alla classe business ed i restanti posti alla prima classe. Inoltre, il costruttore deve creare tre valori interi pari a 0, 
chiamati prenotazioni_economica, prenotazioni_business, prenotazioni_prima.
 
Metodi:

    prenota_posto(posti, classe_servizio): che consente di prenotare un certo numero di posti sul volo in una determinata classe. Tale metodo, prima di riservare 
    un posto, deve controllare prima che ci siano posti disponibili sull'intero volo, poi se ci sono posti disponibili nella classe richiesta. In caso affermativo, 
    contare il numero dei posti prenotati in tale classe. Inoltre, nel caso in cui sia possibile prenotare un posto, il metodo deve stampare a schermo un messaggio 
    che notifichi all'utente di aver riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo). In caso contrario, 
    stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. Se sul volo non ci sono più posti disponibili,
    il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo. Inoltre, se la classe passata come input del metodo non 
    risulta essere una delle seguenti classi ("economica", "business", "prima"), il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente 
    che la classe richiesta non è valida. Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni 
    ricevute per ogni classe di servizio, poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con l'esatto numero delle 
    prenotaioni ricevute per ogni classe di servizio. Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di 
    servizio da azzerare all'inizio di ogni fase di prenotazione.

    posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali sul volo nel seguente modo: il dizionario deve avere
    quattro chiavi, ovvero, 'posti disponibili', 'classe economica', 'classe business', 'prima classe'. Alla chiave 'posti disponibili' associare come rispettivo 
    valore il numero di posti disponibili rimasti sul volo, alla chiave 'classe economica' associare come rispettivo valore il numero di posti che sono rimasti 
    disponibili nella classe economica, alla chiave 'classe business' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella 
    classe business, alla chiave 'prima classe' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe. Se i posti 
    disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.

Classe VoloCharter:
Estende la classe Volo e e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. Il costruttore deve inoltre gestire il costo 
del volo (numero float) per il charter. Un volo charter è un volo di cui tutti i posti disponibili vengono acquistati tutti insieme in una sola volta da un tour 
operator ad un certo prezzo.
 
Metodi:

    prenota_posto(): questo metodo verifica che se l'aereo è vuoto, ovvero i posti disponibili sono pari alla capacità massima di posti. In quel caso, è possibile
      prenotare un numero di posti pari alla capacità massima di posti supportata dal volo. Nel caso in cui la prenotazione charter andasse a buon fine, il metodo 
      deve stampare a schermo un messaggio in cui avvisa il tour operator che il volo charter (specificandone il codice del volo) è stato prenotato completamente, 
      mostrando anche il prezzo pagato. In caso contrario, il metodo deve mostrare un messaggio a schermo in cui avvisa l'utente che il volo charter è gia prenotato.

    posti_disponibili(): che ritorna il numero di posti disponibili totali sul volo.

Classe CompagniaAerea:
Questa classe deve avere un costruttore che richiede come argomento in input solo il nome della compagnia (stringa) ed il prezzo standard di un biglietto 
(numero float), e creare una lista vuota chiamata flotta. La classe CompagniaAerea deve gestire molteplici voli commerciali, attraverso i seguenti metodi:

    aggiungi_volo(volo_commericiale): il volo_commerciale deve essere aggiunto alla flotta della compagnia aerea.
    rimuovi_volo(volo_commericiale): il volo_commerciale deve essere rimosso dalla flotta della compagnia aerea.
    mostra_flotta(): tale metodo deve stampare a schermo tutti i voli che fanno parte della flotta della compagnia aerea, specificando il codice di ogni volo.
    guadagno(): questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali) il gadagno ricavato dalla vendita dei biglietti 
    aerei dei voli nella sua flotta. Su ogni aereo della flotta, il prezzo  per un posto in classe economica è pari a prezzo standard, il prezzo per un posto in 
    classe business è pari al doppio del prezzo standard, mentre il prezzo per un posto in prima classe vale tre volte il prezzo standard.

    Test con codice driver
Scrivere un codice driver che consenta di creare voli commerciali e voli charter.
Per il volo commerciale eseguire i seguenti passaggi:

    mostrare su schermo tutti i posti disponibili sul volo
    provare a prenotare un tot di posti in classe economica, esaurendo i posti disponibili in tale classe (70% dei posti totali dell'aereo).
    provare a prenotare un tot di posti in classe business, esaurendo i posti disponibili in tale classe (20% dei posti totali dell'aereo).
    provare a prenotare un tot di posti in prima classe maggiore della capacità di tale classe (70% dei posti totali dell'aereo), il codice avviserà l'utente non è 
    possibile prenotare quel tot di posti (70%).
    riprovare a prenotare un tot di posti in prima classe, esaurendo i posti disponibili in tale classe (10% dei posti totali dell'aereo).
    effettuare un altro tentativo di prenotazione. Questa volta, la prenotazione non dovrebbe andare a buon fine in quanto il volo deve risultare completo!

NOTA: Per ogni tentativo di prenotazione, stampare i posti disponibili rimasti sul volo commerciale.

Per il volo charter eseguire i seguenti passaggi:

    stampare a schermo i posti disponibili sul volo
    provare a prenotare tutto il volo charter
    provare ad effettuare un secondo tentativo di prenotazione. In questo caso, la prenotazione dovrebbe fallire, in quanto il volo charter dovrebbe essere già 
    prenotato.

Successivamente, creare un secondo volo commerciale e provare a prenotare un tot di posti in economica.
 
Infine, creare una compagnia aerea. Aggiungere i due voli commerciali alla compagnia aerea. Stampare la flotta della compagnia aerea. Calcolare il guadagno 
della compagnia aerea ricavato dalla vendita dei biglietti aerei dei voli della sua flotta.

ESEMPIO DI OUTPUT SU TERMINALE:
 

    Posti disponibili sul volo commerciale COM123:
    {'posti disponibili': 100, 'classe economica': 70, 'classe business': 20, 'prima classe': 10}
    70 posti prenotati su COM123 in classe economica.
    {'posti disponibili': 30, 'classe economica': 0, 'classe business': 20, 'prima classe': 10}
    20 posti prenotati su COM123 in classe business.
    {'posti disponibili': 10, 'classe economica': 0, 'classe business': 0, 'prima classe': 10}
    Non è possibile riservare 70 posti in prima classe. Numero posti disponibili: 10
    {'posti disponibili': 10, 'classe economica': 0, 'classe business': 0, 'prima classe': 10}
    10 posti prenotati su COM123 in classe prima.
    {'posti disponibili': 0, 'classe economica': 0, 'classe business': 0, 'prima classe': 0}
    Volo COM123 al completo!
     
    Posti disponibili sul volo charter CHA456: 200
    Volo charter CHA456 prenotato completamente per €20000.
    Il volo charter CHA456 è già prenotato.
     
    100 posti prenotati su COM456 in classe economica.
     
    Ecco la flotta della compagnia aerea ITA:
    volo commerciale COM123
    volo commerciale COM456
     
    Dalla vendita dei biglietti aerei, la compagnia aerea ITA ha guadagnato 12180.0 euro

 
NOTA: Scrivere l'output su terminale anche su un file chiamato report.txt

'''

from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice_volo, capacita_massima):
        self.codice_volo = codice_volo
        self.capacita_massima = capacita_massima
        self.prenotazioni = 0
    
    @abstractmethod
    def prenota_posto(self, posti, classe_servizio=None):
        pass
    
    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice_volo, capacita_massima):
        super().__init__(codice_volo, capacita_massima)
        self.posti_economica = int(capacita_massima * 0.7)
        self.posti_business = int(capacita_massima * 0.2)
        self.posti_prima = capacita_massima - self.posti_economica - self.posti_business
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0
    
    def prenota_posto(self, posti, classe_servizio):
        if self.prenotazioni >= self.capacita_massima:
            print(f"Volo {self.codice_volo} al completo!")
            return

        if classe_servizio not in ["economica", "business", "prima"]:
            print("Classe richiesta non valida")
            return

        if classe_servizio == "economica":
            posti_disponibili = self.posti_economica - self.prenotazioni_economica
            if posti <= posti_disponibili:
                self.prenotazioni_economica += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice_volo} in classe economica.")
            else:
                print(f"Non è possibile riservare {posti} posti in classe economica. Numero posti disponibili: {posti_disponibili}")

        elif classe_servizio == "business":
            posti_disponibili = self.posti_business - self.prenotazioni_business
            if posti <= posti_disponibili:
                self.prenotazioni_business += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice_volo} in classe business.")
            else:
                print(f"Non è possibile riservare {posti} posti in classe business. Numero posti disponibili: {posti_disponibili}")

        elif classe_servizio == "prima":
            posti_disponibili = self.posti_prima - self.prenotazioni_prima
            if posti <= posti_disponibili:
                self.prenotazioni_prima += posti
                self.prenotazioni += posti
                print(f"{posti} posti prenotati su {self.codice_volo} in classe prima.")
            else:
                print(f"Non è possibile riservare {posti} posti in prima classe. Numero posti disponibili: {posti_disponibili}")

    def posti_disponibili(self):
        posti_totali_disponibili = self.capacita_massima - self.prenotazioni
        return {
            'posti disponibili': posti_totali_disponibili,
            'classe economica': self.posti_economica - self.prenotazioni_economica,
            'classe business': self.posti_business - self.prenotazioni_business,
            'prima classe': self.posti_prima - self.prenotazioni_prima
        }

class VoloCharter(Volo):
    def __init__(self, codice_volo, capacita_massima, costo):
        super().__init__(codice_volo, capacita_massima)
        self.costo = costo
    
    def prenota_posto(self, posti=None, classe_servizio=None):
        if self.prenotazioni == 0:
            self.prenotazioni = self.capacita_massima
            print(f"Volo charter {self.codice_volo} prenotato completamente per €{self.costo}.")
        else:
            print(f"Il volo charter {self.codice_volo} è già prenotato.")
    
    def posti_disponibili(self):
        return self.capacita_massima - self.prenotazioni

class CompagniaAerea:
    def __init__(self, nome, prezzo_standard):
        self.nome = nome
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo):
        self.flotta.append(volo)

    def rimuovi_volo(self, volo):
        if volo in self.flotta:
            self.flotta.remove(volo)

    def mostra_flotta(self):
        print(f"Ecco la flotta della compagnia aerea {self.nome}:")
        for volo in self.flotta:
            print(f"{volo.__class__.__name__.lower()} {volo.codice_volo}")

    def guadagno(self):
        guadagno_totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                guadagno_totale += volo.prenotazioni_economica * self.prezzo_standard
                guadagno_totale += volo.prenotazioni_business * (self.prezzo_standard * 2)
                guadagno_totale += volo.prenotazioni_prima * (self.prezzo_standard * 3)
            elif isinstance(volo, VoloCharter):
                guadagno_totale += volo.costo
        return round(guadagno_totale, 2)

# Test driver
if __name__ == "__main__":
    import sys
    original_stdout = sys.stdout

    with open("report.txt", "w") as f:
        sys.stdout = f

        volo_commerciale = VoloCommerciale("COM123", 100)
        print(f"Posti disponibili sul volo commerciale {volo_commerciale.codice_volo}:")
        print(volo_commerciale.posti_disponibili())

        volo_commerciale.prenota_posto(70, "economica")
        print(volo_commerciale.posti_disponibili())

        volo_commerciale.prenota_posto(20, "business")
        print(volo_commerciale.posti_disponibili())

        volo_commerciale.prenota_posto(70, "prima")
        print(volo_commerciale.posti_disponibili())

        volo_commerciale.prenota_posto(10, "prima")
        print(volo_commerciale.posti_disponibili())

        volo_commerciale.prenota_posto(1, "economica")
        print(volo_commerciale.posti_disponibili())

        volo_charter = VoloCharter("CHA456", 200, 20000)
        print(f"Posti disponibili sul volo charter {volo_charter.codice_volo}: {volo_charter.posti_disponibili()}")

        volo_charter.prenota_posto()
        print(f"Posti disponibili sul volo charter {volo_charter.codice_volo}: {volo_charter.posti_disponibili()}")

        volo_charter.prenota_posto()

        volo_commerciale_2 = VoloCommerciale("COM456", 100)
        volo_commerciale_2.prenota_posto(70, "economica")

        compagnia_aerea = CompagniaAerea("ITA", 100)
        compagnia_aerea.aggiungi_volo(volo_commerciale)
        compagnia_aerea.aggiungi_volo(volo_commerciale_2)

        compagnia_aerea.mostra_flotta()

        print(f"Dalla vendita dei biglietti aerei, la compagnia aerea {compagnia_aerea.nome} ha guadagnato {compagnia_aerea.guadagno()} euro")

        sys.stdout = original_stdout

    with open("report.txt", "r") as f:
        print(f.read())




        