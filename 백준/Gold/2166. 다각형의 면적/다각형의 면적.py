import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

value=0
for i in range(1,N):
  x1,y1=l[i-1]
  x2,y2=l[i]
  value+=x1*y2-x2*y1

x1,y1=l[-1]
x2,y2=l[0]
value+=x1*y2-x2*y1

print('%.1lf'%(abs(value)/2))
