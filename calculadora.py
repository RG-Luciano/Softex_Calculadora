numero1 = float(input("digite o numero "))
numero2 = float(input("digite o numero "))
entrada = int(input("digite a operação "))
def operacao(numero1, numero2, entrada):
    if(entrada == 1):
        print(numero1 + numero2)
    elif(entrada == 2):
        print(numero1 - numero2)
    elif(entrada == 3):
        print(numero1 * numero2)  
    elif(entrada == 4):
        print(numero1 / numero2)      
    else:
        print("0")
operacao(numero1, numero2, entrada)