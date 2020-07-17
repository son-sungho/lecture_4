import math
class Circle:
    def __init__(self, name ,radius, PI):
        self.name = name
        self.radius = radius
        self.pI = PI

        def area(self):
            return self.PI * self.radius **2
            def __del__(self):
                pass


c1 = Circle("원", 4, math.pi)
c1.area()
# print("c1의 면적:", c1.area())
c2 = Circle("원", 200, math.pi)
print("c2의 면적{}".format( c2.area()))
# c3 = Circle("c3", 5, 3.1415)
# print("c3의 면적:", c3.area())
print(c1.__dict__)
