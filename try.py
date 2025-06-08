try:
    print(1)
    print("open")
    #8/0
except ZeroDivisionError:
    print("DIVIDIU ZERO")

else:
    print("Não deu erro!")

finally:
    print(2)
    print("fechar")