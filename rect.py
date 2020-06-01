### Rectangle
#### R-tree
## Author: Duong Le - Trung Huynh
## Features: 2-D R-tree
##  
## Version:
# ----------------------------------------------------
#  
import math,random
import matplotlib.pyplot as plt

def rr():
    return random.uniform(0.0,10.0)

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    '''
    Upper left(u) corner to Lower right(l) corner of a Rectangle
    '''
    __slots__ = ("ux","uy","lx","ly", "swapped_x", "swapped_y")

    def __init__(self,ux,uy,lx,ly):
        self.swapped_x = (lx < ux)
        self.swapped_y = (uy < ly)
        self.ux = ux
        self.uy = uy
        self.lx = lx
        self.ly = ly
        if self.swapped_x: 
            self.lx,self.ux = self.ux,self.lx
            print("ux,uy,lx,ly: swapped ux<-->lx!")
        if self.swapped_y: 
            self.ly,self.uy = self.uy,self.ly
            print("ux,uy,lx,ly: swapped uy<-->ly!")
 
    def coords(self):
        return self.ux,self.uy,self.lx,self.ly

    def size(self):
        w = self.lx - self.ux
        h = self.uy - self.ly
        return w * h

    def is_present(self,item):
        #Check is-present of Point/Rectangle
        if (type(item)==Point):
            if (self.ux<=item.x<=self.lx and self.ly<=item.y<=self.uy):
                return True
        elif (type(item)==Rectangle):
            if(self.ux<=item.ux<=self.lx and self.ly<=item.uy<=self.uy and self.ux<=item.lx<=self.lx and self.ly<=item.ly<=self.uy):
                return True
        return False

    def __str__(self):
        return ("Rectange:  "+str(self.ux)+" "+str(self.uy)+" "+str(self.lx)+" "+str(self.ly)+" \n")

    def rectgen(self, size=10):
        #Generate random rectangles, step == 10.0
        self.ux,self.uy,w,h = rr(),rr(),random.uniform(0,size),random.uniform(0,size)
        #self.lx = self.ux + w
        #self.ly = self.uy - h
        r = Rectangle(self.ux,self.uy,self.ux + w,self.uy - h)
        return r
    
    def rect_draw(self):
        plt.axes()
        re = plt.Rectangle((self.ux,self.ly), self.lx, self.uy, fc='blue',ec="red")
        plt.gca().add_patch(re)
        plt.axis('scaled')
        plt.show()
        return

'''
class rect_generate():
    
    #Generate random rectangles
    
    def rectgen(self, size=10.0):
        #Generate random rectangles, step == 10.0
        self.ux,self.uy,w,h = rr(),rr(),random.uniform(0.0,size), random.uniform(0.0,size)
        self.uy = self.ux + w
        self.ly = self.lx - h
        r = Rectangle(self.ux,self.uy,self.lx,self.ly)
        #assert(not self.swapped_x)
        #assert(not self.swapped_y)
        return r
'''