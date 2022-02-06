from models.midia import Midia


class Filme (Midia):

    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self._duracao = duracao

    def __str__(self):
        return f'Título: {self.titulo} - Ano: {self.ano} - Duração: {self._duracao}min - Likes: {self.likes}'
