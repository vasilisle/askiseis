import random

p=[0 for i in range(98)]
p.append(1)
p.append(2)
random.shuffle(p)
m=[[0 for i in range(10)]for i in range(10)]
a=0
for i in range(10):
    for j in range(10):
        m[i][j]=p[a]
        a=a+1
        if (m[i][j]==1):
            s1=i
            g1=j
        elif (m[i][j]==2):
            s2=i
            g2=j
dif=True
while (dif):
    if (s1>=s2) and (g1>=g2):
        print ('distance is:')
        print g1-g2+s1-s2
    elif (s1>=s2) and (g1<=g2):
        print ('distance is:')
        print g2-g1+s1-s2
    elif (s1<=s2) and (g1>=g2):
        print ('distance is:')
        print g1-g2+s2-s1
    elif (s1<=s2) and (g1<=g2):
        print ('distance is:')
        print s2-s1+g2-g1
    kat=raw_input('choose direction w to go up,s to go down,a for left or d for left')
    if (kat=='a'):
        g1=g1-1
    elif (kat=='s'):
        s1=s1+1
    elif (kat=='d'):
        g1=g1+1
    else :
        s1=s1-1
    if (s1==s2) and (g1==g2):
        dif=False
    
