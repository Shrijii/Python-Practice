import math


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def cal_area(self):
        x= math.pi*self.radius**2
        print("area of circle is : ", x)
    def cal_circum(self):
        x=2*math.pi*self.radius
        print("circumference of circle is :" ,x)

a= int(input("enter radius :"))
e=Circle(a)
e.cal_circum()
e.cal_area()