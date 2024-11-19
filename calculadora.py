from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

class Calculadora:
    def __init__(self):
        self.operacoes = {
            "1": Soma(),
            "2": Subtracao(),
            "3": Multiplicacao(),
            "4": Divisao()
        }

    def executar(self, operacao, a, b):
        if operacao in self.operacoes:
            return self.operacoes[operacao].calcular(a, b)
        return "Operação inválida!"
