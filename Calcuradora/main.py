
from cCalculadora import Calculadora

print("----------Calculadora em Puthon----------")
opcao = int(input("\nDigite 1 para adição\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão\n\n"))

while opcao <= 0 or opcao >= 5:
    print("opção inválida, escolha uma das opçoes abaixo: ")
    opcao = int(input("\nDigite 1 para adição\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão\n\n"))

print("A opção escolhida foi a ",opcao)
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

c = Calculadora(numero1,numero2)

if opcao == 1:
    print(f"A soma é: {c.soma()}")
    #print('A soma é: {}.'.format(c.soma()))
elif opcao == 2:
    print(f"A subtração é: {c.subtracao()}")
elif opcao == 3:
    print(f"A multiplicação é: {c.multiplicacao()}")
else:
    print(f"A divisão é: {c.divisao()}")
