def divide(n,d):
    if d == 0:
        raise ZeroDivisionError("Voce esta tentand dividir por 0")
    return n/d




print(divide(8, 0))