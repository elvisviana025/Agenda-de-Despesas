class Despesa:

    def __init__(self):
        self.__nome = str(input(f'→ Digite o nome da despesa: ')).strip().lower()
        self.__valor = float(input(f'→ Digite o valor da despesa: '))
        print(f'Despesa "{self.__nome}" criada com valor {self.__valor}.')

    def get_valor(self):
        return self.__valor

    def get_nome(self):
        return self.__nome

    def imprime_despesa(self):
        print(f'• Despesa "{self.__nome}: R$ {self.__valor}"')