'''
codigo especificação   preço
1      Cachoro quente  R$ 4.00
2      X-Salada        R$ 4.50
3      X-Bacon         R$ 5.00
4      Torrada simples R$ 2.00
5      Refrigerante    R$ 1.50
'''

class Cardapio:
    def __init__(self):
            self.cardapio_codigo_valor = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
            self.item = 0
            self.quantidade = 0

    def get_item_quantidade(self):        
        item_quantidade = list(map(lambda x: int(x), filter(lambda x: x != " ", list(input()))))        
        self.item = item_quantidade[0]
        self.quantidade = item_quantidade[1]

    def total(self):
        return self.cardapio_codigo_valor[self.item] * self.quantidade

cardapio = Cardapio()
cardapio.get_item_quantidade()

print(f"Total: R$ {cardapio.total():.2f}")
