import tabulate
from mineral import Mineral

minerales=[]
obj_mineral=[]

#Carga de datos
file = open(r"Taller_1-parte_dos\minerales.txt")
lineas = file.readlines()
file.close()


for i in lineas:
    linea=i.strip().replace("\t",",").split(",")
    minerales.append(linea)   
minerales.remove(minerales[0])


#Carga de los objetos
for mineral in minerales: 
    nombre = mineral[0]
    dureza = mineral[1]
    rompimiento_por_fractura = mineral[2]
    color = mineral[3]
    composicion = mineral[4]
    lustre = mineral[5]
    specific_gravity = mineral[6]
    sistema_cristalino = mineral[7]
    
    mineral_i=Mineral(nombre=nombre, dureza=dureza, rompimiento_por_fractura=rompimiento_por_fractura,
                      color=color, composicion=composicion, lustre=lustre, 
                      specific_gravity=specific_gravity, sistema_cristalino=sistema_cristalino)
    
    
    obj_mineral.append(mineral_i)
    

#Funciones
def num_silicatos():
    contador=0
    for i in obj_mineral:
        if i.silicato():
            contador+=1
    return contador

def densidad_prom():
    suma=0
    for i in obj_mineral:
        suma+=i.densidad()
    
    prom=suma/len(obj_mineral)
    return round(prom,3)