# 1. Elabore un programa en Python que permita convertir de pesos a dólares, de
# pesos a euros, de euros a pesos, de pesos a yenes. (10 ptos)
# 1 yen = 26.30 pesos
# 1 dólar = 3944 pesos
# 1 euro = 4279 pesos
import os,sys
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
            os.system('cls')
            menu()
    except KeyboardInterrupt:
        print('ERROR')
        os.system('pause')
        os.system('cls')
        menu()
    

    else:
        pass
    
    opt=input('Ingrese la opcion que desea realizar: /n1.Pesos a dolares: /n2. ' )
# funcionn principal
if __name__=='__main__':
    dolar=3944
    euro = 4279
    yen = 26.30
    varBool=True
    while varBool:
        opt=menu()
        if opt=='1':
            pesos=float(input('Ingrese la cantidad de pesos que desea convertir: '))
            pesosADolar= pesos/dolar
            print(f'La cantidad de {pesos} a dolar es de: {pesosADolar}')
            os.system('pause')
            os.system('cls')
        elif opt=='2':
            pesos=float(input('Ingrese la cantidad de pesos que desea convertir: '))
            pesosAEuro=pesos/euro
            print(f'La cantidad de {pesos} a Euros es de: {pesosAEuro}')
            os.system('pause')
            os.system('cls')
        elif opt=='3':
            Euro=float(input('Ingrese la cantidad de Euros que desea convertir: '))
            euroAPeso=Euro*euro
            print(f'La cantidad de {Euro} a Pesosr es de: {euroAPeso}')
            os.system('pause')
            os.system('cls')
        elif opt=='4':
            pesos=float(input('Ingrese la cantidad de pesos que desea convertir: '))
            pesosAYenes=pesos/yen
            print(f'La cantidad de {Euro} a Yenes es de: {pesosAYenes}')
            os.system('pause')
            os.system('cls')
        else:
            varBool=bool(input('Desea hacer otra conversion? s(si) enter(no)'))
            os.system('cls')

            




