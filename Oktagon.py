#blazer-mot
#oktagon

import math
import matplotlib.patches
import matplotlib.pyplot as p
class Oktagon: 
    def __init__(self,side):
        self.side = side
        self.corner = 135
        self.k = 1 + math.sqrt(2)

    def plosh(self):
        self.square = 2 * self.side ** 2 * self.corner
        print (f"Площадь октагона равна {self.square}")
        
    def per(self):
        self.perimetr = 8 * self.side 
        print (f" Периметр октагона равен {self.perimetr}")
    
    def opisan_okr(self):
        self.opis_r = self.side * math.sqrt (self.k / (self.k - 1))
        self.opis_s = self.opis_r ** 2 * 3.14
        print (f"Радиус описанной окружности {self.opis_r}")
        print (f"Площадь описанной окружности {self.opis_s}")
    def vpisan_okr(self):
        self.vpis_r = math.sqrt(2) / 2 * self.side
        self.vpis_s = self.vpis_r ** 2 * 3.14
        print(f'Радиус вписанной окружности {self.vpis_r}')
        print(f'Площадь вписанной окружности {self.vpis_s}')
    def grafik(self): #выводим графики на экран
        self.square = 2 * self.k *self.side ** 2
        self.vpis_r = math.sqrt (self.square / 8 / (math.sqrt(2) - 1))
        self.opis_r = math.sqrt( self.square / 2 / math.sqrt(2))
        p.xlim(-20, 20)
        p.ylim(-20, 20)
        p.grid()
        axes = p.gca()
        polygon_1 = matplotlib.patches.Polygon([(self.vpis_r, self.side/2),  #создаем октагон
                                                (self.vpis_r, -self.side/2),
                                                (self.side/2, -self.vpis_r),
                                                (-self.side/2, -self.vpis_r),
                                                (-self.vpis_r, -self.side/2),
                                                (-self.vpis_r, self.side/2), 
                                                (-self.side/2, self.vpis_r), 
                                                (self.side/2, self.vpis_r)], 
                                                fill = False, color = 'red')
        circle1 = matplotlib.patches.Circle((0, 0), radius = self.opis_r, fill = False, color = 'yellow')  #описанная окружность
        circle2 = matplotlib.patches.Circle((0, 0), radius = self.vpis_r, fill = False, color = 'purple') #вписанная окружность
        axes.add_patch(circle1)
        axes.add_patch(circle2)
        axes.add_patch(polygon_1)
        p.show()
    def __del__(self): #деинициализация
        print ('Октагон удален')
            