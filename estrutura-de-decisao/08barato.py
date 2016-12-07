"""

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.

"""

def barato():

    a = float(input("Preço do primeiro produto: "))
    b = float(input("Preço do segundo produto: "))
    c = float(input("Preço do terceiro produto: "))

    if a < b and c:
        print("%f é o mais barato" % a)

    elif b < c and a:
        print("%f é o mais barato" % b)

    elif c < b and a:
        print("%f é o mais barato" % c)

    else:
        print("Informe 3 produto corretamente.")

barato()
