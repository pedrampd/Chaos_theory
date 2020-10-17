import numpy as np
import cv2 


def fx(x, y , t):
    return (-(t**2) - (x*y) + t)

def fy(x, y, t):
    return(-(x * y) + (x*t) + y + t)

class Point:
    def __init__(self, x, y, t, color):
        self.x = x
        self.y = y
        self.t = t
        self.r = 3
        self.color = color
    def update (self, x, y):
        self.x = x
        self.y = y
        
    def get_next(self, fx, fy , t):
        x = fx(self.x, self.y, t)
        y = fy(self.x, self.y, t)
        return (x,y)
    
    
class Points:
    def __init__(self):
        self.history = []
    def add_point(self,Point):
        if len(self.history )< 100:
            self.history.append(Point)
        else:
            self.history.pop(0)
            self.history.append(Point)
    
    def update_colors (self):
        current_time = self.history[-1].t
        for i, point in enumerate(self.history):
            landa = current_time - point.t
            c = [i * (1 - landa) for i in point.color]
            self.history[i].color = (c[0], c[1], c[2])






canvas = np.zeros((900,1500))

p1 = Point(0.09,0.09,0.01,(255,255,255))
P1 = Points()
P1.add_point(p1)
t = 0.09
while t <0.1:
    print(t)
    for p in P1.history:
        print(p.x,p.y)
        if(p.x < 900 and p.y < 1500 and p.x >0 and p.y > 0):
            
            cv2.circle(canvas,(int(p.x), int(p.y)), 3, p.color, -1)

    cv2.imshow('Canvas', canvas)
    cv2.waitKey(100)
    t += 0.000001
    last_point = P1.history[-1]
    (x, y) = last_point.get_next(fx, fy , t)
    next_point = Point(x, y , t, (255,255,255))
    P1.add_point(next_point)
    P1.update_colors()



    



cv2.waitKey(0)
cv2.destroyAllWindows()