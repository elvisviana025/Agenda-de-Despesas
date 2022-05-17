class Conta:

    def __init__(self, valor):
        self.__valor = valor

    def imprime_valor(self):
        print(f'Valor disponível: {self.__valor}.')

    def depositar_valor(self):
        valor = float(input(f'• Digite o valor do deposito: '))
        self.__valor += valor

    def adicionar_despesa(self, valor_despesa):
        self.__valor -= valor_despesa

    def remover_despesa(self, valor_despesa):
        self.__valor += valor_despesa
