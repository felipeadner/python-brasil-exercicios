"""
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário. 
"""

def main():
    lado = float(input("Digite o valor em metros do lado do quadrado: "))
    area = float(lado ** 2)
    dobro = float(area * 2)
    print("Para um quadrado de lado:",lado,"m. A área corresponde é:",area,"m². "
          "E o dobro dessa área é:",dobro,"m²")

main()
