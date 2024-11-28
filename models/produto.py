from typing import Type           # O Type serve para especificar os tipos de dados

class Produto:
    contador_produto_id = 0       # Contador para dar valores distintos as ids de diferentes produtos

    def __init__(self, nome_produto: Type[str], preco_produto: Type[float]) -> Type[None]:
        Produto.contador_produto_id += 1                      # Incrementeando o contador
        self.__id_produto = Produto.contador_produto_id       # Dando um valor unico ao id do produto
        self.__nome_produto = nome_produto                    # Atributo que guarda o nome do produto
        self.__preco_produto = preco_produto                  # Valor do produto

    # Metodos para exibir os valores das variaveis 
    def exibir_id(self) -> Type[int]:
        return self.__id_produto

    def exibir_nome(self) -> Type[str]:
        return self.__nome_produto

    def exibir_preco(self) -> Type[float]:
        return self.__preco_produto

    # Metodo para modificar o valor do produto
    def atualizar_preco(self, novo_preco: Type[float]) -> Type[None]:
        self.__preco_produto = novo_preco
