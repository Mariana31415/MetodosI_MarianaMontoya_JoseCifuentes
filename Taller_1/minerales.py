
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
        ox="O" in self.composicion
        si="Si" in self.composicion
        resp=False
        if ox==True and si==True:

            resp=True
            
        return resp
            
        
papa=Mineral()
        

"""""
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print("Hola, mi nombre es", self.nombre)
    def años(self):
        print("Mi edad es", self.edad)
         

p=persona("Juan", 38)
p.años()
"""



        


        




    