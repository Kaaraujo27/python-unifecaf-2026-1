# Avaliação Continuada 4 - 1 ponto
# PROJETO DE VENDAS - parte 2
# Exercicios de CRUD completo (Produtos, Vendedores e Vendas)
# Entrega - dia 24/05/2026

import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='projeto_vendas_eletronicos_unifecaf'
        )

        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            return conexao

    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None


def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='projeto_vendas_eletronicos_unifecaf',
            user='root',
            password='root'        )
        if conexao.is_connected():
            print("Conexao bem sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# PRODUTOS

def criar_produto():
    # Exercicio 1: cadastrar um novo produto na tabela produtos (descricao, preco).
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO produtos (nome, preco) VALUES  (%s, %s)", (descricao, preco)

        """)
        print("\n=== CRIE UM PRODUTO ===")

        nome = input("Nome: ")
        preco = float(input("Preço: "))

        cursor.close()
        fechar_conexao(conexao)
    return


def listar_produtos():
    # Exercicio 2: listar todos os produtos cadastrados com id, descricao e preco.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute(""""
        SELECT id, descricao, preco FROM produtos
        
        """)

        produtos = cursor.fetchall()

        print("\n=== LISTA DE PRODUTOS ===")
        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")

        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_produto():
    # Exercicio 3: atualizar descricao e/ou preco de um produto existente por id.
    conexao = conectar ()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE produtos SET nome=?, preco=? WHERE id_produto=?", (descricao, preco, id_produto)

        """)

        produto = cursor.fetchall()

        print("\n=== ATUALIZAR PRODUTO ===")

        id_produto = int(input("ID: "))
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))

        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_produto():
    # Exercicio 4: excluir um produto por id, tratando dependencias em vendas_produtos.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM vendas_produtos WHERE id_produto=?", (id_produto)
                       
        """)

        id_produto = int(input("ID: "))

        cursor.close()
        fechar_conexao(conexao)
    return


# VENDEDORES

def criar_vendedor():
    # Exercicio 5: cadastrar um novo vendedor na tabela vendedores.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO vendedores (nome)

        """)
        print("\n=== INSIRA O NOME DO VENDEDOR ===")

        nome = input("Nome: ")

        cursor.close()
        fechar_conexao(conexao)
    return


def listar_vendedores():
    # Exercicio 6: listar todos os vendedores cadastrados.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute(""""
        SELECT id, nome, FROM vendedores
        
        """)

        vendedor = cursor.fetchall()

        print("\n=== LISTA DE VENDEDORES ===")
        for vendedor in vendedor:
            print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}")

        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_vendedor():
    # Exercicio 7: atualizar o nome de um vendedor existente por id.
    conexao = conectar ()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE vendedores SET nome=?WHERE id=?", (nome, id_vendedor)

        """)

        vendedor = cursor.fetchall()

        print("\n=== ATUALIZAR PRODUTO ===")

        id_produto = int(input("ID: "))
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))

        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_vendedor():
    # Exercicio 8: excluir vendedor por id, validando se possui vendas vinculadas.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        DELETE FROM vendedores WHERE id_vendedor=?", (id_vendedor)
                       
    """)
        
        vendedor = cursor.fetchall()

        print("\n=== EXCLUIR VENDEDOR ===")

        id_vendedor = int(input("ID: "))

        cursor.close()
        fechar_conexao(conexao)
    return


# VENDAS

def criar_venda_com_itens():
    # Exercicio 9: criar uma venda e inserir itens na tabela vendas_produtos com quantidade e valores.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        id_vendedor = int(input("ID do vendedor: "))

        total = 0

        cursor.execute("""
            INSERT INTO vendas (vendedor_id, desconto, valor_final)
            VALUES (%s, %s, %s)
        """, (id_vendedor, 0, 0))
        id_venda = cursor.lastrowid
        conexao.commit()

        while True:
            id_produto = int(input("Produto ID (0 para sair): "))
            if id_produto == 0:
                break

            quantidade = int(input("Quantidade: "))

            cursor.execute("SELECT preco FROM produtos WHERE id = %s", (id_produto,))
            produto = cursor.fetchone()
            if produto is None:
                print("Produto não encontrado.")
                continue

            preco = produto[0]
            total_item = preco * quantidade
            total += total_item

            cursor.execute("""
                INSERT INTO vendas_produtos (id_venda, produto_id, quantidade, valor_unitario)
                VALUES (%s, %s, %s, %s)
            """, (id_venda, id_produto, quantidade, preco))

        desconto = float(input("Desconto: "))
        valor_final = total - desconto

        cursor.execute("""
            UPDATE vendas SET desconto=%s, valor_final=%s WHERE id_venda=%s
        """, (desconto, valor_final, id_venda))
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)
    return


def listar_vendas_completas():
    # Exercicio 10: listar vendas com vendedor e itens (produto, quantidade, valor_unitario, valor_total).
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT vendas.id AS id_venda, vendedores.nome, vendas.data, vendas.valor_final
            FROM vendas
            JOIN vendedores ON vendas.vendedor_id = vendedores.id
        """)

        for id_venda, vendedor, data, total in cursor.fetchall():
            print(f"\nVenda #{id_venda} | Vendedor: {vendedor} | Data: {data} | Total: R${total:.2f}")

            cursor.execute("""
                SELECT produtos.nome, vendas_produtos.quantidade, vendas_produtos.valor_unitario
                FROM vendas_produtos
                JOIN produtos ON vendas_produtos.produto_id = produtos.id
                WHERE vendas_produtos.venda_id = %s
            """, (id_venda,))

            for nome, quantidade, valor_unitario in cursor.fetchall():
                print(f" - {nome}: {quantidade}x R${valor_unitario:.2f}")

        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_venda = int(input("ID da venda: "))
        desconto = float(input("Novo desconto: "))
        valor_final = float(input("Novo valor final: "))

        cursor.execute("""
            UPDATE vendas SET desconto=%s, valor_final=%s WHERE id_venda=%s
        """, (desconto, valor_final, id_venda))
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_venda = int(input("ID da venda: "))

        cursor.execute("DELETE FROM vendas_produtos WHERE id_venda = %s", (id_venda,))
        cursor.execute("DELETE FROM vendas WHERE id = %s", (id_venda,))
        
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE vendas SET desconto=?, valor_final=? WHERE id_vendedor=? (desconto, valor_final, venda_id)

    """)
        
        venda_id = int(input("ID da venda: "))
        desconto = float(input("Novo desconto: "))
        valor_final = float(input("Novo valor final: "))   

        cursor.close()
        fechar_conexao(conexao)
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        DELETE FROM vendas WHERE id_vendedor=?", (id_vendedor)
                       
    """)
        
        vendedor = cursor.fetchall()

        print("\n=== EXCLUIR VENDEDOR ===")

        id_vendedor = int(input("ID: "))

        cursor.close()
        fechar_conexao(conexao)
    return


def menu():
    opcoes = {
        "1": ("Criar produto", criar_produto),
        "2": ("Listar produtos", listar_produtos),
        "3": ("Atualizar produto", atualizar_produto),
        "4": ("Excluir produto", excluir_produto),
        "5": ("Criar vendedor", criar_vendedor),
        "6": ("Listar vendedores", listar_vendedores),
        "7": ("Atualizar vendedor", atualizar_vendedor),
        "8": ("Excluir vendedor", excluir_vendedor),
        "9": ("Criar venda com itens", criar_venda_com_itens),
        "10": ("Listar vendas completas", listar_vendas_completas),
        "11": ("Atualizar venda e itens", atualizar_venda_e_itens),
        "12": ("Excluir venda", excluir_venda),
    }

    while True:
        print("\n=== MENU AC4 - CRUD COMPLETO ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
            print("Exercicio em estrutura base (return vazio).")
        else:
            print("Opcao invalida. Tente novamente.")
