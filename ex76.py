# Definindo a tupla com os nomes dos produtos e seus respectivos preços
produtos_precos = (
    ("Lápis", 10.00),
    ("Bprracha", 12.50),
    ("Caderno", 8.99),
    ("Estojo", 15.30),
    ("Transferidor", 22.00),
)


# Função para exibir a tabela de preços
def exibir_tabela(produtos_precos):
    print("Listagem de Preços")
    print("-" * 30)
    print(f"{'Produto':<15}{'Preço':>15}")
    print("-" * 30)

    for produto, preco in produtos_precos:
        print(f"{produto:<15}R$.........{preco:>13.2f}")

    print("-" * 30)


# Chamando a função para exibir a tabela
exibir_tabela(produtos_precos)
