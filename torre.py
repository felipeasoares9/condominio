class Torre:
    def __init__(self):
        self.id = 0
        self.nome = None
        self.endereco = None
        
    def cadastrar(self):
        self.nome = str(input("Nome da torre: ")).upper()
        self.endereco = str(input("Endereço: "))
        
    def imprimir(self):
        print("----------------------------------------------")
        print(f"Torre: {self.nome}\nEndereço: {self.endereco}")
        print("----------------------------------------------")