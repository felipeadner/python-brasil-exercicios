"""

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

"""

def aumento():

    s = float(input("Informe seu salário atual: "))

    if s <= 280.0:
        p = (20.0/100.0) * s
        r = s + p
        print("Salário entes do reajuste: R$%2.f" %s)
        print("Porcentagem de aumento: 20%")
        print("Valor do aumento: R$%2.f" %p)
        print("Salário reajustado: R$%2.f" %r)

    elif s > 280.0 and s <= 700.0:
        p = (15.0/100.0) * s
        r = s + p
        print("Salário entes do reajuste: R$%2.f" %s)
        print("Porcentagem de aumento: 15%")
        print("Valor do aumento: R$%2.f" %p)
        print("Salário reajustado: R$%2.f" %r)

    elif s > 700.0 and s <= 1500.0:
        p = (10.0/100.0) * s
        r = s + p
        print("Salário entes do reajuste: R$%2.f" %s)
        print("Porcentagem de aumento: 10%")
        print("Valor do aumento: R$%2.f" %p)
        print("Salário reajustado: R$%2.f" %r)

    elif s > 1500.0:
        p = (5.0/100.0) * s
        r = s + p
        print("Salário entes do reajuste: R$%2.f" %s)
        print("Porcentagem de aumento: 5%")
        print("Valor do aumento: R$%2.f" %p)
        print("Salário reajustado: R$%2.f" %r)

    else:
        print("Informe o salario corretamente!")

aumento()

