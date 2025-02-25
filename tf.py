def adicionar_produto(inventario, codigo, nome, preco, quantidade):
    inventario[codigo] = {"nome": nome, "preço": preco, "quantidade": quantidade}
    print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(inventario, codigo):
    if codigo in inventario:
        nome = inventario[codigo]["nome"]
        del inventario[codigo]
        print(f"Produto {nome} removido com sucesso!")
    else:
        print("Produto não encontrado!")

def listar_produtos(inventario):
    if inventario:
        print("Inventário de produtos:")
        for codigo, info in inventario.items():
            print(f"Código: {codigo}, Nome: {info['nome']}, Preço: {info['preço']}, Quantidade: {info['quantidade']}")
    else:
        print("Inventário vazio.")

def main():
    inventario = {}
    while True:
        print("\nOpções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionar_produto(inventario, codigo, nome, preco, quantidade)
        elif opcao == "2":
            codigo = input("Digite o código do produto a ser removido: ")
            remover_produto(inventario, codigo)
        elif opcao == "3":
            listar_produtos(inventario)
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
