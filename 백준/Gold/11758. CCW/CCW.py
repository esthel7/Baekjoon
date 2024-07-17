import sys
input=sys.stdin.readline

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

l1=0
if x2!=x1:
  l1=(y2-y1)/(x2-x1)
p1=y1-(l1*x1)
# y = l1*x + p1

l2=0
if x3!=x2:
  l2=(y3-y2)/(x3-x2)
p2=y2-(l2*x2)

if l1==l2:
  print(0)
  exit(0)

if l1==0:
  if x1==x2:
    if y1<y2:
      if x1<x3:
        print(-1)
      else:
        print(1)
    else:
      if x1>x3:
        print(-1)
      else:
        print(1)
  else: # y1==y2
    if x1<x2:
      if y1<y3:
        print(1)
      else:
        print(-1)
    else:
      if y1>y3:
        print(1)
      else:
        print(-1)
else:
  if x1<x2:
    if y3>l1*x3+p1:
      print(1)
    else:
      print(-1)
  else:
    if y3<l1*x3+p1:
      print(1)
    else:
      print(-1)
