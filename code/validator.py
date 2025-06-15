import re

def validar_cartao(numero_cartao: str) -> bool:
    # Remove espaços e verifica se só há dígitos
    numero_cartao = numero_cartao.replace(" ", "")
    if not numero_cartao.isdigit():
        return False

    soma = 0
    inverter = False

    # Percorre os dígitos da direita para a esquerda
    for digito in reversed(numero_cartao):
        n = int(digito)
        if inverter:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
        inverter = not inverter

    # Se a soma for múltipla de 10, o cartão é válido
    return soma % 10 == 0

def identificar_bandeira(numero_cartao: str) -> str:
    numero_cartao = numero_cartao.replace(" ", "")

    bandeiras = [
        ("Visa",            r"^4\d{12}(\d{3})?$"),
        ("MasterCard",      r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$"),
        ("American Express",r"^3[47]\d{13}$"),
        ("Diners Club",     r"^3(0[0-5]|[68]\d)\d{11}$"),
        ("Discover",        r"^6(011\d{12}|5\d{14}|4[4-9]\d{13})$"),
        ("EnRoute",         r"^(2014|2149)\d{11}$"),
        ("JCB",             r"^35\d{14}$"),  # 3528-3589 + 12 dígitos
        ("Voyager",         r"^8699\d{11}$"),
        ("Hipercard",       r"^(606282\d{10}(\d{3})?|3841\d{15})$"),
        ("Aura",            r"^50\d{14}$"),  # Começa com 50 e tem 16 dígitos
        ("Elo",             r"^(4011(78|79)\d{10}|(431274|438935|451416|457393|4576(31|32)|504175|5067(0[0-9]|1[0-9]|20)|509\d{12}|627780|636297|636368|650\d{13}|6516\d{12}|6550\d{12}))$")
    ]

    for nome, padrao in bandeiras:
        if re.match(padrao, numero_cartao):
            return nome
    return "Bandeira desconhecida"


# Exemplo de uso:
numero = input("Digite o número do cartão de crédito: ")
if validar_cartao(numero):
    print("Cartão válido!")
    print("Bandeira: "+identificar_bandeira(numero)) 
else:
    print("Cartão inválido.")
