import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def tuplas_longitud_onda(archivo):
    arreglo = []
    imprimir = False
    with open(archivo,'r') as archivo1:      

        for linea in archivo1:

            if linea == '    data: |\n':
                imprimir = True
            elif linea == '  - type: tabulated k\n':
                imprimir = False
            elif linea == 'SPECS:\n':
                imprimir = False
            elif imprimir:
                separacion = linea.split()
                a_float = [float(numero) for numero in separacion]
                arreglo.append(tuple(a_float))
    return arreglo

tuplas_plastico = tuplas_longitud_onda('./Plásticos/French.yml')
tuplas_plastico = tuplas_longitud_onda('./Combustible/Wang-20C.yml')




#Promedio n

def promedio(n:list):
    resultado = 0

    for promedio in n:
        resultado += promedio[1]
    resultado = resultado/len(n)
    return resultado

promedio_n = promedio(tuplas_plastico)

#Desviacion estandar de muestra
def desviacion_estandar(n:list, p):

    suma = 0
    for i in range(len(n)):
        resta = (n[i][1] - p)**2
        suma += resta
    division = suma/(len(n) - 1)
    raiz = division**(1/2)
    return raiz

desviacion_plastico = desviacion_estandar(tuplas_plastico, promedio_n)


#Grafica indice de refraccion
fig,ax = plt.subplots()
ax.set_title('Kapton')
rango = np.linspace(min([tuplas[0] for tuplas in tuplas_plastico]),max([tuplas[0] for tuplas in tuplas_plastico]),100)
ax.plot(rango,np.full_like(rango,promedio_n),color='r',label = 'promedio')
ax.plot(rango,np.full_like(rango,promedio_n - desviacion_plastico),color='k',label = 'Desviacion estandar')
ax.plot(rango,np.full_like(rango,promedio_n + desviacion_plastico),color='k',label = 'Desviacion estandar')
ax.scatter([tuplas[0] for tuplas in tuplas_plastico],[tuplas[1] for tuplas in tuplas_plastico])
ax.legend()
plt.savefig('Kapton.png')


lista_elementos = pd.read_csv('./indices_refraccion.csv')

#Funcion en general
def funcion_general(lista_elementos:pd.DataFrame):

    


    for i in range(len(lista_elementos)):
        arreglo_general = tuplas_longitud_onda(lista_elementos.iloc[i][0] + '/' + lista_elementos.iloc[i][3].split('/')[-1])
        promedio_general = promedio(arreglo_general)
        desviacion_estandar_general = desviacion_estandar(arreglo_general,promedio_general)
        

        #Graficar y guardar en cada uno
        fig,ax = plt.subplots()
        ax.set_title(lista_elementos.iloc[i][0])
        rango = np.linspace(min([tuplas[0] for tuplas in arreglo_general]),max([tuplas[0] for tuplas in arreglo_general]),100)
        ax.plot(rango,np.full_like(rango,promedio_general),color='r',label = 'promedio')
        ax.plot(rango,np.full_like(rango,promedio_general - desviacion_estandar_general),color='k',label = 'Desviacion estandar')
        ax.plot(rango,np.full_like(rango,promedio_general + desviacion_estandar_general),color='k',label = 'Desviacion estandar')
        ax.scatter([tuplas[0] for tuplas in arreglo_general],[tuplas[1] for tuplas in arreglo_general])
        ax.legend()
        plt.savefig(lista_elementos.iloc[i][0] + '/' + lista_elementos.iloc[i][2] +'.png')
        plt.close()

funcion_general(lista_elementos=lista_elementos)       

        

       




        


   
