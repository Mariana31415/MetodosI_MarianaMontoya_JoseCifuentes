import numpy as np
import matplotlib.pyplot as plt

#aproximar raices 

def f(x):
    return 

def f_prima(x):
    return 3*x**5 + 5*x**4 - x**3

def tan(pendiente,x1,y1,x):
    return 15*x**4 + 20*x**3 - 3*x**2


def hallar_raices(funcion,x1,derivada,tan):
    it = 50
    error = 1 * 10**(-5)
    j = 0
    Xn_1 = x1
    dominio = np.linspace(-2,2,100)

    grafica = funcion(dominio)
    while j < it or abs(funcion(Xn_1)) > error:
        Xn = Xn_1 - funcion(Xn_1)/derivada(Xn_1)
        j =  j + 1
        Xn_1 = Xn
        print(f"iteracion:{j}\nXn: {Xn}\nfuncion: {funcion(Xn_1)}\n")


        plt.plot(dominio,grafica)
        plt.plot(Xn,0,c = 'red', marker = '*')
        plt.plot(dominio,tan(derivada(Xn_1),Xn_1,funcion(Xn_1),dominio))
        plt.grid()
        plt.show()
hallar_raices(f,3,f_prima,tan) 

