import matplotlib.pyplot as plt

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
#tuplas_plastico = tuplas_longitud_onda('./Combustible/Wang-20C.yml')

#Grafica indice de refraccion
fig,ax = plt.subplots()
ax.set_title('Kapton')
ax.scatter([tuplas[0] for tuplas in tuplas_plastico],[tuplas[1] for tuplas in tuplas_plastico])

#Promedio n
resultado = 0
for promedio in tuplas_plastico:
    resultado += promedio[1]
resultado = resultado/len(tuplas_plastico)
print(resultado)

#Desviacion estandar



plt.savefig('Kapton.png')

