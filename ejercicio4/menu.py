from corefy import pause_screen, clear_screen
def menu():
    listaMenu=['1','2','3','4','5']
    titulo="""
       BD PAGOS EMPLEADOS
    ************************
    """
    print(titulo)
    try:
        opt=input('Ingrese el numero de la opcion que desea realizar: \n1.Agregar Empleado: \n2.Agregar nomina: \n3.Consultar colilla de pago: \n4.Consultar nomina: \n5.Salir\n -  ' )
        if opt in listaMenu:
            return opt
        else: 
            print('Opcion Incorrecta')
            pause_screen()
            clear_screen()
            menu()
    except KeyboardInterrupt:
        print('ERROR')
        pause_screen()
        clear_screen()
        menu()
    

    else:
        pass
    