"""

Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

"""

sexo = input("Informe seu sexo: (1) para masculino (2) para feminino:")

if sexo == str(1):

    aM = float(input("Informe sua altura em metros:"))
    peso_real = float(input("Informe seu peso atual:"))
    peso_ideal = float((78.7 * aM) - 58)

    if peso_real > peso_ideal:
        print("O peso informado é: %2.fKg. Você está acima do peso. Procure estar o mais próximo de: %2.fKg" %(
        peso_real, peso_ideal))

    elif peso_real < peso_ideal:
        print("O peso informado é: %2.fKg,. Você está abaixo do peso. Procure estar o mais próximo de: %2.fKg" %(
        peso_real, peso_ideal))

    elif peso_real == peso_ideal:
        print("O peso informado é: %2.fKg,. Você está em forma" % peso_ideal)

elif sexo == str(2):

    aF = float(input("Informe sua altura em metros:"))
    peso_real = float(input("Informe seu peso atual:"))
    peso_ideal = float((62.1 * aF) - 44.7)

    if peso_real > peso_ideal:
        print("O peso informado é: %2.fKg. Você está acima do peso. Procure estar o mais próximo de: %2.fKg" % (
            peso_real, peso_ideal))

    elif peso_real < peso_ideal:
        print("O peso informado é: %2.fKg,. Você está abaixo do peso. Procure estar o mais próximo de: %2.fKg" % (
            peso_real, peso_ideal))

    elif peso_real == peso_ideal:
        print("O peso informado é: %2.fKg,. Você está em forma" % peso_ideal)

