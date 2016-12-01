"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
"""

import math

def main():
    raio = float(input("Digite o raio do círculo em metros: "))
    area = float(math.pi * (raio ** 2))
    print ("A área do circulo é de",area,"m²")

main()
