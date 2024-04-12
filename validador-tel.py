import re

# Expressão regular para validar o formato (XX) 9XXXX-XXXX
pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"

def validate_numero_telefone(phone_number):
    """
    Função para validar se um número de telefone está no formato correto.

    Argumentos:
      phone_number: Uma string representando o número de telefone.

    Retorno:
      Uma mensagem indicando se o número de telefone é válido ou inválido.
    """

    # Verifica se o padrão regex corresponde ao número de telefone
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Recebe o número de telefone diretamente (ajuste conforme necessário para o ambiente de teste)
phone_number = input()

# Imprime o resultado da validação
print(validate_numero_telefone(phone_number))
