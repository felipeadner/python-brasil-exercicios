"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""

def main():
   altura = float(input("Informe sua altura em metros: "))
   peso = float((72.7 * altura)-58)
   print("Seu peso ideal é: ",int(peso))

main()
