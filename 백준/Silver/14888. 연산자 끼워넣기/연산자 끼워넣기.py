def cal(l,m):
    total=l[0]
    j=0
    for i in range(1,len(l)):
        if m[j]==1:
            total=total+l[i]
        elif m[j]==2:
            total=total-l[i]
        elif m[j]==3:
            total=total*l[i]
        else:
            if total<0:
                total=(-1)*total//l[i]
                total=total*(-1)
            else:
                total=total//l[i]
        j=j+1
    return total

def change(h,m,i,l,t,num,last):
    if i==last:
        total=cal(l,h)
        t.append(total)
        if len(t)==num:
            print(max(t))
            print(min(t))
            return
    else:
        for j in range(len(m)):
            h[i]=m[j]
            del(m[j])
            change(h,m,i+1,l,t,num,last)
            m.insert(j,h[i])
      

import math
import sys
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
a,b,c,d=map(int,sys.stdin.readline().split())
m=[]
m=[1]*a+[2]*b+[3]*c+[4]*d
h=[0]*len(m)
t=[]
num=math.factorial(len(m))
last=len(m)
change(h,m,0,l,t,num,last)