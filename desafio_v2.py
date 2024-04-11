import json
import textwrap

def carregar_dados():
    try:
        with open("dados_banco.json", "r") as arquivo:
            dados = json.load(arquivo)
        usuarios = dados.get("usuarios", [])
        contas = dados.get("contas", [])
        return usuarios, contas
    except FileNotFoundError:
        print("Arquivo de dados não encontrado, iniciando com dados vazios.")
        return [], []

def salvar_dados(usuarios, contas):
    with open("dados_banco.json", "w") as arquivo:
        json.dump({"usuarios": usuarios, "contas": contas}, arquivo, indent=4)

def menu_principal():
    menu_text = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu_text))

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def selecionar_conta(usuario, contas):
    print(f"\nContas disponíveis para {usuario['nome']}:")
    for conta in contas:
        if conta['usuario']['cpf'] == usuario['cpf']:
            print(f"ID: {conta['id']} - Tipo: {conta['tipo']} - Saldo: R${conta['saldo']:.2f}")
    conta_id = int(input("\nSelecione o ID da conta para operar: "))
    return next((conta for conta in contas if conta['id'] == conta_id), None)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return None
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo: ")
    novo_usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucesso! ===")
    return novo_usuario

def criar_conta(usuarios, contas, usuario):
    agencia = "0001"
    numero_conta = str(len(contas) + 1)
    tipo = input("Tipo de conta (Poupança/Corrente): ")
    nova_conta = {
        "id": len(contas) + 1,
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "tipo": tipo
    }
    contas.append(nova_conta)
    print("\n=== Conta criada com sucesso! ===")
    return nova_conta

def realizar_operacao(opcao, conta, usuarios, contas):
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta['saldo'] += valor
        print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif opcao == "e":
        print(f"\nExtrato da Conta ID {conta['id']} - {conta['tipo']}:")
        print(f"Saldo Atual: R$ {conta['saldo']:.2f}")
    elif opcao == "nc":
        criar_conta(usuarios, contas, conta['usuario'])
    elif opcao == "lc":
        selecionar_conta(conta['usuario'], contas)
    elif opcao == "nu":
        criar_usuario(usuarios)

def main():
    usuarios, contas = carregar_dados()
    cpf = input("Informe seu CPF para entrar ou cadastrar: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("CPF não registrado. Vamos criar um novo usuário.")
        usuario = criar_usuario(usuarios)
        if not usuario:
            return

    conta = selecionar_conta(usuario, contas)
    if not conta:
        print("Nenhuma conta associada encontrada, criando uma nova.")
        conta = criar_conta(usuarios, contas, usuario)

    while True:
        opcao = menu_principal()
        if opcao == "q":
            salvar_dados(usuarios, contas)
            print("Saindo...")
            break
        realizar_operacao(opcao, conta, usuarios, contas)

if __name__ == "__main__":
    main()
