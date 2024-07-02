'''
GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo 
float che memorizza l'importo del pagamento e si definiscano appropriati 
metodi get() e set(). L'importo non è un parametro da passare in input alla classe 
Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive 
l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". 
Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da 
Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo 
dettagliPagamento() per indicare che il pagamento è in contanti. 
Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote 
da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o 
in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 
0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e 
che definisce l'importo. Questa classe deve contenere gli attributi per il nome 
del titolare della carta, la data di scadenza, e il numero della carta di credito. 
Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le 
informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due 
di tipo PagamentoCartaDiCredito con valori differenti e si invochi 
dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
'''
class Pagamento:
    def __init__(self):
        self.__importo = 0.0

    def set_importo(self, importo):
        self.__importo = float(importo)

    def get_importo(self):
        return self.__importo

    def dettagliPagamento(self):
        return f"Importo del pagamento: €{self.__importo:.2f}"


class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.set_importo(importo)

    def dettagliPagamento(self):
        return f"Pagamento in contanti di: €{self.get_importo():.2f}"

    def inPezziDa(self):
        importo = self.get_importo()
        pezzi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        result = []
        for pezzo in pezzi:
            count = int(importo // pezzo)
            if count > 0:
                if pezzo >= 5:
                    result.append(f"{count} banconota{'e' if count > 1 else ''} da {pezzo} euro")
                else:
                    result.append(f"{count} moneta{'e' if count > 1 else ''} da {pezzo:.2f} euro")
                importo -= count * pezzo
                importo = round(importo, 2)  # avoid floating-point arithmetic issues
        return f"{self.get_importo():.2f} euro da pagare in contanti con:\n" + "\n".join(result)


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nome_titolare, data_scadenza, numero_carta):
        super().__init__()
        self.set_importo(importo)
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagliPagamento(self):
        return (f"Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito\n"
                f"Nome sulla carta: {self.nome_titolare}\n"
                f"Data di scadenza: {self.data_scadenza}\n"
                f"Numero della carta: {self.numero_carta}")


# Creazione degli oggetti di tipo PagamentoContanti
pagamento_contanti1 = PagamentoContanti(150.00)
pagamento_contanti2 = PagamentoContanti(95.25)

# Creazione degli oggetti di tipo PagamentoCartaDiCredito
pagamento_carta1 = PagamentoCartaDiCredito(200.00, "Mario Rossi", "12/24", "1234567890123456")
pagamento_carta2 = PagamentoCartaDiCredito(500.00, "Luigi Bianchi", "01/25", "6543210987654321")

# Invocazione del metodo dettagliPagamento() per ogni oggetto
print(pagamento_contanti1.dettagliPagamento())
print(pagamento_contanti1.inPezziDa())
print()

print(pagamento_contanti2.dettagliPagamento())
print(pagamento_contanti2.inPezziDa())
print()

print(pagamento_carta1.dettagliPagamento())
print()

print(pagamento_carta2.dettagliPagamento())

    
