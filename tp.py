from random import randrange
import random
from PIL import Image, ImageDraw

meg=[]
aktina=[]
for i in range(20):
    aktina.append(randrange(10,500))
    v=aktina[i]
    meg.append(1024-v)

mik=aktina
x=[]
y=[]
for i in range(20):
    x.append(randrange(mik[i],meg[i]))
    y.append(randrange(mik[i],meg[i]))
t=0 #arithmos kiklwn pou temnontai
k=0 #voithitiki metavliti
x1=0
x2=0
y1=0
y2=0
ap=((x1-x2)**2+(y1-y2)**2)**(1/2)
for i in range(19):
    x1=x[i]
    y1=y[i]
    for j in range(i+1,20):
        x2=x[j]
        y2=y[j]
        if (ap<=aktina[i]-aktina[j]):
            if (k==i):
                t=t+1
                k=k+1
print t
im=Image.new('RGB',(1024,1024),'white')
draw=ImageDraw.Draw(im)
for i in range(20):
    draw.ellipse((x[i]-aktina[i],y[i]-aktina[i],x[i]+aktina[i],y[i]+aktina[i]),outline='red')
im.show()
im.save('kikloi.png','PNG')

