class Playlist(list):
    # Herda da classe list para se tornar um objeto iteravel com propriedades de uma lista

    def __init__(self, nome, midias):
        self.nome = nome
        super().__init__(midias)
