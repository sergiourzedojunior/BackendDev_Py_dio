# Cria uma lista 'itens' para armazenar os equipamentos
itens = []

# Cria um loop para solicitar ao usuário inserir até três equipamentos
for i in range(3):
    # Solicita ao usuário para digitar o nome do equipamento
    item = input()
    # TODO: Adicione o item à lista "itens"
    itens.append(item)
    i += 1

# Exibe a lista de itens
print("Lista de Equipamentos:")
# Loop que percorre cada item na lista "itens" e exibe com prefixo
for item in itens:
    print(f"- {item}")
