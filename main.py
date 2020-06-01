### Main
#### R-tree
## Author: Duong Le - Trung Huynh
## Features: 2-D R-tree
##  
## Version:
# ----------------------------------------------------
#  
from rtree import *
from knn import *
from rect import *
import random, math
import matplotlib.pyplot as plt

def main():
    #size = 20.0
    #numberrect = 10
    #rec=[None]*numberrect

    a = RTree()
    '''
    for i in range (numberrect):
        rec[i] = Rectangle(rr(),rr(),random.uniform(0,size),random.uniform(0,size))
    '''
    rec1=Rectangle(10,12,11,14)
    #rec1.rect_draw()
    rec2=Rectangle(13,15,14,17)
    #rec2.rect_draw()
    rec3=Rectangle(14,16,17,19)
    rec4=Rectangle(14,15,15,14)
    rec5=Rectangle(21,22,23,23)
    rec6=Rectangle(24,27,28,25)
    rec7=Rectangle(30,32,32,30)
    rec8=Rectangle(35,36,36,35)
    rec9=Rectangle(40,45,45,40)
    rec10=Rectangle(50,53,53,50)
    rec11=Rectangle(5,6,6,5)
    rec12=Rectangle(7,8,8,7)
    rec13=Rectangle(55,57,57,55)
    rec14=Rectangle(60,62,62,60)
    rec15=Rectangle(65,66,66,65)
    rec16=Rectangle(90,100,100,90)
    rec17=Rectangle(60,70,65,60)
    rec18=Rectangle(150,200,170,140)
    rec19=Rectangle(80,100,90,90)
    rec20=Rectangle(12,32,32,12)

    p1="o1"
    p2="o2"
    p3="o3"
    p4="o4"
    p5="o5"
    p6="o6"
    p7="o7"
    p8="o8"
    p9="o9"
    p10="o10"
    p11="o11"
    p12="o12"
    p13="o13"
    p14="o14"
    p15="o15"
    p16="o16"
    p17="o17"
    p18="o18"
    p19="o19"
    p20="o20"

    #Inserting 20 rectangles
    '''
    a.insert(rec[0],p1)
    a.insert(rec[1],p2)
    a.insert(rec[2],p3)
    a.insert(rec[3],p4)
    a.insert(rec[4],p5)
    a.insert(rec[5],p6)
    a.insert(rec[6],p7)
    a.insert(rec[7],p8)
    a.insert(rec[8],p9)
    a.insert(rec[9],p10)
    '''
    a.insert(rec1,p1)
    a.insert(rec2,p2)
    a.insert(rec3,p3)
    a.insert(rec4,p4)
    a.insert(rec5,p5)
    a.insert(rec6,p6)
    a.insert(rec7,p7)
    a.insert(rec8,p8)
    a.insert(rec9,p9)
    a.insert(rec10,p10)
    a.insert(rec11,p11)
    a.insert(rec12,p12)
    a.insert(rec13,p13)
    a.insert(rec14,p14)
    a.insert(rec15,p15)
    a.insert(rec16,p16)
    a.insert(rec17,p17)
    a.insert(rec18,p18)
    a.insert(rec19,p19)
    a.insert(rec20,p20)
    #rec1.rect_draw()
    
    #R-Tree Display
    print("\n",15 * "-" , "R-Tree" , 30 * "-","\n",)
    #a.display()
    
    #Look-Up for rec
    print("\n",15 * "-" , "Look-Up for a Point" , 30 * "-","\n",)
    p=Point(42,45)
    print(a.lookup(p))
    
    #Finding k nearest neighbours to the point p  (k=5 in this case)
    print("\n",15 * "-" , "KNN (k=5 Nearest Neighbours to Point(1,3))" , 30 * "-","\n",)
    p=Point(1,3)
    nearest_neighbours(p,a,5)

    #Deleting rec8 (and R-Tree display after deleting rec8)
    print("\n",15 * "-" , "Deletion (for o8)" , 30 * "-","\n",)
    a.delete(rec8)
    a.display()

if __name__ == '__main__':
    main()
