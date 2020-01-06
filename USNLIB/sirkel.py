import math # Importerer matte biblioteket
class SIRKEL():
    """Klasse beregning av et sirkulært areal
    param: radius: sirkelsens radius
    :type  radius: float
    """    

    def __init__(self,radius):
        self.radius=radius

    radius=0.0
    """ Sirkelens radius
    :type radius: float 
    """

    def getAreal(self):
        "Beregner arealet til en sirkel"
        return self.radius*self.radius*math.pi
    
if __name__ == '__main__':
    sirkel1=SIRKEL(12.0)
    areal=sirkel1.getAreal()
    print("Arealet av en sirkel med R=",sirkel1.radius," er ", areal)
        
        
    