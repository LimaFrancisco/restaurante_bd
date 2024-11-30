from typing import Type          # O Type serve para especificar os tipos de dados
from datetime import datetime    # O datetime captura a data e a hora atual do sistema
from .produto import Produto

class Pedido:
    contador_pedido_id = 0       # Contador para dar valores distintos as ids de diferentes pedidos

    def __init__(self) -> Type[None]:
        Pedido.contador_pedido_id += 1                                  # Incrementeando o contador         
        self.__id_pedido = Pedido.contador_pedido_id                    # Dando um valor unico ao id do pedido 
        self.__hora_pedido = datetime.now().time().strftime("%H:%M:%S") # Atributos que guarda o horario que foi realizado o pedido
        self.__produtos = []                                            # Lista de produtos

    # Metodos que retornam dados dos atributos
    def exibir_id(self) -> Type[int]:
        return self.__id_pedido
    
    def exibir_hora_pedido(self) -> Type[str]:
        return self.__hora_pedido

    # Retorna o valor total do pedido
    def retornar_total(self) -> Type[float]:
        total = 0
        for item in self.__produtos:
            total += item.exibir_preco()

        return total

    # Adiciona um novo produto a lista de produtos
    def adicionar_produto(self, novo_produto: Type[Produto]) -> Type[None]:
        self.__produtos.append(novo_produto)

    # Retorna uma comanda com todos os itens do pedido
    def exibir_comanda(self) -> Type[str]:
        dados = self.__retornar_apenas_dados_do_pedido()
        dados += self.__retornar_dados_produtos()
        dados += self.__retornar_total_formatado()
        return dados

    # Metodos com toda a logica para o metodo que retorna a nota do pedido
    def __retornar_apenas_dados_do_pedido(self) -> Type[str]:
        dados = '------------- DADOS DO PEDIDO -------------'
        dados += f'\nID DO PEDIDO: # {self.__id_pedido}'
        dados += f'\nHORA DO PEDIDO: # {self.__hora_pedido}\n'
        return dados

    def __retornar_dados_produtos(self) -> Type[str]:
        produtos_consolidados = {}
        for item in self.__produtos:
            nome = item.exibir_nome()
            preco_unitario = item.exibir_preco()

            if nome in produtos_consolidados:
                produtos_consolidados[nome]['quantidade'] += 1
            else:
                produtos_consolidados[nome] = {
                    'quantidade': 1,
                    'preco_unitario': preco_unitario,
                }

        dados = '\n----------------- PRODUTOS ----------------'
        for nome, info in produtos_consolidados.items():
            quantidade = info['quantidade']
            preco_total = quantidade * info['preco_unitario']
            dados += f'\n{nome + ' ':-<31} {quantidade}X R$ {preco_total:.2f}'

        return dados
    
    def __retornar_total_formatado(self) -> Type[str]:
        dados = '\n\n' + ('-' * 43)
        dados += f'\n{'TOTAL: ':-<34} R$ {self.retornar_total():.2f}'
        return dados
