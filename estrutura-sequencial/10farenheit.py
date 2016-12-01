"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
"""

def main():
    celsius = float(input("Informe a temperatura em C: "))
    farenheit = float(celsius * 1.8 + 32)
    print(int(celsius),"C. Corresponde à",farenheit,"F")

main()
