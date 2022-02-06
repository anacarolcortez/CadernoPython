class Conta:
    #funcao construtora (__init__)
    def __init__(self, numero, agencia, titular, limite):
        self.__numero = numero,
        self.__agencia = agencia,
        self.__titular = titular,
        self.__limite = limite,
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        if valor <= self.saldo + self.saldo:
            return True
        else:
            return False

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor

    def imprimir_extrato(self):
        print(f'Saldo atualizado: {self.saldo}')

    def transferir(self, valor, destino):
        if self.saldo > valor:
            self.sacar(valor)
            destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novoLimite):
        self.__limite = novoLimite

    @staticmethod
    def dados_banco():
        return "Bytebank Ltda - contato@bytebank.com"