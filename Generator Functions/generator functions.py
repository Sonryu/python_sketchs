### INTRODUÇÃO ÀS GENERATOR FUNCTIONS EM PYTHON

generator = (n for n in range(1000))

def generator(n=0, maximum=10):
    while True:
        yield n
        
        n += 1

        if n > maximum:
            return

        


#def generator(n=0, maximum=10):
#    yield 1 # Pausar
  #  print('continuando...')
 #   yield 2 # Pausar
#    print('continuando outra vez...')
  #  yield 3 # Pausar
 #   print('vou terminar...')
#    return 'ACABOU'

gen = generator(n=5, maximum=8)

for n in gen:
    print(n)