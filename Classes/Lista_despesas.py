class Lista_despesas:

    def __init__(self):
        self.__lista_despesas = []

    @property
    def lista_despesas(self):
        return self.__lista_despesas

    @lista_despesas.setter
    def lista_despesas(self, despesa):
        self.__lista_despesas.append(despesa)

    def remover_da_lista(self, despesa):
        self.__lista_despesas.remove(despesa)

    def remover_da_lista_e_conta(self, conta):
        nome = str(input(f'Digite nome da despesa para remover: '))
        for despesa in self.lista_despesas:
            if despesa.nome == nome:
                conta.remover_despesa(despesa.valor)
                self.remover_da_lista(despesa)
                print(f'• Despesa "{despesa.nome}" removida.')

    def imprime_lista(self):
        if self.lista_despesas == []:
            print(f'• Lista vazia')
        else:
            for despesa in self.lista_despesas:
                despesa.imprime_despesa()