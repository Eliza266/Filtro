import json,os
BASE='ejercicio3/data/'

def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE+ archivo))):
        with open(BASE + archivo,'w') as bw:
            json.dump(data,bw,indent=4)

def readFile(archivo:str):
    with open(BASE + archivo,'r') as br:
        inventario=json.load(br)
    return inventario
    
def updateFile(archivo:str,data): 
    with open(BASE + archivo,'w') as bf:
        json.dump(data,bf,indent=4)