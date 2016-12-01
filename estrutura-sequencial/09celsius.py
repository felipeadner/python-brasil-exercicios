"""
Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
"""

def main():
    farenheit = float(input("Informe a temperatura em F: "))
    celsius = int(5 * (farenheit - 32) / 9)
    print(farenheit,"F. Corresponde a",celsius,"C")

main()
