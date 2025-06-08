import importlib

import modulos

for i in range(10):
    importlib.reload(modulos)
    print(i)

print('fim')