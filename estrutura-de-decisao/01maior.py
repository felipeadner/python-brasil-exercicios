"""

Faça um Programa que peça dois números e imprima o maior deles.

"""

def main():
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))

    if a > b:
        print("O primeiro número%2.f é maior que o segundo%2.f." %(a, b))

    elif b > a:
        print("O segundo número%2.f é maior que o primeiro%2.f." %(b, a))

    else:
        print("Os números são iguais")

main()
