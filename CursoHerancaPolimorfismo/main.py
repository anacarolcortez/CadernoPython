from models.filme import Filme
from models.playlist import Playlist
from models.serie import Serie

if __name__ == "__main__":
    dogville = Filme("dogville", 2003, 177)
    relatos_selvagens = Filme("relatos selvagens", 2014, 122)
    as_horas = Filme("as horas", 2002, 117)
    para_sempre_alice = Filme("para sempre alice", 2015, 101)
    mais_estranho_que_a_ficcao = Filme("Mais Estranho que a Ficção", 2006, 115)

    the_good_place = Serie("the good place", 2016, 5)
    master_of_none = Serie("master of none", 2015, 3)
    dark = Serie("dark", 2017, 3)
    gracie_and_frankie = Serie("gracie and frankie", 2015, 7)
    unbreakable_ks = Serie("unbreakable kimmy schmidt", 2015, 4)

    midias = [dogville, relatos_selvagens, as_horas, para_sempre_alice, mais_estranho_que_a_ficcao,
              the_good_place, master_of_none, dark, gracie_and_frankie, unbreakable_ks]

    favoritos = Playlist("favoritos", midias)

    for midia in favoritos:
        midia.dar_likes()
        print(midia)

    print(f'Tamanho da lista de favoritos: {len(favoritos)}')
