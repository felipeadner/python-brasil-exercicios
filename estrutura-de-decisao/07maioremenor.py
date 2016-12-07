"""

Faça um Programa que leia três números e mostre o maior e o menor deles.

"""

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

def maior():

    if a > b and c:
        print("%2.f é o maior número." %a)

    elif b > c and a:
        print("%2.f é o maior número." %b)

    elif c > b and a:
        print("%2.f é o maior número" %c)

    #verificação de iguais

    elif a == b and b and a > c:
        print("%2.f é o maior número." % a)

    elif a == c and c and a > b:
        print("%2.f é o maior número." % a)

    elif b == c and c and b > a:
        print("%2.f é o maior número." % b)

def menor():

    if a < b and c:
        print("%2.f é o menor número." % a)

    elif b < c and a:
        print("%2.f é o menor número." % b)

    elif c < b and a:
        print("%2.f é o menor número" % c)

    # verificação de iguais
    elif a == b and b and a < c:
        print("%2.f é o menor número." % a)

    elif a == c and c and a < b:
        print("%2.f é o menor número." % a)

    elif b == c and c and b < a:
        print("%2.f é o menor número." % b)

    else:
        print("Informe 3 algarismos corretamente.")

maior()
menor()