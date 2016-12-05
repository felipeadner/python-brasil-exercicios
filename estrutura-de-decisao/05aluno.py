"""

Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""

def main():

    parcial1 = float(input("Informe a Parcial 01: "))
    parcial2 = float(input("Informe a Parcial 02: "))

    nota = float((parcial1 + parcial2) / 2)

    if nota == 10.0:

        print("Parabéns, sua nota é %f. Você foi aprovado com distinção." %nota)

    elif nota >= 7.0:

        print("Parabéns, sua nota é %f. Você foi aprovado." %nota)

    elif nota < 7.0:

        print("Que pena, sua nota é %f. Você foi reprovado" %nota)

    else:

        print("Não foi possível calcular sua nota")

main()
