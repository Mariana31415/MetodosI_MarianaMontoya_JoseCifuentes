import matplotlib.pyplot as plt
import numpy as np


class Mineral:
    def __init__(self, nombre, dureza, lustre,rompimiento_por_fractura,
                 color, composicion, sistema_cristalino, specific_gravity):
        self.nombre=nombre
        self.dureza=dureza
        self.lustre=lustre
        self.rompimiento_por_fractura=rompimiento_por_fractura
        self.color=color
        self.composicion=composicion
        self.sistema_cristalino=sistema_cristalino
        self.specific_gravity=specific_gravity
        
    def silicato(self):
        resp=False
        if ("ox" in self.composicion) and ("si" in self.composicion):
            resp=True
            
        return resp
    
    def densidad(self):
        dense=self.specific_gravity*1000
        return dense
    
    def colores(self):
        plt.pie([1], labels=[self.nombre], colors=[self.color], radius=1.5)
        plt.show()
        
    def datos(self):
        print(self.dureza)
        print(self.rompimiento_por_fractura)
        print(self.sistema_cristalino)
            

        





        


        




    