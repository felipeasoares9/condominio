class Apartamento:
    def __init__(self):
        self.id = 0
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None
        
    def cadastrar(self):
        self.numero = int(input("Numero do apartamento: "))
        self.torre = str(input("Torre: ")).upper()
        
    def imprimir(self):
        print("----------------------------------------------")
        print(f"Numero do apartamento: {self.numero}\nTorre: {self.torre}")
        print("----------------------------------------------")