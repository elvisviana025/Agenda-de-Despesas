class Despesa:

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
        print(f'Despesa "{self.__nome}" criada com valor {self.__valor}.')

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

    def imprime_despesa(self):
        print(f'• Despesa "{self.__nome}": R$ {self.__valor}')

    def registra_despesa(self, despesa, lista, conta):
        lista.lista_despesas = despesa
        conta.adicionar_despesa_na_conta(despesa.valor)

