import math
from point import Point
import time
import sys,os
import random
import matplotlib.pyplot as plt
def init_map_points( Lr,Ld,WB,WL):
    l=[]
    y=0
    for x in range(Lr+Ld):
        if (x>Lr):
            y =round( (x*(WL-WB)-Lr*(WL-WB)+WB*Ld)/Ld)
            #print(x,y)
            if (y<WB):
                l.append(Point(x,y))

    return l
def convertPointToPattern(list,sizeW,sizeL):
    img=[[255 for i in range(sizeW)] for i in range(sizeL)]

    for p in list:
        #if ((p.X>=0) and (p.X<sizeL) and (p.Y>=0) and (p.Y<sizeW)):
            #print(p.Y,p.X)
            img[p.Y][p.X]=0


    return img

def computeMap(carList,map,l,w):
    temp = map
    for car in carList:
        for x,y in carShape(carList,l,w,len(map[0]),len(map)):
            temp[y][x]=0
    norm = plt.Normalize(0, 256)

    return (norm(temp))

def addBlock(blockMap,p,Lcar,Wcar):
    w=len(blockMap[0])
    l=len(blockMap)
    #print(l,w)
    for x in range(p.X-Lcar+1,p.X+Lcar):
        for y in range(p.Y-Wcar+1,p.Y+Wcar):
            if (judgeInMap(x,y,l,w)):
                #print('b',x,y)
                blockMap[x][y]=True
    return blockMap
def initialBlockMap(blockPoints,sizeW,sizeL,Lcar,Wcar):
    ans=[[False for i in range(sizeW)] for i in range(sizeL)]
    for p in blockPoints:
        #print('blockP',p.X,p.Y)
        for x in range(p.X-(int(Lcar/2)),p.X+1):
            for y in range(p.Y-(int(Wcar/2)),p.Y+1):
                #print(x,y,sizeL,sizeW)
                if (judgeInMap(x,y,sizeL,sizeW)):
                    #print('b',x,y)
                    ans[x][y]=True
    for x in range(sizeL):
        ans[x][int(Wcar/2)-1]=True
    return ans

def carShape(carList,l,w,ll,ww):
    ans=[]
    for car in carList:
        for x in range(l):
            for y in range(w):
                xx=car.X-(int(l/2))+x
                yy=car.Y-(int(w/2))+y
                if (judgeInMap(xx,yy,ll,ww)):
                    ans.append([xx,yy])
    return ans

    return

def judgeInMap(x,y,l,w):
    if ((x>=0)&(x<l)&(y>=0)&(y<w)):
        return True
    else:
        return False


def cur_file_dir():

    path = sys.path[0]


    if os.path.isdir(path):

        return path

    elif os.path.isfile(path):

        return os.path.dirname(path)

def getTime():
    return time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))