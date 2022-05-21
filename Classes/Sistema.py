from Classes.Despesa import Despesa
from Classes.Lista_despesas import Lista_despesas
from Classes.Conta import Conta


class Sistema:

    def __init__(self):
        pass

    def imprime_texto_inicial(self):
        print(f'{" Notas de despesas ":-^40}')

    def cria_conta(self):
        valor_inicial = input(f'Digite o valor inicial: ')
        conta = Conta(float(valor_inicial))
        return conta

    def __cria_despesa(self):
        nome = str(input(f'→ Digite o nome da despesa: ')).strip()
        valor = float(input(f'→ Digite o valor da despesa: '))
        despesa = Despesa(nome, valor)
        return despesa

    def __exibe_menu(self):
        print('-' * 40)
        escolha = int(input(
            f'Escolha a operação:'
            f'\n{"[1] Saldo":<20} {"[2] Lista despesas":<20}'
            f'\n{"[3] + Despesa":<20} {"[4] - Despesa":<20}'
            f'\n{"[5] Deposita Valor":<20} {"[6] Gerar documento":<20}'
            f'\n{"[0] Sair":<20}'
            f'\n-> '))
        return escolha

    def remover_despesa_da_lista_e_conta(self, conta, lista):
        flag_removeu = False
        nome = str(input(f'Digite nome da despesa para remover: '))
        for despesa in lista.lista_despesas:
            if despesa.nome == nome:
                conta.remover_despesa_da_conta(despesa.valor)
                lista.remover_despesa_da_lista(despesa)
                print(f'• Despesa "{despesa.nome}" removida.')
                flag_removeu = True
        if flag_removeu == False:
            print(f'Erro: despesa "{nome}" não encontrada.')


    def exibe_e_filtra_menu(self, lista, conta):
        while True:
            escolha = self.__exibe_menu()

            if escolha == 1:
                conta.imprime_valor_inicial()
                conta.imprime_saldo()

            elif escolha == 2:
                lista.imprime_lista()
                conta.imprime_saldo()

            elif escolha == 3:
                despesa = self.__cria_despesa()
                despesa.registra_despesa(despesa, lista, conta)

            elif escolha == 4:
                self.remover_despesa_da_lista_e_conta(conta, lista)

            elif escolha == 5:
                conta.depositar_valor()
                conta.imprime_saldo()

            elif escolha == 6:
                lista_impressão = []
                for despesa in lista.lista_despesas:
                    string = str(f'• Despesa "{despesa.nome}": R$ {despesa.valor}\n')
                    lista_impressão.append(string)
                valor_inicial = str(conta.valor_inicial)
                saldo = str(conta.saldo)

                nome = str(input(f'• Digite o nome do arquivo: '))
                with open(f'Documentos/{nome}.txt', "a") as arquivo:  # WITH: FECHA O DOCUMENTO AUTOMATICAMENTE APÓS O FIM DOS CMDS
                    arquivo.write(f'----- Lista {nome} -----\n')
                    arquivo.write(f'• Valor inicial: R$ {valor_inicial}\n\n')
                    for despesa in lista_impressão:
                        arquivo.write(str(despesa))
                    arquivo.write(f'\n• Valor disponível: R$ {saldo}\n')


            elif escolha == 0:
                break
