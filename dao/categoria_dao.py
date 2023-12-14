from model.categoria import Categoria
from database.client_factory import ClientFactory


class CategoriaDAO:

    def __init__(self):
        self.__categorias: list[Categoria] = list()
        self.__client: ClientFactory = ClientFactory()

    def listar(self) -> list[Categoria]:
        categorias = list()

        client = self.__client.get_client()
        db = client.livraria
        for documento in db.categorias.find():
            cat = Categoria(documento['nome'])
            cat.id = documento['_id']
            categorias.append(cat)
        client.close()

        return categorias

    def adicionar(self, categoria: Categoria) -> None:
        client = self.__client.get_client()
        db = client.livraria
        db.categorias.insert_one({'nome': categoria.nome})
        client.close()

    def remover(self, categoria_id: int) -> bool:
        encontrado = False

        for c in self.__categorias:
            if (c.id == categoria_id):
                index = self.__categorias.index(c)
                self.__categorias.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if (c.id == categoria_id):
                cat = c
                break
        return cat

    def ultimo_id(self) -> int:
        index = len(self.__categorias) - 1
        if (index == -1):
            id = 0
        else:
            id = self.__categorias[index].id
        return id
