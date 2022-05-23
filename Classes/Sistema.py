from Classes.Despesa import Despesa
from Classes.Lista_despesas import Lista_despesas
from Classes.Conta import Conta

class Sistema:

    def __init__(self):
        pass

    def imprime_texto_inicial(self):
        print(f'{" Notas de despesas ":-^40}')

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

    def cria_conta(self):
        valor_inicial = input(f'→ Digite o valor inicial: R$ ')
        conta = Conta(float(valor_inicial))
        return conta

    def __cria_despesa(self):
        nome = str(input(f'→ Digite o nome da despesa: ')).strip()
        valor = float(input(f'→ Digite o valor da despesa: '))
        despesa = Despesa(nome, valor)
        return despesa

    def __remover_despesa_da_lista_e_conta(self, conta, lista):
        flag_removeu = False
        nome = str(input(f'→ Digite nome da despesa para remover: '))
        for despesa in lista.lista_despesas:
            if despesa.nome == nome:
                conta.remover_despesa_da_conta(despesa.valor)
                lista.remover_despesa_da_lista(despesa)
                print(f'• Despesa "{despesa.nome}" removida.')
                flag_removeu = True
        if flag_removeu == False:
            print(f'• Erro: despesa "{nome}" não encontrada.')

    def __criar_lista_despesas_para_impressao(self, lista):
        lista_impressao = []
        for despesa in lista.lista_despesas:
            string = str(f'• Despesa "{despesa.nome}": R$ {despesa.valor}\n')
            lista_impressao.append(string)
        return lista_impressao

    def __converter_float_em_string(self, conta):
        valor_inicial = str(conta.valor_inicial)
        saldo = str(conta.saldo)
        return valor_inicial, saldo

    def __criar_documento(self, lista_impressão, resultado_conversao):
        nome = str(input(f'→ Digite o nome do arquivo: '))
        with open(f'Documentos/{nome}.txt', "a") as arquivo:  # WITH: FECHA O DOCUMENTO APÓS OS CMDS
            arquivo.write(f'----- Lista "{nome}" -----\n')
            arquivo.write(f'• Valor inicial: R$ {resultado_conversao[0]}\n\n')
            for despesa in lista_impressão:
                arquivo.write(str(despesa))
            arquivo.write(f'\n• Valor disponível: R$ {resultado_conversao[1]}\n')
        print(f'• Documento "{nome}.txt" gerado na pasta "Documentos".')

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
                self.__remover_despesa_da_lista_e_conta(conta, lista)

            elif escolha == 5:
                conta.depositar_valor()
                conta.imprime_saldo()

            elif escolha == 6:
                lista_impressao = self.__criar_lista_despesas_para_impressao(lista)
                resultado_conversao = self.__converter_float_em_string(conta)
                self.__criar_documento(lista_impressao, resultado_conversao)

            elif escolha == 0:
                break
