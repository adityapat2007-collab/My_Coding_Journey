class Solution:
    def __init__(self,x,y,z):
        self.c1 = x
        self.c2 = y
        self.c3 = z
    def distance(self):
        dis_xz = abs(self.c1 - self.c3)
        dis_yz = abs(self.c2 - self.c3)
        if dis_xz < dis_yz:
            return 1
        elif dis_yz < dis_xz:
            return 2
        elif dis_xz == dis_yz:
            return 0
a=int(input('x = '))
b=int(input('y = '))
c=int(input('z = '))
obj1 = Solution(a,b,c)
print(obj1.distance())

'''a = int(input('x = '))
b = int(input('y = '))
c = int(input('z = '))
def distance(a,b,c):
    dis_xz = abs(a - c)
    dis_yz = abs(b - c)
    if dis_xz < dis_yz:
        return 1
    elif dis_yz < dis_xz:
        return 2
    elif dis_xz == dis_yz:
        return 0
print(distance(a,b,c))'''




