from Classes.Conta import Conta
from Classes.Lista_despesas import Lista_despesas
from Classes.Sistema import Sistema

# INICIALIZA OBJETOS
sistema = Sistema()
lista_despesas = Lista_despesas()

# EXECUTA MÉTODOS
sistema.imprime_texto_inicial()
conta = sistema.cria_conta()
sistema.filtra_menu(lista_despesas, conta)