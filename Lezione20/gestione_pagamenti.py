class Pagamento:

    def set(self, importo: float):
        self.__importo: float = importo


    def getImporto(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.__importo}:.2f")

    
