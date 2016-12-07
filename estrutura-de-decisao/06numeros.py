"""

Faça um Programa que leia três números e mostre o maior deles.

"""

def main():

    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    c = float(input("Informe o terceiro número: "))

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

    else:

        print("Informe 3 algarismos corretamente.")

main()