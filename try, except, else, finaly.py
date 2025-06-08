#try, except, else e finaly
a = 18
b = 0

#c = a / b #ele n vai funcionar


try: 
    #a = 18

    print(b[0])
    print('linha 1'[1000])
    c = a / b #Mas, aqui ele "funciona" (ele vai tentar, se n conseguir ele vai pra o proximo.)
    print("linha 2")
#basicamente o erro esta silenciado.
except ZeroDivisionError:
    print("dividiu por 0.")

except NameError:
    print("Nome 'b' não esta definido.")

except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
    
except Exception:
    print("ERRO DESCONHECIDO")

print("CONTINUAR")