import json
import time
import sys


def abrirArquivo():
    with open('desafios.json', 'r', encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvarArquivo(dados):
    with open('desafios.json', 'w', encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
        print('Arquivo salvo com sucesso!')
        time.sleep(1)


def adicionarDesafio():
    desafios = abrirArquivo()
    id_novo_desafio = str(max([int(k) for k in desafios.keys()]) + 1)

    # Adiciona um novo desafio
    print('Adicionar Desafio')
    print('-----------------')
    print('Digite os dados do desafio:')
    print('-----------------')
    print('Desafios:')

    nome = input('Nome do desafio: ')
    descricao = input('Descrição do desafio: ')
    data = input('Digite o dia do desafio: ')
    concluido = False

    desafio = {
        'dia': int(data),
        'title': nome,
        'description': descricao,
        'concluido': concluido
    }
    desafios[id_novo_desafio] = desafio
    salvarArquivo(desafios)
    print("Desafio adicionado com sucesso.")
    time.sleep(1)
    menu()


def listarDesafios():
    desafios = abrirArquivo()
    print('Listar Desafios')
    print('-----------------')
    print('Desafios:')
    for id, desafio in desafios.items():
        print(f'ID: {id}')
        print(f'Título: {desafio["title"]}')
        print(f'Descrição: {desafio["description"]}')
        print(f'Dia: {desafio["dia"]}')
        print(f'Concluído: {desafio["concluido"]}')
        print('-----------------')
    time.sleep(2)
    menu()


def removerDesafio():
    desafios = abrirArquivo()
    print("remover desafio")
    print('-----------------')
    print('Selecione o desafio que desaja remover:')

    for id, desafio in desafios.items():
        print(f"Id: {id}, Titulo: {desafio['title']}.")

    desafio_excluir = input("Digite o id da pergunta que deseja remover: ")

    while desafio_excluir not in desafios:
        print("Desafio não encontrado.")
        desafio_excluir = input("Digite o id da pergunta que deseja remover: ")

    del desafios[desafio_excluir]
    salvarArquivo(desafios)
    print("Desafio excluido com sucesso.")
    time.sleep(1)
    menu()


def concluirDesafio():
    desafios = abrirArquivo()
    print("Concluir desafio")
    print('-----------------')
    print('Selecione o desafio que deseja concluir:')

    for id, desafio in desafios.items():
        print(f"ID: {id}, Titulo: {desafio['title']}")
        print(type(id))
        print('')
    desafio_concluir = input("Digite o ID do Desafio que deseja Concluir: ")

    while desafio_concluir not in desafios:
        print("Desafio não encontrado.")
        desafio_concluir = input(
            "Digite o ID do Desafio que deseja Concluir: ")

    desafios[desafio_concluir]['concluido'] = True
    salvarArquivo(desafios)
    print("Desafio concluido com sucesso.")
    time.sleep(1)
    menu()

def desfazerDesafio():
    desafios = abrirArquivo()
    print("Desfazer desafio")
    print('-----------------')
    print('Selecione o desafio que deseja Desfazer:')

    for id, desafio in desafios.items():
        print(f"ID: {id}, Titulo: {desafio['title']}")
        print(type(id))
        print('')
    desafio_concluir = input("Digite o ID do Desafio que deseja Desfazer: ")

    while desafio_concluir not in desafios:
        print("Desafio não encontrado.")
        desafio_concluir = input("Digite o ID do Desafio que deseja Desfazer: ")

    desafios[desafio_concluir]['concluido'] = False
    salvarArquivo(desafios)
    print("Desafio Desfeito com sucesso.")
    time.sleep(1)
    menu()

# Menu


def menu():
    print('''
    [1] - Adicionar Desafio
    [2] - Listar Desafios
    [3] - Remover Desafio
    [4] - Concluir Desafio
    [5] - Desfazer Desafio   
    [0] - Sair      
    ''')
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            adicionarDesafio()
        case 2:
            listarDesafios()
        case 3:
            removerDesafio()
        case 4:
            concluirDesafio()
        case 5:
            desfazerDesafio()
        case 0:
            sys.exit()


menu()
