import numpy as np
# import cv2 
import pygame
import random

class Lorenz:
    def __init__(self):
        self.xMin , self.xMax = -30, 30
        self.yMin, self.yMax = -30, 30
        self.zMin , self.zMax = 0, 50 
        self.X , self.Y, self.Z = 0.1, 0.0, 0.0
        self.oX, self.oY, self.oZ = self.X, self.Y, self.Z
        self.dt = 0.0005
        self.a , self.b, self.c  =10, 28, 8/3
        self.pixelcolor = (255,0,0)

    def step(self):
        self.oX, self.oY, self.oZ = self.X, self.Y, self.Z
        self.X = self.X + (self.dt * self.a * (self.Y - self.X))
        self.Y = self.Y + (self.dt * (self.X * (self.b - self.Z) - self.Y))
        self.Z = self.Z + (self.dt * (self.X * self.Y - self.c * self.Z))

    def draw(self, display):
        width, height = display.get_size()
        oldpos = self.ConvertToScreen(self.oX,self.oY,self.xMin,self.xMax,self.yMin,self.yMax,width,height)
        newpos = self.ConvertToScreen(self.X,self.Y,self.xMin,self.xMax,self.yMin,self.yMax,width,height)
        
        newRect = pygame.draw.line(display, self.pixelcolor,oldpos, newpos,2)
        
        return newRect

    def ConvertToScreen(self, x, y, xMin, xMax, yMin, yMax, width, height):
        newX = width * ((x - xMin) / (xMax - xMin))
        newY = height * ((y - yMin) / (yMax - yMin))
        return round(newX), round(newY)

class lorenz_app:
    def __init__(self):
        
        self.count = 0
        self.isrunning = True
        self.displaySurface = None
        self.fpsClock = None
        self.attractors = []
        self.width , self.height = 1820,980
        self.size = (self.width, self.height)
        # self.size = 0
        
        self.outputCount = 1

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Lorenz")
        self.displaySurface = pygame.display.set_mode(self.size)
        self.isrunning = True
        self.fpsClock = pygame.time.Clock()
        color = []
        # color.append((50,120,200))
        # color.append((255,0,100))
        # color.append((100,30,12))
        # color.append((180,90,30))
        # color.append((68, 80, 148))
        color.append((29, 17, 53))
        color.append((12, 22, 79))
        # color.append((186, 30, 104))
        color.append((86, 67, 253))
        color.append((118, 73, 254  ))
        color.append((252, 251, 254))
        
        
        for i in range(5):
            self.attractors.append(Lorenz())
            
            self.attractors[i].X = random.uniform(0.01, 0.101)

            self.attractors[i].pixelcolor = color[i]

    

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.isrunning = False

    def on_loop(self):
        # print(type(self.attractors[0]))
        for x in self.attractors:
            x.step()

    def on_render(self):
        for x in self.attractors:   
            newRect = x.draw(self.displaySurface)
            pygame.display.update(newRect)

    def on_execute (self):
        if self.on_init() == False:
            self.isrunning = False
        
        while self.isrunning:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            self.fpsClock.tick()
            self.count += 1
        pygame.quit()

if __name__ == "__main__":
    print("pygame lorenz")
    t = lorenz_app()
    a = Lorenz()
    print(a.dt)
    print(t.isrunning)
    t.on_execute()


    






# def fx(x, y , t):
#     return (-(t**2) - (x*y) + t)

# def fy(x, y, t):
#     return(-(x * y) + (x*t) + y + t)

# class Point:
#     def __init__(self, x, y, t, color):
#         self.x = x
#         self.y = y
#         self.t = t
#         self.r = 3
#         self.color = color
#     def update (self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_next(self, fx, fy , t):
#         x = fx(self.x, self.y, t)
#         y = fy(self.x, self.y, t)
#         return (x,y)
    
    
# class Points:
#     def __init__(self):
#         self.history = []
#     def add_point(self,Point):
#         if len(self.history )< 100:
#             self.history.append(Point)
#         else:
#             self.history.pop(0)
#             self.history.append(Point)
    
#     def update_colors (self):
#         current_time = self.history[-1].t
#         for i, point in enumerate(self.history):
#             landa = current_time - point.t
#             c = [i * (1 - landa) for i in point.color]
#             self.history[i].color = (c[0], c[1], c[2])






# canvas = np.zeros((900,1500))

# p1 = Point(0.09,0.09,0.01,(255,255,255))
# P1 = Points()
# P1.add_point(p1)
# t = 0.09
# while t <0.1:
#     print(t)
#     for p in P1.history:
#         print(p.x,p.y)
#         if(p.x < 900 and p.y < 1500 and p.x >0 and p.y > 0):
            
#             cv2.circle(canvas,(int(p.x), int(p.y)), 3, p.color, -1)

#     cv2.imshow('Canvas', canvas)
#     cv2.waitKey(100)
#     t += 0.000001
#     last_point = P1.history[-1]
#     (x, y) = last_point.get_next(fx, fy , t)
#     next_point = Point(x, y , t, (255,255,255))
#     P1.add_point(next_point)
#     P1.update_colors()



    



# cv2.waitKey(0)
# cv2.destroyAllWindows()