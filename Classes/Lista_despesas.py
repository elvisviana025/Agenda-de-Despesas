class Lista_despesas:

    def __init__(self):
        self.__lista_despesas = []

    @property
    def lista_despesas(self):
        return self.__lista_despesas

    @lista_despesas.setter
    def lista_despesas(self, despesa):
        self.__lista_despesas.append(despesa)

    def remover_despesa_da_lista(self, despesa):
        self.__lista_despesas.remove(despesa)


    def imprime_lista(self):
        if self.lista_despesas == []:
            print(f'• Lista vazia')
        else:
            for despesa in self.lista_despesas:
                print(despesa)