import matplotlib.pyplot as plt
import numpy as np


class Mineral:
    def __init__(self, nombre, dureza, rompimiento_por_fractura, color,
                 composicion, lustre, specific_gravity, sistema_cristalino):
        self.nombre=nombre
        self.dureza=dureza
        self.rompimiento_por_fractura=rompimiento_por_fractura
        self.color=color
        self.composicion=composicion
        self.lustre=lustre
        self.specific_gravity=specific_gravity
        self.sistema_cristalino=sistema_cristalino
        
        
    def silicato(self):
        resp=False
        h=self.composicion
        if ("O" in h) and ("Si" in h):
            resp=True
            
        return resp
    
    def densidad(self):
        dense=float(self.specific_gravity)*1000
        return dense
    
    def colores(self):
        plt.pie([1], labels=[self.nombre], colors=[self.color], radius=1.5)
        plt.show()
        
    def datos(self):
        print(self.dureza)
        print(self.rompimiento_por_fractura)
        print(self.sistema_cristalino)
            

        





        


        




    