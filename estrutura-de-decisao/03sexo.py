"""

Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""

def main ():

    sexo = str(input("Informe (f) para Feminino ou (m) para Masculino: ").upper())

    if sexo == "F":

        print("Seu gênero é Feminino.")

    elif sexo == "M":

        print("Seu gênero é Masculino")

    else:

        print("Letra incorreta")

main()
