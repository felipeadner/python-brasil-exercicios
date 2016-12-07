"""

Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

def decrescente():

    a = float(input("Informe o 1º número: "))
    b = float(input("Informe o 2º número: "))
    c = float(input("Informe o 3º número: "))

    if a > b and b > c:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(a, b, c))

    elif a > c and c > b:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(a, c, b))

    elif c > a and a > b:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(c, a, b))

    elif c > b and b > a:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(c, b, a))

    elif b > a and a > c:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(b, a, c))

    elif b > c and c > a:
        print("Seus números em ordem decrescente: %2.f, %2.f, %2.f " %(b, c, a))

    else:
        print("Informe apenas números distintos")

decrescente()