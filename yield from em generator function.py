# Yield from
def gen1():
    
    print('começou GEN-1')
    yield 1
    yield 2
    yield 3
    print('acabou GEN-1')

def gen2():
    print('começou GEN-2')
    yield 4
    yield 5
    yield 6
    print('acabou GEN-2')
def gen3(gen):
    print('começou GEN-2')
    yield from gen()
    yield 40
    yield 50
    yield 60
    print('acabou GEN-3')

g = gen3(gen1)
g2 = gen3(gen2)

for numero in g:
    print(numero)

for numero in g2:
    print(numero)
    