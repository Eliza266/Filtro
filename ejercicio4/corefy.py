import json,os,sys

BASE='ejercicio4/data/'
def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo,'w') as bw:
            json.dump(data,bw,indent=4)

def readFile(archivo:str):
    with open(BASE + archivo,'r') as br:
        empleados=json.load(br)
    return empleados
    
def updateFile(archivo:str,data): 
    with open(BASE + archivo,'w') as bf:
        json.dump(data,bf,indent=4)