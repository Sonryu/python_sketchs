def fora(x):
    a = x
    def dentro():
        #print(locals())
        print(dentro.__code__.co_freevars) 
        return a #variavel dentro
    
    return dentro()


dentro1 = fora(10)

dentro2 = fora(20)

print(dentro1)
print(dentro2)


def concatentar(string_inicial):
    
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    
    return interna

c = concatentar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c
print(final)