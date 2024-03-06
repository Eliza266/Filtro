# 2. Elabore un programa en Python que permita leer la información de un usuario
# Y la almacene en un diccionario. La información del usuario es la siguiente(15 ptos):
# id
# nombres
# apellidos
# ubicación
# dirección
# ciudad
# longitud
# latitud
# email
# edad
# ocupación
import os
if __name__=='__main__':
    id=input('Ingrese el numero Id: ')
    nombres=input('Ingrese los nombres: ')
    apellidos=input('Ingrese los apellidos: ')
    ubicación=input('Ingrese la ubicacion')
    dirección=input('Ingrese la direccion: ')
    ciudad=input('Ingrese la ciudad: ')
    longitud=input('Ingrese la longitud: ')
    latitud=input('Ingrese la latitu: ')
    email=input('Ingrese la email: ')
    edad=input('Ingrese la edad: ')
    ocupación=input('Ingrese la ocupacion')

    InfoUsuario={
       ' id':id,
        'nombres': nombres,
        'apellidos': apellidos,
       ' ubicación': ubicación,
        'dirección': dirección,
        'ciudad': ciudad,
        'longitud': longitud,
        'latitud':latitud,
       ' email': email,
        'edad': edad,
        'ocupación': ocupación
        
    }
    os.system('pause')
    os.system('cls')
    for i,valor in InfoUsuario.items():
        print(f'{i} : {valor}')


