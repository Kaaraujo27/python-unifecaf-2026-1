# SOBRE A APLICAÇÃO
# Desenvolva um CRUD de produtos utilizando while no menu e 
# for para listar ou buscar produtos
# Apenas serão permitidos os métodos de lista 
# append (adicionar) e pop (remover a partir de um índice)
# A aplicação deve ser executada até que o valor da opção seja 0
# Caso o valor da opção não exista, informar ao usuário


# DADOS
# O produto deve ter os dados Nome (string) e Preço (float)


# FUNCIONALIDADES
# O sistema deve ter as funções:

# 1 - listarProdutos: Retorna todos os produtos cadastrados 
#       > Dados de entrada: nenhum
#       > Leia todos os produtos
#       > Retorno: lista de produtos

# 2 - adicionarProduto: 
#       > Dados de entrada: dict Produto(nome, preco)
#       > Adiciona um produto (use append)
#       > Retorno: True ou False

# 3 - buscarProduto: 
#       > Dados de entrada: nome do produto (string)
#       > Retorne o índice do produto encontrado, ou None se não for encontrado nenhum item
#       > Retorno: o índice do produto

# 4 - atualizarProduto: Atualiza os dados de um produto
#       > Dados de entrada: índice (int), dict do novo Produto(nome, preco)
#       > Atualiza os dados de um produto já existente
#       > Retorno: True ou False

# 5 - removerProduto: Dado o índice do produto, ele deve ser removido da lista 
#       > Dados de entrada: índice (int)
#       > Remove o produto do índice
#       > Retorno: True ou False

# IMPORTANTE: Ignore os erros de execução. Em funções como atualizar e remover, apenas passe como
# parâmetros índices de produtos existentes.

produtos = [
{'nome': 'Arroz', 'preco': 30.00},
{'nome': 'Feijao', 'preco': 20.99},
{'nome': 'Macarrao', 'preco': 8.99},
{'nome': 'Farofa', 'preco': 8.99},
{'nome': 'Bolacha', 'preco': 3.50}
] #Exemplo de item {nome: Arroz, preco: 30.00}

def listarProdutos():
    if(len(produtos) == 0):
        print('Não tem produtos cadastrados')
    for p in produtos:
        print(f'{p['nome']} ... R$ {p['preco']:.2f}')
        
        
def adicionarProduto(produto):
        produtos.append(produto)
        print('Produto adicionado com sucesso') 


def buscarProduto(produtoNome):
    for i in range(len(produtos)):
        if produtos[i]['nome'] == produtoNome:
            return i
    return None 


def atualizarProduto(indice, produto):
    produtos[indice] = produto
    return True 


def removerProduto(indice):
    for i, produto in enumerate(produtos):
        if produto['nome'].lower() == nome.lower():
            return i
    return None    



opcao = None
while(opcao != '0'):
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Listar Produtos')
    print('2 - Adicionar Produto')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('0 - Sair')
    print('========================================')
    
    if(opcao == '1'): 
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '2'): 
        print()
        print('ADICIONAR DE PRODUTOS ==================')
        nome = input('Nome:')
        preco = float(input('Preço:'))
        adicionarProduto({'nome': nome, 'preco': preco})
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '3'): 
        print('BUSCAR PRODUTO =========================')
        busca = input('Busque um produto: ')
        indice = buscarProduto(busca)

        if indice != None:
            p = produtos[indice]
            print(f'Produto encontrado:{indice + 1} - {p['nome']} R${float(p['preco']):.2f}')
        else:
            print('Produto nao encontrado') 
            #código opção 3 ainda está com erro   
    
    elif(opcao == '4'): 
        print('ATUALIZAR PRODUTO ======================')
        nome = input('Nome do produto: ')
        indice = buscarProduto(nome)
        if (indice != None):
            novoNome = input('Novo nome: ')
            novoPreco = float(input('Novo preco: '))
            atualizarProduto(indice, {'nome': novoNome, 'preco': novoPreco})
            print('Produto atualizado')
        else:
            print('Produto nao encontrado')
    
    elif(opcao == '5'): 
        print('REMOVER PRODUTO ========================')
        nome = input('Nome do produto para remover: ')
        indice = buscarProduto(nome)

        if indice != None:
            produto_removido = produtos.pop(indice)
            print('Produto removido com suceso!')
        else:
            print('Produto nao encontrado')    
    
    elif(opcao != None): 
        print('Opção não existe')    
    
    print()
    opcao = input('Opção desejada:')