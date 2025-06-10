import copy

from dados import produtos

reverse = True

novos_produtos = [
    {**p, 'preco': round(p['preco']* 1.1, 2 )}
    
    for p in copy.deepcopy(produtos)
    
    ]


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['nome']
)


produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['preco']
)
print()
print('ORIGINAL')
print()
print(*novos_produtos, sep='\n')
print()
print('ADICIONAL DE 10%')
print()
print(*produtos, sep='\n')
print()
print('ORDENAR MENOR-MAIOR')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()


print('ORDENAR MAIOR-MENOR')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()