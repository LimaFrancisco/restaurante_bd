from typing import Type, List          # O Type serve para especificar os tipos de dados
from .mesa import Mesa
from .conta import Conta

class Atendente:
    contador_id_atendente = 0   # Contador para incrementar o id do atendente a cada objeto criado

    def __init__(self, nome: Type[str]) -> Type[None]:
        Atendente.contador_id_atendente += 1                   # Incrementando o contador para o id
        self.__id_atendente = Atendente.contador_id_atendente  # Adicionando um valor unico ao id 
        self.__nome = nome                                     # Atribudo para guardar o nome do atendente
        self.__mesas_responsaveis: Type[List[Mesa]] = []       # Lista de IDs de mesas que o atendente gerencia

    # Medotodos para retornar os dados dos atributos
    def retornar_id_atendente(self) -> Type[int]:
        return self.__id_atendente
    
    def retornar_nome(self) -> Type[None]:
        return self.__nome

    # Metodo para adiciona mesa a uma lista de mesas
    def adicionar_mesa(self, mesa: Type[Mesa]) -> Type[None]:
        if mesa not in self.__mesas_responsaveis:
            self.__mesas_responsaveis.append(mesa)

    # Metodo para remover mesa da lista mesas
    def remover_mesa(self, mesa: Type[Mesa]) -> Type[None]:
        if mesa in self.__mesas_responsaveis:
            self.__mesas_responsaveis.remove(mesa)

    # Metodo para criar uma conta
    def cria_conta(sefl) -> Type[Conta]:
        conta = Conta()
        return conta
