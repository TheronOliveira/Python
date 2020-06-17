
class Calculadora:

    #construtor da classe
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2

    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2
    
    def divisao(self):
        return self.num1 / self.num2
