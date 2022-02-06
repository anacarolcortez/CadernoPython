class Midia:

    def __init__(self, titulo, ano):
        self._titulo = titulo
        self._ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'Título: {self.titulo} - Ano: {self.ano} - Likes: {self.likes}'

    @property
    def likes(self):
        return self._likes

    @property
    def titulo(self):
        return self._titulo.title()

    @property
    def ano(self):
        return self._ano
