# Elabore un programa en Python que permita registrar los productos de una
# Tienda de viveres. La información se debe almacenar en un archivo JSON. La
# Información de los productos es la siguiente (20ptos):

# id
# nombre
# valorUnitario
# stockmin
# stockmax
# valorUnitario
from corefy import checkFile, readFile, updateFile
inventario={

}

if __name__=='__main__':
    checkFile('inventario.json',inventario)

    Inventario= readFile('inventario.json')
    id=input('Ingrese el id del producto: ')
    nombre=input('Ingrese el nombre del producto: ')
    valorUnitario=input('Ingrese el valor del producto: ')
    stockmin=input('Ingrese el stock minimo del producto: ')
    stockmax=input('Ingrese el stock maximo del producto: ')
    valorVenta=input('Ingrese el valor de Venta del producto: ')

    producto={
        'id':id,
        'nombre':nombre,
        'valorUnitario':valorUnitario,
        'stockmin':stockmin,
        'stockmax':stockmax,
        'valorVenta':valorVenta
    }
    Inventario.update({id:producto})
    updateFile('inventario.json',Inventario)
    
