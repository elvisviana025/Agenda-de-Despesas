from Classes.Conta import Conta
from Classes.Despesa import Despesa

lista_despesas = []

conta = Conta(float(input(f'Digite o valor inicial: ')))

while True:
    escolha = int(input('Escolha a operação: [1] Saldo [2] + Despesa [3] - Despesa [4] Lista despesas [5] Deposita Valor [6] Sair\n->'))
    if escolha == 1:
        conta.imprime_valor()

    elif escolha == 2:
        despesa = Despesa()
        lista_despesas.append(despesa)
        conta.adicionar_despesa(despesa.get_valor())

    elif escolha == 3:
        nome = str(input(f'Digite nome da despesa para remover: '))
        for despesa in lista_despesas:
            if despesa.get_nome() == nome:
                conta.remover_despesa(despesa.get_valor())
                lista_despesas.remove(despesa)
                print(f'• Despesa "{despesa.get_nome()}" removida.')

    elif escolha == 4:
        if lista_despesas == []:
            print(f'Lista vazia')
        else:
            for despesa in lista_despesas:
                despesa.imprime_despesa()

    elif escolha == 5:
        conta.depositar_valor()

    elif escolha == 6:
        break

conta.imprime_valor()