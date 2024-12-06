from models.produto import Produto
from models.pedido import Pedido    
from models.conta import Conta
from models.mesa import Mesa
from models.atendente import Atendente

# Testando a classe Produto
produto1 = Produto("Hambúrguer", 15.00)
produto2 = Produto("Batata Frita", 8.00)
produto3 = Produto("Refrigerante", 5.00)

print(f"Produto 1: {produto1.exibir_nome()} - R$ {produto1.exibir_preco()}")
print(f"Produto 2: {produto2.exibir_nome()} - R$ {produto2.exibir_preco()}")
print(f"Produto 3: {produto3.exibir_nome()} - R$ {produto3.exibir_preco()}")

# Atualizando o preço de um produto
produto1.atualizar_preco(16.00)
print(f"Preço atualizado do Produto 1: R$ {produto1.exibir_preco()}")

# Testando a classe Pedido
pedido1 = Pedido()
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)
pedido1.adicionar_produto(produto3)

print(f"ID do Pedido 1: {pedido1.exibir_id()}")
print(f"Hora do Pedido 1: {pedido1.exibir_hora_pedido()}")
print("Comanda do Pedido 1:")
print(pedido1.exibir_comanda())

# Testando a classe Conta
conta1 = Conta()
conta1.adicionar_pedido(pedido1)
print("Nota fiscal da Conta 1:")
print(conta1.exibir_nota())

# Testando a classe Mesa
mesa1 = Mesa()
print(f"Número da Mesa: {mesa1.retornar_nr_mesa()}")
print(f"Disponibilidade inicial: {mesa1.verificar_disponibilidade()}")

# Vinculando pedido à mesa
mesa1.vincular_pedido(pedido1)
print(f"Disponibilidade após vincular pedido: {mesa1.verificar_disponibilidade()}")

# Fechando a conta da mesa
mesa1.fechar_conta("dinheiro")
print(f"Disponibilidade após fechar conta: {mesa1.verificar_disponibilidade()}")

# Testando a classe Atendente
atendente1 = Atendente("Carlos")
print(f"Atendente: {atendente1.retornar_nome()} (ID: {atendente1.retornar_id_atendente()})")
atendente1.adicionar_mesa(mesa1)
