from modelos.cardapio.ItemCardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
   def __init__(self, nome, preco, descricao):
      super().__init__(nome, preco)
      self.descricao = descricao