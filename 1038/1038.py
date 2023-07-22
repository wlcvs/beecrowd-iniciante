item_quantidade = list(map(lambda x: int(x), list(filter(lambda x: x is not " ", list(input())))))

'''

codigo especificação   preço
1      Cachoro quente  R$ 4.00
2      X-Salada        R$ 4.50
3      X-Bacon         R$ 5.00
4      Torrada simples R$ 2.00
5      Refrigerante    R$ 1.50

'''

cardapio_codigo_valor = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

total = cardapio_codigo_valor[item_quantidade[0]] * item_quantidade[1]

print(f"Total: R$ {total:.2f}")
