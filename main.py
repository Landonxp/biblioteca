livros = []

def escolhas(): #Feito
    while True:
        print(f"\n{5 * '='} BIBLIOTECA {5 * '='}")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Emprestar livro")
        print("5 - Devolver livro")
        print("6 - Remover livro")
        print("7 - Estatisticas")
        print("0 - Sair\n")

        escolha = int(input("Escolha: "))

        if escolha == 1:
            cadastrar_livro()
        elif escolha == 2:
            listar_livros()
        elif escolha == 3:
            buscar_livro()
        elif escolha == 4:
            emprestar_livro()
        elif escolha == 5:
            devolver_livro()
        elif escolha == 6:
            remover_livro()
        elif escolha == 7:
            mostrar_estatisticas()
        else:
            break
    
def cadastrar_livro(): #Feito
    titulo = input('\nDigite o titulo: ')
    autor = input('Digite o autor: ')
    ano = int(input('Digite o ano: '))
    livros.append({'titulo' : titulo, 'autor' : autor, 'ano' : ano, 'emprestado' : False})

def listar_livros(): #Feito
    numero = 0

    for i in livros:
        numero += 1
        if i['emprestado'] == False:
            status = "Disponivel"
        else:
            status = "Indisponivel"


        print(f"\n{numero}. {i['titulo']}")
        print(f"Autor: {i['autor']}")
        print(f"Ano: {i['ano']}")
        print(f"Status: {status}")
        print(f"\n{25 * '-'}")

def buscar_livro(): #Feito
    livro_buscado = input('\nDigite o livro que deseja buscar: ').lower()
    for i in livros:
        if livro_buscado in i['titulo'].lower():
            print(f"{i['titulo']}")

def emprestar_livro(): #Feito
    livro = input('\nQual livro deseja pegar emprestado? ')

    for i in livros:
        if livro == i['titulo'] and i['emprestado'] == False:
            i['emprestado'] = True
            print('Livro emprestado com sucesso!')
        elif livro == i['titulo'] and i['emprestado'] == True:
            print('Esse livro esta indisponivel!')

def devolver_livro(): #Feito
    livro = input('\nQual livro deseja devolver? ')
    
    for i in livros:
        if livro == i['titulo'] and i['emprestado'] == True:
            i['emprestado'] = False
            print('Livro devolvido com sucesso!')
        elif livro == i['titulo'] and i['emprestado'] == False:
            print('Você não pegou esse livro emprestado!')

def remover_livro(): #Feito
    livro_remover = input('\nDigite o livro que você quer remover: ').lower()

    for i in livros:
        if livro_remover in i['titulo'].lower():
            print(i['titulo'])
            decisao = input('Esse livro que você quer remover? (S/N): ').upper()
            
            if decisao == "S":
                livros.remove(i)
                print(f'Livro: {i["titulo"]} removido com sucesso!')
                break
            else:
                continue

def mostrar_estatisticas(): #Feito
    total = 0
    emprestados = 0
    disponiveis = 0
    
    mais_antigo = livros[0]['ano']
    

    for l in livros:
        atual = l['ano']
        if atual < mais_antigo:
            mais_antigo = atual
    

    for i in livros:
        total += 1
        if i['emprestado'] == False:
            disponiveis += 1
        elif i ['emprestado'] == True:
            emprestados += 1

    print(20 * '-')
    print(f'\nTotal de livros: {total}')
    print(f'Disponiveis: {disponiveis}')
    print(f'Emprestados: {emprestados}')
    print(f'Livro mais antigo: \n{l['titulo']} ({mais_antigo})')

escolhas()
