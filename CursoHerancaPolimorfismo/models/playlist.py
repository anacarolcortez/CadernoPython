class Playlist():

    def __init__(self, nome, midias):
        self.nome = nome
        self._midias = midias

    @property
    def midias(self):
        return self._midias

# Duck Typing

# Cria um metodo para tornar a classe um iteravel
    def __getitem__(self, item):
        return self._midias[item]

# Cria um metodo para retornar o tamanho da lista na classe
    def __len__(self):
        return len(self._midias)
