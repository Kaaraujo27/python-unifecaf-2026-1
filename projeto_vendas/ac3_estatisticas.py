# Avaliação Continuada 3 - 1 ponto
# PROJETO DE VENDAS - parte 1
# Exercicios de estatisticas de vendas.
# Entrega - dia 17/05/2026

from datetime import datetime

import mysql.connector
from mysql.connector import Error

from projeto_vendas.banco_de_dados.conexao import fechar_conexao

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='projeto_vendas',
            user='root',
            password='root'        )
        if conexao.is_connected():
            print("Conexao bem sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def total_vendas_periodo():
    # Exercicio 1: calcular o valor total vendido em um periodo usando vendas.valor_final.
    conexao = conectar()

    while True:
        data_inicial = input('Data inicial (YYYY-MM-DD): ')
        try:
            datetime.strptime(data_inicial, '%Y-%m-%d')
            break
        except:
            print('Data inválida. Tente novamente.')

    while True:
        data_final = input('Data final (YYYY-MM-DD): ')
        try:
            datetime.strptime(data_final, '%Y-%m-%d')
            break
        except:
            print('Data inválida. Tente novamente.')

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT SUM(vaolor_final) total_vendido
                FROM vendas
                WHERE data_e_hora between %s and %s
            """, (data_inicial, data_final))

            total_vendas = cursor.fetchone()

            print("\n=== TOTAL DE VENDAS POR PERIODO ===")
            print(f"Valor total: {total_vendas[0]}]")

            cursor.close()
            fechar_conexao(conexao)
            


def qtd_vendas_por_vendedor():
    # Exercicio 2: contar quantas vendas cada vendedor realizou usando vendas.id_vendedor.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                vendedores.nome,
                COUNT(*) qtde_vendas
                SUM(valor_final ) total_vendas
                MAX(valor_final ) maior_venda
                MIN(valor_final ) menor_venda
                AVG(valor_final ) ticket_medio
            FROM vendas
            INNER JOIN vendedores
                ON vendas.id_vendedor = vendedores.id
            GROUP BY vendedores.id
        """)

        vendedores = cursor.fetchall()

        print("\n=== QUANTIDADE DE VENDAS POR VENDEDOR ===")
        for vendedor in vendedores:
            print(f"Vendedor: {vendedor[0]} - Quantidade de vendas: {vendedor[1]}")

        cursor.close()
        fechar_conexao(conexao)


def ticket_medio_geral():
    # Exercicio 3: calcular o ticket medio geral a partir de vendas.valor_final.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                AVG(valor_final)
            FROM vendas
        """)

        ticket_medio = cursor.fetchone()
        
        print("\n=== TICKET MEDIO GERAL ===")
        print(f"Valor total: {ticket_medio[0]}")

        cursor.close()
        fechar_conexao(conexao)


def ticket_medio_por_vendedor():
    # Exercicio 4: calcular o ticket medio de cada vendedor cruzando vendas e vendedores.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                vendedores.nome,
                CONCAT('R$ ', FORMAT(AVG(vendas.valor_final), 2, 'pt_BR')) ticket_medio
            FROM vendas
            INNER JOIN vendedores
                ON vendas.id_vendedor = vendedores.id
            GROUP BY vendedores.nome
        """) 

        vendedores = cursor.fetchall()

        print("\n=== TICKET MEDIO POR VENDEDOR ===")
        for vendedor in vendedores:
            print(f"Vendedor: {vendedor[0]} - qtde vendas: {vendedor[1]}")
        
        cursor.close()
        fechar_conexao(conexao)

def produto_mais_vendido_qtd():
    # Exercicio 5: identificar o produto mais vendido por quantidade em vendas_produtos.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                vendas_produtos.id_produto
                SUM(vendas_pruduto.quantidade) total_vendido
            FROM vendas_produtos
            GROUP BY vendas_produtos.id_produto
            ORDER BY total_vendido DESC LIMIT 1
        """)

        produto_mais_vendido_qtd = cursor.fetchall()

        print("\n=== PRODUTO MAIS VENDIDO ===")
        for produto in produto:
            print(f"Produto: {produto[0]} - qtde vendas: {produto[1]}")

        cursor.close()
        fechar_conexao(conexao)

def produto_mais_rentavel_valor():
    # Exercicio 6: identificar o produto que gerou maior faturamento somando vendas_produtos.valor_total.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                vendas_produtos.id_produto,
                SUM(vendas_produtos.valor_total) total_faturado
            FROM vendas_produtos
            GROUP BY vendas_produtos.id_produto
            ORDER BY total_faturado DESC
            LIMIT 1
        """)

        produto_mais_rentavel = cursor.fetchone()

        print("\n=== PRODUTO MAIS RENTAVEL ===")
        if produto_mais_rentavel:
            print(f"Produto: {produto_mais_rentavel[0]} - Valor: {produto_mais_rentavel[1]}")
        else:
            print("Nenhum produto encontrado.")

        cursor.close()
        fechar_conexao(conexao)


def total_descontos_aplicados():
    # Exercicio 7: somar todos os descontos concedidos usando vendas.desconto.
    conexao = conectar()
    
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                SUM(vendas.desconto) total_descontos
            FROM vendas
        """)

        total_descontos = cursor.fetchone()

        print("\n=== TOTAL DE DESCONTOS APLICADOS ===")
        print(f"Valor dos descontos: {total_descontos[0]}")

        cursor.close()
        fechar_conexao(conexao)


def percentual_desconto_medio():
    # Exercicio 8: calcular o percentual medio de desconto comparando desconto e valor_final das vendas.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                AVG((vendas.desconto / vendas.valor_final) * 100) percentual_medio
            FROM vendas
        """)

    percentual_desconto_medio = cursor.fetchone

    print("\n=== PERCENTUAL DE DESCONTOS ===")
    print(f"Percentual dos descontos: {percentual_desconto_medio[0]}")

    cursor.close()
    fechar_conexao(conexao)


def faturamento_por_dia():
    # Exercicio 9: agrupar o faturamento por dia com base em vendas.data_e_hora e vendas.valor_final.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                DATE(vendas.data_e_hora)
                UM(venas.valor_final) faturamento_dia
            FROM vendas
            GROUP BY DATE(vendas.data_e_hora)
            ORDER BY DATE(vendas.data_e_hora)
        """)

        faturamento_por_dia = cursor.fetchall

        print("\n=== FATURAMENTO POR DIA ===")
        print(f"Fatumento diário: {faturamento_por_dia[1]}")

        cursor.close()
        fechar_conexao(conexao)

def top_3_vendedores_faturamento():
    # Exercicio 10: listar os 3 vendedores com maior faturamento total no periodo.
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT
                vendas.id_vendedor
                SUM(vendas.valor_final) faturanento_total
            FROM vendas
            GROUP BY vendas.id_vendedor
            ORDER BY faturamento_total DESC LIMIT 3
        """)

        top_3_vendedores_faturamento = cursor.fetchall

        print("\n=== MELHORES VENDEDORES ===")
        print(f"TOP 3 Vendedores: {top_3_vendedores_faturamento[0]}")

        cursor.close()
        fechar_conexao(conexao)

def menu_relatorios():
    opcoes = {
        "1": ("Total de vendas por periodo", total_vendas_periodo),
        "2": ("Quantidade de vendas por vendedor", qtd_vendas_por_vendedor),
        "3": ("Ticket medio geral", ticket_medio_geral),
        "4": ("Ticket medio por vendedor", ticket_medio_por_vendedor),
        "5": ("Produto mais vendido por quantidade", produto_mais_vendido_qtd),
        "6": ("Produto mais rentavel por faturamento", produto_mais_rentavel_valor),
        "7": ("Total de descontos aplicados", total_descontos_aplicados),
        "8": ("Percentual medio de desconto", percentual_desconto_medio),
        "9": ("Faturamento por dia", faturamento_por_dia),
        "10": ("Top 3 vendedores por faturamento", top_3_vendedores_faturamento),
    }

    while True:
        print("\n=== MENU AC3 - RELATORIOS ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nGerando relatorio: {descricao}")
            resultado = funcao()

            if resultado is None:
                print("Relatorio em estrutura base (return vazio).")
            else:
                print(resultado)
        else:
            print("Opcao invalida. Tente novamente.")
