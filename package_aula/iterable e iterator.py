import sys

iterable = ['Eu', 'Tenho', '__iter__']

#iterator = iterable.__iter__() #tem __iter__ e __next__

iterator = iter(iterable)
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(generator))

print(sys.getsizeof(lista))

for i in range(10):
    print(next(generator))