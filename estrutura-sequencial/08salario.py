"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. 
"""

def main():
    vH = float(input("Informe o valor recebido por hora: R$"))
    tH = float(input("Informe quantas horas foram trabalhadas neste mês: "))

    salarioB = float(tH * vH)
    
    irenda = float(salarioB * 11/100.0)
    inss = float(salarioB * 8/100.0)
    sindicato = float(salarioB * 5/100)

    
    descontos = float(irenda + inss + sindicato)
    salarioL = float(salarioB - descontos)

    print("Esse mês você trabalhou: ",tH,"Horas")
    print("Você recebe R$",vH,"por cada hora trabalhada")
    print("Seu salario base é: R$",salarioB)
    print("Seus descontos. Imposto de Renda: R$",irenda,
          "INSS: R$",inss,
          "Sindicato: R$",sindicato,
          "Totalizando: R$",descontos,"de descontos")
    print("Seu salário líquido corresponde à: R$",salarioL)

main()
