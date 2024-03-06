# 4. Elabore un programa que permite registrar la información de los empleados
# De una compañía y le permita calcular el valor a pagar por concepto de nomina a
# Cada empleado. La información que se tiene por cada empleado es la siguiente (55ptos):

# id
# nombre
# cargo (Almacenista, Jefe IT, Administrador, Mensajero, Genrente)
# salario

# Para calcular el valor a pagar por cada empleado se debe tener en cuenta la
# Siguiente información:
# diasTrabajados
# horasExtras
# valorDia

# descuentoxCafeteria
# cuotaPrestamo

# El valor de la hora extra es de 5500 pesos. La información de la colilla de pago
# Se debe almacenar en caso de una solicitud de revisión por parte de algún
# Empleado que no este conforme con el pago la información que debe guardar
# La colilla de pago es la siguiente:

# mesPagado
# fechaPago(dd/mm/yyyy)
# sueldoBase
# valorTotalHrasExtras
# cuotaPrestamo
# descuentoxCafeteria
# totalAPagar

# La información se debe guardar en un archivo JSON.
# El gerente desea obtener la siguiente información:
# 1. Total pagado por concepto de nomina
# 2. Consultar la colilla de pago de un determinado empleado.
from menu import menu
from corefy import checkFile, readFile, updateFile,pause_screen, clear_screen
empleados={}
def regEmpleados():
    empleados=readFile('empleados.json')
    id=input('Ingrese el id del empleado')
    nombre=input('Ingrese el nombre del empleado')
    cargo=input('Ingrese el cargo del empleado')
    salario=float(input('Ingrese el salario del empleado'))

    empleado={
        'id':id,
        'nombre':nombre,
        'cargo':cargo,
        'salario':salario,
        'nomina':{}
    }
    empleados.update({id:empleado})
    updateFile('empleados.json',empleados)
    


def agrNomina():
    empleados=readFile('empleados.json')
    id=input('Ingrese el id del empleado para registro de nomina: ')
    mesPagado=input('Ingrese el mes ')
    fechaPago=input('Ingrese la fecha de pago: ')
    sueldoBase= empleados.get(id).get('salario')
    horasExtras=float(input('Ingrese el numero de horas extras trabajadas: '))
    diasTrabajados=float(input('Ingrese el numero de dias Trabajados'))
    valorTotalHrasExtras=horasExtras*5500
    cuotaPrestamo=float(input('Ingrese el valor de la cuota del prestamo :'))
    descuentoxCafeteria=float(input('Ingrese el valor total de gastos en cafeteria: '))
    
    totalAPagar= (((sueldoBase/30)* diasTrabajados)+valorTotalHrasExtras)-cuotaPrestamo-descuentoxCafeteria

    nomina={
        'mesPagado':mesPagado,
        'fechaPago':fechaPago,
        'sueldoBase':sueldoBase,
        'valorTotalHrasExtras':valorTotalHrasExtras,
        'cuotaPrestamo':cuotaPrestamo,
        'descuentoxCafeteria':descuentoxCafeteria,
        'totalAPagar':totalAPagar
    }
    empleados.get(id).get('nomina').update({mesPagado:nomina})
    updateFile('empleados.json',empleados)
    
def consultarPago():
    empleados=readFile('empleados.json')
    id = input('Ingrese el numero Id del empleado: ')
    mes= input('Ingrese el mes que desea consultar: ')
    pago=empleados[id]['nomina'][mes]['totalAPagar']
    print(f'El pago fue de: {pago}')
def consulNomina():
    empleados=readFile('empleados.json')
    id = input('Ingrese el numero Id del empleado: ')
    mes= input('Ingrese el mes que desea consultar: ')
    for key,valor in empleados[id]['nomina'][mes].items():
        print(f'{key}: {valor}')

if __name__=='__main__':
    checkFile('empleados.json',empleados)
    varBool=True
    while varBool:
        opt=menu()
        if opt=='1':
            regEmpleados()
            pause_screen()
            clear_screen()
        elif opt=='2':
            agrNomina()
            pause_screen()
            clear_screen()
        elif opt=='3':
            consultarPago()
            pause_screen()
            clear_screen()
        elif opt=='4':
            consulNomina()
            pause_screen()
            clear_screen()
        else:
            varBool=bool(input('Desea ver de nuevo el menu? s(si) enter(no)'))
        
    
   