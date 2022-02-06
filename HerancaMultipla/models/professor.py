from models.alura import Alura
from models.caelum import Caelum
from models.utils import Utils


class Professor(Alura, Caelum, Utils):

    def mostrar_tarefas(self):
        return super().mostrar_tarefas()

# Em Python2, a ordem de implementação de métodos será:
# Alura > Funcionario > Caelum > Funcionario

# Já em Python3, existe a MRO (remove duplicata na hierarquia de classes)
# Alura > Caelum > Funcionario
