import textwrap

# Inicializa os usuários e contas diretamente no script para garantir que estão disponíveis.
usuarios = [
    {"nome": "Sergio", "cpf": "03217296680", "data_nascimento": "01-01-1980", "endereco": "Endereço de Sergio"}
]
contas = [
    {"id": 1, "agencia": "0001", "numero_conta": "12345", "usuario": usuarios[0], "saldo": 10000000, "extrato": "Extrato:\n", "tipo": "Poupança"},
    {"id": 2, "agencia": "0001", "numero_conta": "54321", "usuario": usuarios[0], "saldo": 20000, "extrato": "Extrato:\n", "tipo": "Corrente"}
]

def menu():
    return """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [tf]\tTransferir fundos
    [cs]\tMudar conta
    [q]\tSair
    => """

def exibir_menu_cliente(cpf):
    print(f"\nContas registradas para CPF {cpf}:")
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            print(f"ID: {conta['id']}, Tipo: {conta['tipo']}, Saldo: R$ {conta['saldo']:.2f}")
    conta_selecionada_id = int(input("Selecione o ID da conta para operar: "))
    conta_selecionada = next((conta for conta in contas if conta['id'] == conta_selecionada_id and conta['usuario']['cpf'] == cpf), None)
    if conta_selecionada:
        print(f"Operando na conta ID {conta_selecionada['id']} do tipo {conta_selecionada['tipo']}.")
        return conta_selecionada
    else:
        print("Conta inválida ou não encontrada.")
        return None

def depositar(conta):
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nValor de depósito inválido.")

def sacar(conta):
    valor = float(input("Valor do saque: "))
    if 0 < valor <= conta['saldo']:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque:\tR$ {valor:.2f}\n"
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nSaque não realizado. Verifique o valor e tente novamente.")

def exibir_extrato(conta):
    print(f"\nExtrato da Conta ID {conta['id']}:")
    print(conta['extrato'])
    print(f"Saldo Atual: R$ {conta['saldo']:.2f}")

def transferir_fundos(conta_origem):
    conta_destino_id = int(input("Selecione o ID da conta de destino: "))
    conta_destino = next((conta for conta in contas if conta['id'] == conta_destino_id), None)
    if conta_destino and conta_destino != conta_origem:
        valor = float(input("Valor a transferir: "))
        if 0 < valor <= conta_origem['saldo']:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            conta_origem['extrato'] += f"Transferência enviada:\tR$ {valor:.2f}\n"
            conta_destino['extrato'] += f"Transferência recebida:\tR$ {valor:.2f}\n"
            print(f"\nTransferência de R$ {valor:.2f} realizada com sucesso da conta {conta_origem['id']} para a conta {conta_destino['id']}.")
        else:
            print("\nSaldo insuficiente para a transferência.")
    else:
        print("\nConta de destino inválida ou igual à conta de origem.")

def selecionar_acao(conta_ativa):
    while True:
        opcao = input(textwrap.dedent(menu()))
        if opcao == 'd':
            depositar(conta_ativa)
        elif opcao == 's':
            sacar(conta_ativa)
        elif opcao == 'e':
            exibir_extrato(conta_ativa)
        elif opcao == 'tf':
            transferir_fundos(conta_ativa)
        elif opcao == 'cs':
            return 'cs'
        elif opcao == 'q':
            print("Saindo...")
            return 'q'
        else:
            print("\nOpção inválida.")

def main():
    cpf = input("Por favor, entre com seu CPF para acessar suas contas: ")
    conta_ativa = exibir_menu_cliente(cpf)
    while True:
        resultado = selecionar_acao(conta_ativa)
        if resultado == 'cs':
            conta_ativa = exibir_menu_cliente(cpf)
            if not conta_ativa:
                break
        elif resultado == 'q':
            break

if __name__ == "__main__":
    main()
