"""
Exercício 000 - Estressados

Na entrada de um evento de um experimento social, os participantes ganhavam uma pulseira especial que precisavam ficar
 utilizando. A pulseira informava, num pequeno visor, um número inteiro que representava o nível de stress daquele
participante. O número 1 significava totalmente tranquilo e vai aumentando conforme o stress do participante aumentava
até o valor máximo de infinito. Para fazer uma representação lógica de homens e mulheres em um vetor de inteiros,
os números positivos representam os homens e os números negativos representam mulheres. Precisamos escrever os
algorítmos que identifiquem informações importantes sobre os participantes da fila.

Exemplos:
{} equivale a uma fila vazia.
{-1, -50, -99} equivale a uma mulher totalmente tranquila, uma mulher médio estressada e uma mulher extremamente
estressada.
{80, 70, 90, -4} equivale a três homens estressados e uma mulher tranquila.
"""


class Estressados:
    def __init__(self, fila: list):
        self._fila = fila

    @property
    def fila(self):
        return self._fila

    def in_lista(self, valor):
        """existe determinado valor na fila?"""

        if valor in self._fila:
            return True
        return False

    def index_of(self, valor):
        """qual posição aparece X na fila pela primeira vez?"""

        if valor not in self.fila:
            return -1
        return self.fila.index(valor)

    def find_if(self):
        """qual a posição do primeiro homem da fila?"""

        for pessoa in enumerate(self._fila):
            if pessoa[1] > 0:
                return pessoa[0]
        return -1

    def min_element(self):
        """qual a posição do menor valor da lista?"""

        if not self.fila:
            return -1
        return self.fila.index(min(self.fila))

    def find_min_if(self):
        """qual a posição do homem mais calmo?"""

        if not self.fila:
            return -1
        temp_fila = [x for x in self.fila if x > 0]
        return min(temp_fila)


fila = Estressados([-1, -2, 20, 2, 1])
# Testes
print(fila.in_lista(50))
print(fila.index_of(-2))
print(fila.find_if())
print(fila.min_element())
print(fila.find_min_if())
