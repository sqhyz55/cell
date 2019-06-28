import matplotlib.pyplot as plt
from point import Point
import matplotlib.animation as animation
import random
from funcs import *
import numpy as np

import time
import matplotlib.pyplot as plt
fig = plt.figure()
#data = np.arange(100).reshape(10, 10)



random.seed(a=10000)
# initial
Lcar=9
Wcar=5
Vmax=20

B=8
Wb=9
WB=Wb*B
L =3
Wl = 7
WL=Wl*L

Lr=100
Ld=600


sizeW=WB
sizeL=Lr+Ld
grad=((WB-WL)/Ld)
blockPoints= init_map_points(Lr,Ld,WB,WL)

step = 0
pin = 0.4
pd = 0.1
pv=0.3
q=0

points=[]
carList=[]
initBlockMap=initialBlockMap(blockPoints,sizeW,sizeL,Lcar,Wcar)
map = convertPointToPattern(blockPoints,sizeL,sizeW);
cmap = plt.cm.gray
norm = plt.Normalize(0,256)
rgba = cmap(norm(map))

def compare(p):
    return -p.X
def fushu(x):
    return -x
def computeNext():
    global carList, map, step, p1, pd, q
    map = convertPointToPattern(blockPoints, sizeL, sizeW);
    carList.sort(key = compare)
    blockMap=initialBlockMap(blockPoints,sizeW,sizeL,Lcar,Wcar)
    removeList=[]
    for i in range(len(carList)):
        car=carList[i]
        #print(car.X,car.Y,car.V)
        x=car.X
        y=car.Y
        v2=car.V
        for dn in range(Vmax):
            if (judgeInMap(x+dn+1,y,sizeL,sizeW)):
                #print(x+dn+1,y)
                if (blockMap[x+dn+1][y]):

                    break
            else:
                break
        #speed update
        #print(dn)
        if(random.random()<pv):
            v2=max(v2-1,0)
            v2=min(v2,dn)
        else:
            v2=min(v2+1,Vmax,dn)
        #position update
        if (x+v2+1>=sizeL):
            removeList.append(i)
            q=q+1
        else:
            if (y>WL*0.7):
                x = x + v2
                dy=round(v2*(WB-WL/2)/(Ld+Lr)+(random.random()-0.5))
                if (v2==0): dy=(int)((WB-WL/2)/(Ld+Lr))+1
                if (v2<dy) :x=x+dy-v2
                v2=max(dy,v2)
                if (y>dy):
                        if (x+v2-dy<sizeL):
                            if (not blockMap[x+v2-dy][y-dy]):
                                y=y-dy
                                x=x-dy
            else:
                x=x+v2
                if (random.random()<pd):
                    if (y>0):
                        if (not blockMap[x][y-1]):
                            y=y-1
            p=Point(x,y)
            p.V=v2
            carList[i]=p
            blockMap=addBlock(blockMap, p, Lcar, Wcar)
    removeList.sort(key=fushu)
    #print('len of carList',len(carList))
    for i in removeList:
        del carList[i]
    for i in range(B):
        if (random.random()<pin):
            x=0
            y=i*Wb+int(Wb/2)+1
            if (not blockMap[x][y]):
                carList.append(Point(x, y))
    return
def updatefig(*args):
    global carList,map,step,p1,pd,q
    print(step)
    if (step==150)or(step==225)or(step==247)or(step==250):
        plt.savefig('D:\_'+str(step)+'.png')
    for i in range(1):computeNext()
    step=step+1
    im.set_array(computeMap(carList,map,Lcar,Wcar))


im = plt.imshow(computeMap(carList,map,Lcar,Wcar), cmap = plt.cm.gray,animated=True)
ani = animation.FuncAnimation(fig, updatefig, interval=10)
plt.show()
localPath=cur_file_dir()
print(localPath)
totalStep=3600;
t=np.arange(totalStep)
q_t=np.arange(totalStep)
midu_gap=30
midu=np.linspace(0, 1, midu_gap, endpoint=True)
q_midu=np.linspace(0, 1, midu_gap, endpoint=True)
for i in range(midu_gap):
    pin=midu[i];
    print(pin)
    carList=[]
    q=0
    percent1=i/midu_gap*100
    for step in range(totalStep):
        if (step%36==0) :print((percent1+step/3600/midu_gap*100),'%')
        if (step==600):
            q_midu[i]=q
        computeNext()
    q_midu[i]=(q-q_midu[i])*6/5
plt.plot(midu,q_midu)
plt.show()


