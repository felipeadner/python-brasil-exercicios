"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média
"""


def main():
    bim1 = float(input("Nota do 1º Bimestre: "))
    bim2 = float(input("Nota do 2º Bimestre: "))
    bim3 = float(input("Nota do 3º Bimestre: "))
    bim4 = float(input("Nota do 4º Bimestre: "))
    
    media = float((bim1 + bim2 + bim3 + bim4) / 4)
    print ("Nota média: ", media)

main()
