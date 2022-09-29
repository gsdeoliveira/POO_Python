"""O objetivo dessa atividade é implementar uma calculadora a bateria.
Se há bateria, ela executa operações de soma e divisão.
É possível também mostrar a quantidade de bateria e recarregar a calculadora.
Ela avisa quando está sem bateria e se há tentativa de divisão por 0."""


class Calculadora:
    def __init__(self, max_bateria):
        self.max_bateria = max_bateria
        self.display = 0.00
        self.bateria = 0

    def show(self):
        """Exibe o display e a bateria da calculadora"""

        print(f'Display: {self.display}\nBateria: {self.bateria}')

    def charge(self, valor):
        """Recarrega a calculadora"""

        if self.bateria + valor > self.max_bateria:
            self.bateria = self.max_bateria
        else:
            self.bateria = self.bateria + valor

    def sum(self, valor1, valor2):
        """Realiza a operação de soma"""

        if self.bateria == 0:
            print(f'Bateria insuficiente!')
        else:
            self.display = valor1 + valor2
            self.bateria -= 1

    def div(self, valor1, valor2):
        """Realiza a operação de divisão"""

        if self.bateria == 0:
            print(f'Bateria insuficiente!')
        else:
            if valor2 == 0:
                print(f'Não é possível realizar a divisão por 0!')
            else:
                self.display = valor1 / valor2
                self.bateria -= 1


calc = Calculadora(3)
