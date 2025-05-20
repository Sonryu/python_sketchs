produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'escritorio',
}

print(produto.items())


for chave, valor in produto.items():
    ...


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}



lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]


#dc = {
#    chave: valor
#      for chave, valor in lista
    
#}

#print(dict(lista))

s1 = {2 ** i for i in range (10)}

print(s1)

