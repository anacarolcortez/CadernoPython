from models.midia import Midia


class Serie (Midia):

    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f'Título: {self.titulo} - Ano: {self.ano} - Temporadas: {self._temporadas} - Likes: {self.likes}'
