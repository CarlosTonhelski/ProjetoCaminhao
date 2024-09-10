from Carro import Carro
from Moto import Moto
from Caminhao import Caminhao
from Veiculo import Veiculo
#BD em memória
listaVeiculos = [
    Carro("Hyundai", "Hb20", "ABC", 2023, 4),
    Moto("Yamaha", "Lander", "DEF", 2008, 250),
    Caminhao("Peterbilt", "389", "ZXC", 1940, 13000 ),
]

def cadastrar():
    print("Qual o tipo de veículo: (1) Carro - (2) Moto - (3) Caminhao")
    tipo = input()
    print("Digite a marca:")
    marca = input()
    print("Digite o modelo:")
    modelo = input()
    print("Digite o placa:")
    placa = input()
    print("Digite o Ano:")
    ano = input()
    if tipo == "1":
        nPortas = input("Digite o número de portas: ")
        veiculoAdd = Carro(marca, modelo ,placa, ano, nPortas)
    elif tipo == "2":
        cilindradas = input("Digite as cilindradas: ")
        veiculoAdd = Moto(marca, modelo, placa, ano, cilindradas)
        listaVeiculos.append(veiculoAdd)
    elif tipo == "3":
        carga = input("Digite a carga:" )
        veiculoAdd = Caminhao(marca, modelo, placa, ano, carga)
        listaVeiculos.append(veiculoAdd)


def listar():
    if len(listaVeiculos) == 0:
        print ("Não existem veículos cadastrados")
    else:
        i = 1
        for veiculo in listaVeiculos:
            print(f"Veículo: {i}")
            print(f" - {veiculo}")
            i += 1

def excluir():
    listar()
    print("Digite a placa que deseja excluir")
    placa = input()
    encontrou = False
    for veiculo in listaVeiculos:
        if veiculo.get_placa() == placa:
            listaVeiculos.remove(veiculo)
            encontrou = True
            break
    if encontrou:
        print("Veículo excluído")
    else:
        print("Veículo não encontrado")


while True:
    print("Escolha uma das opções:")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Excluir Veículo")
    print("0 - SAIR")
    opcao = input()
    try:
        opcao = int(opcao)
    except:
        print("Opção Inválida")
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")