from typing import Type          # O Type serve para especificar os tipos de dados
from .pedido import Pedido

class Conta:
    contador_conta_id = 0       # Contador para dar valores distintos as ids de diferentes contas

    def __init__(self) -> Type[None]:
        Conta.contador_conta_id += 1                                  # Incrementeando o contador         
        self.__id_conta = Conta.contador_conta_id                     # Dando um valor unico ao id da conta
        self.__valor = 0                                              # Atributo que guarda o valor da conta
        self.__pedidos = []                                           # Lista de pedidos

    # Metodos que retornam dados dos atributos
    def retornar_id_conta(self) -> Type[int]:
        return self.__id_conta
    
    def retornar_valor(self) -> Type[float]:
        return self.__valor

    # Metodo responsavel por pagar a conta
    def fechar_conta(self, forma_de_pagamento: Type[str]) -> Type[None]:
        if self.__verificar_forma_pagamento(forma_de_pagamento):
            self.__pedidos.clear()
            self.__valor = self.__calcular_valor_conta()
    
    # Acrecenta um pedido a lista de pedidos
    def adicionar_pedido(self, novo_pedido: Type[Pedido]) -> Type[None]:
        self.__pedidos.append(novo_pedido)
        self.__valor = self.__calcular_valor_conta()

    # Atualiza o valor do atribudo valor
    def __calcular_valor_conta(self) -> Type[float]:
        valor_conta = 0
        for pedido in self.__pedidos:
            valor_conta += pedido.retornar_total()

        return valor_conta
    
    def exibir_nota(self) -> Type[str]:
        nota = self.__retornar_dados_nota()
        nota += self.__retornar_dados_pedidos()
        nota += self.__retornar_total_formatado()
        return nota
    
    # Metodos com funcionalidades para o metodo exibir_nota()
    def __retornar_dados_nota(self) ->Type[str]:
        cabecalho = '--------------- NOTA FISCAL ---------------'
        cabecalho += f'\nID DA CONTA: # {self.retornar_id_conta()}\n\n'
        return cabecalho 
    
    def __retornar_dados_pedidos(self) -> Type[str]:
        dados_pedidos = ''
        for pedido in self.__pedidos:
            dados_pedidos += pedido.exibir_comanda()
            dados_pedidos += '\n\n' + ('-' * 43) + '\n\n'

        return dados_pedidos

    def __retornar_total_formatado(self) -> Type[str]:
        total_formatado = '\n' + (43 * '-') + '\n'
        total_formatado += f'\n{'TOTAL CONTA: ':-<34} R$ {self.__valor:.2f}\n'
        return total_formatado

    # Metodo que verica o tipo do pagamento e retorna uma variavel boleana
    def __verificar_forma_pagamento(self, forma_pagamento: Type[str]) -> Type[bool]:
        forma_pagamento = forma_pagamento.upper()
        if forma_pagamento in ['DINHEIRO', 'DEBITO', 'CREDITO', 'PIX']:
            return True
        else:
            return False