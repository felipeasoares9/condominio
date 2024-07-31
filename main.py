from fila import *
from listaencadeada import *
from torre import Torre
from apartamento import Apartamento


listaTorres = []
listaApartamentos = []
torre = Torre()
ap = Apartamento()
listaEnc = Lista()
fila = Fila()

while True:
    print("---------------------------------")
    print(f"1 - Cadastrar torre\n2 - Cadastrar apartamento\n3 - Liberar vaga\n4 - Imprimir apartamentos com vaga\n5 - Imprimir lista de espera por vaga\n6 - Imprimir torres cadastradas\n7 - Sair")
    print("---------------------------------")
    opcao = int(input("Escolha uma opção: "))
    if (opcao == 1):
        torre.cadastrar()
        char = len(torre.nome)
        if (torre.nome in listaTorres):
            print("Torre já cadastrada, digite um nome válido!")
            pass
        else:
            if (char == 1):
                torre.id += 1
                print(f"id: {torre.id}")
                torre.imprimir()
                listaTorres.append(torre.nome)
                print(f"Torres cadastradas: {listaTorres}")
            else:
                print("Nome de bloco deve conter apenas 1 caractere, digite um nome válido!")
                pass
    if (opcao == 2):
        ap.cadastrar()
        if (ap.numero in listaApartamentos):
            print("Apartamento já cadastrado, digite um numero válido!")
            pass
        else:
            if (ap.torre in listaTorres):
                ap.id += 1
                print(f"id: {ap.id}")
                ap.imprimir()
                listaApartamentos.append(ap.numero)
                print(f"Apartamentos cadastrados: {listaApartamentos}")
                print("------------------------------------------------")
                if (listaEnc.tamanho < 10):
                    listaEnc.add(ap.numero)
                else:
                    fila.adicionar(ap.numero)
                print("------------------------------------------------")
            else:
                print("Torre não localizada!")
                pass
    if (opcao == 3):
        listaEnc.imprimir()
        fila.imprimir()
        dado = int(input("Ap a ser removido: "))
        listaEnc.remover(dado)
        if (fila.primeiro.dado == None):
            fila.adicionar(dado)
        else:
            print(f"Primeiro elemento da fila de espera: {fila.primeiro.dado}")
            listaEnc.add(fila.primeiro.dado)
            fila.remover()
            fila.adicionar(dado)
        listaEnc.imprimir()
        fila.imprimir()
    if (opcao == 4):
        print("Apartamentos com vaga: \n")
        listaEnc.imprimir()
    if (opcao == 5):
        print("Apartamentos esperando por vaga: \n")
        fila.imprimir()
    if (opcao == 6):
        print("Torres cadastradas: ")
        if (len(listaTorres) == 0):
            print("Nenhuma torre cadastrada!")
            print(listaTorres)
        else:
            print(listaTorres)
    if (opcao == 7):
        break