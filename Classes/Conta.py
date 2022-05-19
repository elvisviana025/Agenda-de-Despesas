class Conta:

    def __init__(self, valor):
        self.__valor_inicial = valor
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    @property
    def valor_inicial(self):
        return self.__valor_inicial

    def imprime_valor_inicial(self):
        print(f'• Valor inicial: {self.__valor_inicial}.')

    def imprime_saldo(self):
        print(f'• Valor disponível: {self.__saldo}.')

    def depositar_valor(self):
        valor = float(input(f'• Digite o valor do deposito: '))
        self.__saldo += valor

    def adicionar_despesa(self, valor_despesa):
        self.__saldo -= valor_despesa

    def remover_despesa(self, valor_despesa):
        self.__saldo += valor_despesa
