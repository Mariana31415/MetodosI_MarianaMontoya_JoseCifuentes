from mineral import Mineral
import matplotlib.pyplot as plt
import numpy as np




#Carga de datos

def cohef_expansion(ruta):
       
    file = open(ruta)
    datos = file.readlines()
    file.close()
    
    volumen=[]
    temperatura=[]

    for i in datos:
        linea=i.strip().split(",")
        if  linea[1]=="volume_cc":
            pass
        else:
            volumen.append(float(linea[0]))
            temperatura.append(float(linea[1]))
        
    #Calculo de coheficiente de expansión para un valor medio de la temperatura
    coef=[]
    tmedia=[]
    for i in range(len(volumen)-1):
        valor_coef=(1/volumen[i])*(volumen[i+1]-volumen[i])/(temperatura[i+1]-temperatura[i])
        new_temp=(temperatura[i+1]+temperatura[i])/2
    
        tmedia.append(new_temp)
        coef.append(valor_coef)
    
    #Presentación por terminal
    plt.scatter(temperatura,volumen)
    plt.xlabel('Temperatura',fontsize=15)
    plt.ylabel('Volumen',fontsize=15)
    plt.show()

    #Calculo error
    error=np.std(coef)/np.sqrt(len(coef))

    print("El coheficiente de expansión es:",round(np.mean(coef),2), "\t El error es de",error)    
    plt.scatter(tmedia,coef, color="red")
    plt.xlabel('Temperatura',fontsize=15)
    plt.ylabel('Coheficiente\n de expansión',fontsize=15)
    plt.show()

    
    
        
                
        
        