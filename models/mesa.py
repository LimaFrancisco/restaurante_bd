from typing import Type          # O Type serve para especificar os tipos de dados
from .conta import Conta
from .pedido import Pedido

class Mesa:
    contador_mesa = 0            # Contador para dar valores distintos aos identificadores de mesa

    def __init__(self) -> Type[None]:
        Mesa.contador_mesa += 1                                  # Incrementeando o contador         
        self.__disponibilidade = True                            # O atributo de disponibilidade sempre comeca como True
        self.__nr_mesa = Mesa.contador_mesa                      # Numero da mesa recebe um valor unico
        self.__conta = Conta()                                   # Todaas as mesas possuem um atributo conta do Tipo Conta

    # Metodos que retornam os valores dos atributos
    def verificar_disponibilidade(self) -> Type[bool]:
        return self.__disponibilidade
    
    def retornar_nr_mesa(self) -> Type[int]:
        return self.__nr_mesa

    # Metodo para atribuir um novo pedido a conta
    def vincular_pedido(self, novo_pedido: Type[Pedido]) -> Type[None]:
        self.__conta.adicionar_pedido(novo_pedido)
        if self.__disponibilidade == True:
            self.__alterar_disponibilidade()

    # O metodo fechar conta zera todos os itens da contas
    def fechar_conta(self, forma_de_pagamento: Type[str]) -> Type[None]:
        self.__conta.fechar_conta(forma_de_pagamento)
        self.__alterar_disponibilidade()

    # Metodo para alterar a disponibilidade da mesa
    def __alterar_disponibilidade(self) -> Type[None]:
        if self.__disponibilidade == True:
            self.__disponibilidade = False
        else:
            self.__disponibilidade = True
