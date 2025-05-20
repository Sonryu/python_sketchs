string = 'Luiz'
metodo = 'upper'
#print(string)

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('não existe o metodo', metodo)