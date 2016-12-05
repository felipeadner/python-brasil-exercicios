"""

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""

def main():

    letra = input("Informe uma letra: ")

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":

        print("A letra %s é uma vogal." %letra)

    else:

        print("A letra %s é uma consoante" %letra)

main()

