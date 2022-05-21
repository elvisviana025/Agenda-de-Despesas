class Conta:

    def __init__(self, valor):
        self.__valor_inicial = valor
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor

    @property
    def valor_inicial(self):
        return self.__valor_inicial

    @valor_inicial.setter
    def valor_inicial(self, valor):
        self.__valor_inicial += valor

    def imprime_valor_inicial(self):
        print(f'• Valor inicial: {self.__valor_inicial}.')

    def imprime_saldo(self):
        print(f'• Valor disponível: {self.__saldo}.')

    def depositar_valor(self):
        valor = float(input(f'• Digite o valor do deposito: '))
        self.valor_inicial = valor
        self.saldo = valor

    def adicionar_despesa_na_conta(self, valor_despesa):
        self.__saldo -= valor_despesa

    def remover_despesa_da_conta(self, valor_despesa):
        self.__saldo += valor_despesa
