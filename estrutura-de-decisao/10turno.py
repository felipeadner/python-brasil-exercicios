"""

Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

"""

def turno():

    t = input("Informe o seu turno: (M) Matutino, (V) Vespertino, (N) Noturno: ").upper()

    if t == "M":
        print("Bom dia!")

    elif t == "V":
        print("Boa tarde!")

    elif t == "N":
        print("Boa noite!")

    else:
        print("Informe corretamente o turno correspondente")

turno()
