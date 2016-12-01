"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
o produto do dobro do primeiro com metade do segundo . 
a soma do triplo do primeiro com o terceiro. 
o terceiro elevado ao cubo.
"""

def main():
    int1 = int(input("Informe o primeiro número Inteiro: "))
    int2 = int(input("Informe o segundo número Inteiro: "))
    real = float(input("Informe um número Real: "))

    produto = float(int1 * int1 * (int2 / 2))
    soma = float(int1 * 3 + real)
    cubo = float(real ** 3)

    print("o produto do dobro do primeiro com metade do segundo = ",produto,
          "A soma do triplo do primeiro com o terceiro = ",soma,
          "O terceiro elevado ao cubo = ",cubo)

main()
