# importa bibliotecas
import time  # usada para criar pausas e simular processamento
import os  # usada para limpar a tela

# matriz que armazena os produtos
matriz = [
    [1, "Coca-Cola", 3.75, 0],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

# armazena o estoque de troco em uma variável do tipo dicionário
estoqueTroco = {
    100: 5, 50: 5, 20: 5, 10: 5, 5: 5, 2: 5, 1: 10,  # cédulas
    0.50: 10, 0.25: 10, 0.10: 20, 0.05: 20, 0.01: 50  # moedas
}

# função que inicia o ID
def iniciar():
    os.system("cls")
    # dá as opções ao usuário do que fazer
    print("0 - Sair")
    print("1 - Comprar bebidas")
    print("2 - Acessar modo Admin")
    opcao = input("\nEscolha uma opção: ")
    
    # lógica de continuidade de acordo com a resposta do usuário
    if opcao == "1":
        os.system("cls")
        escolherBebida()
    elif opcao == "2":
        os.system("cls")
        modoAdmin()
    elif opcao == "0":
        os.system("cls")
        print("Sistema encerrado.")
        exit()
    else:
        os.system("cls")
        print("Opção inválida! Tente novamente em 3 segundos...")
        time.sleep(3)
        iniciar()

# função que faz a lógica para mostrar as bebidas existentes na matriz e pegar o ID delas
def escolherBebida():
    os.system("cls")
    print("======== Escolha sua bebida ========\n")
    for linha in matriz:
        print(f"{linha[0]} - {linha[1]} (R$ {linha[2]:.2f}) - Estoque: {linha[3]}")
    print("\n====================================\n")
    bebidaEscolhida = int(input("Digite o código da bebida ou 0 para voltar: "))
    os.system("cls")
    
    # permite ao usuário voltar à tela inicial
    if bebidaEscolhida == 0:
        iniciar()
    # garante que o usuário não escolha uma bebida que não existe
    elif bebidaEscolhida > len(matriz) or bebidaEscolhida < 0:
        print("Código inválido! Tente novamente em 5 segundos...")
        time.sleep(5)
        escolherBebida()
    # direciona o usuário a dar continuidade na compra 
    else:
        verificarEstoque(bebidaEscolhida)

# função que verifica o estoque
def verificarEstoque(idBebida):
    # seleciona a bebida - 1 para não dar erro
    bebida = matriz[idBebida - 1]
    
    # se a bebida não tiver estoque, volta à tela inicial
    if bebida[3] < 1:
        print(f"Desculpe, {bebida[1]} está fora de estoque. Escolha outra.")
        time.sleep(3)
        escolherBebida()
    # se tiver estoque, dá continuidade
    else:
        print(f"O valor da {bebida[1]} é R$ {bebida[2]:.2f}. Deseja continuar?")
        print("1 - Sim\n2 - Não")
        resposta = input("\nEscolha: ")
        
        # garante que o usuário escolheu certo a bebida
        if resposta == "1":
            os.system("cls")
            verificarPagamento(idBebida)
        # senão, volta à tela inicial
        else:
            escolherBebida()

# função que verifica o pagamento
def verificarPagamento(idBebida):
    # pega o preço da bebida - 1 na matriz
    bebida = matriz[idBebida - 1]
    valorBebida = bebida[2]
    print(f"Insira o valor para pagamento de R$ {valorBebida:.2f}:")
    valorPagamento = float(input())
    
    # se o valor do pagamento for menor do que o esperado, volta à tela inicial das bebidas
    if valorPagamento < valorBebida:
        os.system("cls")
        print("Valor insuficiente. Tente novamente em 5 segundos...")
        time.sleep( 5)
        escolherBebida()
    # se não, faz a lógica do troco
    else:
        # mostra quanto troco será devolvido
        troco = round(valorPagamento - valorBebida, 2)
        os.system("cls")
        print(f"Troco a ser devolvido é de: {troco}")
        time.sleep(2)
        # chama a função que mostrará como esse troco será devolvido
        if calcularTroco(troco):
            os.system("cls")
            print("Descarregando bebida...")
            bebida[3] -= 1  # reduz o estoque da bebida
            time.sleep(2)
            escolherBebida()
        # se não houver troco suficiente, a compra é cancelada
        else:
            os.system("cls")
            print("Desculpe, mas não temos troco suficiente. Compra cancelada.")
            time.sleep(2)
            escolherBebida()

# função que tenta fornecer o troco e atualiza o estoque do troco
def calcularTroco(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]  # vetor que armazena os tipos de notas/cédulas
    moedas = [0.50, 0.25, 0.10, 0.05, 0.01]  # vetor que armazena os tipos de moedas
    trocoUsado = []  # armazena as cédulas e moedas usadas no troco para exibir depois
    
    # usa for para armazenar o troco usado e append para armazená-las no vetor de acordo com a quantidade de moedas e cédulas usadas juntas
    for unidade in cedulas + moedas:
        while valor >= unidade and estoqueTroco[unidade] > 0:  # faz com que, enquanto ainda haja troco a ser devolvido, ele percorra cada unidade de moeda e cédula disponível que ainda esteja disponível no estoque
            valor = round(valor - unidade, 2)  # arredonda o valor e o atualiza a cada loop
            estoqueTroco[unidade] -= 1  # diminui o estoque do troco de acordo com a cédula ou a moeda usada
            trocoUsado.append(unidade)  # acrescenta de fato a moeda ou cédula usada no vetor
            
    if valor > 0:  # se não foi possível fornecer o troco exato
        restaurarEstoque(trocoUsado)  # chama a função para restaurar o troco até então reunido 
        return False  # não mostra o troco, pois não foi possível realizá-lo
    mostrarTroco(trocoUsado)  # mostra o troco se foi possível usá-lo
    return True

# função que restaura o estoque se o troco não puder ser fornecido
def restaurarEstoque(trocoUsado):
    for unidade in trocoUsado:  # para cada cédula ou moeda usada no troco até então utilizado...
        estoqueTroco[unidade] += 1  # restaura o estoque da cédula ou moeda usada

# função que exibe as cédulas e moedas usadas no troco
def mostrarTroco(trocoUsado):
    print("\nO troco será devolvido na forma de:\n")
    print("----------------------")
    trocoContado = {}  # armazena a quantidade de cada unidade de troco que foi utilizada como em um dicionário
    for unidade in trocoUsado:  # para cada unidade que foi usada no troco...
        if unidade in trocoContado:  # se a unidade já estiver na variável trocoContado, adiciona mais 1
            trocoContado[unidade] += 1 
        else:  # se a unidade não estiver no troco contado, a adiciona
            trocoContado[unidade] = 1
            
    # para cada unidade e quantidade no trocoContado
    for unidade, quantidade in trocoContado.items():
        # verifica se é moeda ou cédula se o valor for maior que 1
        if unidade >= 1:
            tipo = "nota"
        else:
            tipo = "moeda"
        print(f"{quantidade} {tipo}(s) de R$ {unidade:.2f}")
    print("----------------------")
    time.sleep(10)

# função do modo admin que adiciona novas bebidas, as edita ou as exclui
def modoAdmin():
    os.system("cls")
    print("0 - Voltar")
    print("1 - Cadastrar nova bebida")
    print(" 2 - Editar bebida")
    print("3 - Excluir bebida")
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "0":
        iniciar()
    elif opcao == "1":
        cadastrarBebida()
    elif opcao == "2":
        editarBebida()
    elif opcao == "3":
        excluirBebida()
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
        modoAdmin()

# função extra para adicionar novas bebidas à matriz
def cadastrarBebida():
    os.system("cls")
    nome = input("Nome da bebida: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    id = len(matriz) + 1
    matriz.append([id, nome, preco, estoque])
    os.system("cls")
    print(f"Bebida {nome} cadastrada com sucesso!")
    time.sleep(3)
    modoAdmin()

# função extra para editar as bebidas na matriz
def editarBebida():
    os.system("cls")
    for linha in matriz:
        print(f"{linha[0]} - {linha[1]} (R$ {linha[2]}) - Estoque: {linha[3]}")
    
    # edita a bebida de acordo com o ID
    id = int(input("\nDigite o código da bebida para editar: "))
    
    # se o usuário digitar um ID que não existe, volta à tela do admin
    if id <= 0 or id > len(matriz):
        os.system("cls")
        print("Código inválido! Retornando ao menu admin...")
        time.sleep(3)
        modoAdmin()
    # se não, dá continuidade à edição
    else:
        os.system("cls")
        bebida = matriz[id - 1]
        nome = input(f"Novo nome ({bebida[1]}): ") 
        preco = input(f"Novo preço ({bebida[2]}): ")
        estoque = input(f"Novo estoque ({bebida[3]}): ")
        matriz[id - 1] = [id, nome, float(preco), int(estoque)]
        os.system("cls")
        print("Bebida editada com sucesso!")
        time.sleep(3)
        modoAdmin()

# função extra para excluir bebidas de acordo com o ID
def excluirBebida():
    os.system("cls")
    for linha in matriz:
        print(f"{linha[0]} - {linha[1]} (R$ {linha[2]}) - Estoque: {linha[3]}")
    
    id = int(input("\nDigite o código da bebida para excluir: "))
    
    # se não existir o ID, volta à tela do admin
    if id <= 0 or id > len(matriz):
        os.system("cls")
        print("Código inválido! Retornando ao menu admin...")
        time.sleep(3)
        modoAdmin()
    # se existir, dá continuidade à exclusão
    else:
        bebida = matriz.pop(id - 1)
        os.system("cls")
        print(f"Bebida {bebida[1]} excluída com sucesso!")
        time.sleep(3)
        atualizarID()
        modoAdmin()

# função para atualizar os IDs depois da exclusão e ficar tudo arrumadinho
def atualizarID():
    for i, bebida in enumerate(matriz):
        bebida[0] = i + 1

# dá início ao ID
iniciar()