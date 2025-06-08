#o primeiro modulo é __main___


import recurso_modularizacao

try:
    import sys
    sys.path.append('/home')

except ModuleNotFoundError:
    ...

print("Este modulo se chama: ", __name__)

print(*sys.path, sep='\n')
