"""

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

"""

def main():

    valor = float(input("Informe qualquer valor:"))

    if valor > 0:

        print("%2.f é positivo." %valor)

    elif valor < 0:

        print("%2.f é negativo" %valor)

    else:

        print("%2.f é nulo" %valor)

main()