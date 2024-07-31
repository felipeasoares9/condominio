from no import No

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        
    def imprimir(self):
        if self.tamanho == 0:
            print("Fila Vazia")
        else:
            texto = "Fila de espera: "
            aux = self.primeiro
            while(aux):
                texto = texto + str(aux.dado) + " - "
                aux = aux.proximo
            ("------------------------------------------------")
            print(texto)
            ("------------------------------------------------")
            
    def adicionar(self, valor):
        no = No(valor)
        if self.ultimo is None:
            self.ultimo = no
        else:
            self.ultimo.proximo = no
            self.ultimo = no
        if self.primeiro is None:
            self.primeiro = no
        self.tamanho = self.tamanho + 1
        self.imprimir()
        
    def remover(self):
        if self.tamanho > 0:
            valor = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
            self.tamanho = self.tamanho - 1
            print("Valor " + str(valor) + " removido com sucesso!")
            self.imprimir()
        if self.tamanho == 0:
            self.primeiro = None
            self.ultimo = None