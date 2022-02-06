from models.conta import *

if __name__ == '__main__':
    ana = Conta(123, '001', 'Ana', 1000.0)
    print(ana)
    ana.depositar(500.0)
    ana.sacar(50.0)
    ana.imprimir_extrato()

    carol = Conta(321, '001', 'Carol', 0.0)
    carol.imprimir_extrato()

    ana.transferir(100.0, carol)
    ana.imprimir_extrato()
    carol.imprimir_extrato()

    print(Conta.dados_banco())