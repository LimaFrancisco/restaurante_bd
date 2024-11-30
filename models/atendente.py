from typing import Type, List                #
from .mesa import Mesa

class Atendente:
    contador_id_atendente = 0

    def __init__(self, nome: Type[str]) -> Type[None]:
        Atendente.contador_id_atendente += 1
        self.__id_atendente = Atendente.contador_id_atendente
        self.__nome = nome
        self.__mesas_responsaveis: Type[List[Mesa]] = []  # Lista de IDs de mesas que o atendente gerencia

    def retornar_id_atendente(self) -> Type[int]:
        return self.__id_atendente
    
    def retornar_nome(self) -> Type[None]:
        return self.__nome

    def adicionar_mesa(self, mesa: Type[Mesa]) -> Type[None]:
        if mesa not in self.__mesas_responsaveis:
            self.__mesas_responsaveis.append(mesa)

    def remover_mesa(self, mesa: Type[Mesa]) -> Type[None]:
        if mesa in self.__mesas_responsaveis:
            self.__mesas_responsaveis.remove(mesa)
