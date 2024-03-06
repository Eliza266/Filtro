# 1. Elabore un programa en Python que permita convertir de pesos a dólares, de
# pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
# 1 yen = 26.30 pesos
# 1 dólar = 3944 pesos
# 1 euro = 4279 pesos
import os
#funcion menu
def menu():
    listaMenu=['1','2','3','4','5']
    titulo="""
       CONVERSOR DE MONEDA
    ************************
    """
    print(titulo)
    try:
        opt=input('Ingrese el numero de la opcion que desea realizar: \n1.Pesos a dolares: \n2.Pesos a euros: \n3.Euros a Pesos: \n4Pesos a Yenes: \n5.Salir  ' )
    
        if opt in listaMenu:
            return opt
        else: 
            print('Opcion Incorrecta')
            os.system('pause')
            os.system('pause')
            menu()
    except ValueError:
        print('Opcion Incorrecta')
        menu()
    

    else:
        pass
    
    opt=input('Ingrese la opcion que desea realizar: /n1.Pesos a dolares: /n2. ' )
# funcionn principal
if __name__=='__main__':
    
    opt=menu()
    dolar=3944
    euro = 4279
    yen = 26.30

    pesos=float(input('Ingrese la cantidad de pesos que desea convertir: '))
    Euro=float(input('Ingrese la cantidad de pesos que desea convertir: '))
    pesosADolar= pesos/dolar

    pesosAEuro=pesos/euro

    euroAPeso=Euro*euro

    pesosAYenes=pesos/yen



