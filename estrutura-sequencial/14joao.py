"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
Caso contrário mostrar tais variáveis com o conteúdo ZERO.

"""

def main():

    kilo_pescado = float(input("Informe quantos quilos foram pescados: "))

    if kilo_pescado > float(50):
        kilo_excedido = kilo_pescado - float(50)
        multa = kilo_excedido * 4.00
        print("Você excedeu %3.fKg. E irá pagar uma multa de R$%3.f." %(kilo_excedido, multa))

    else:
        print("Você não excedeu o limite de pescados.")

main()