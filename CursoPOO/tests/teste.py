#Arquivo apenas para confrontar Paradigma funcional x Paradigma POO
def criar_conta(numero, agencia, titular, limite):
    conta = {'numero': numero, 'agencia': agencia, 'titular': titular, 'limite': limite, 'saldo': limite }
    return conta

def depositar(conta, valor):
    conta['saldo'] = conta['saldo'] + valor

def sacar(conta, valor):
    conta['saldo'] = conta['saldo'] - valor

def imprimir_extrato(conta):
    print(f'Saldo atualizado: {conta["saldo"]}')
