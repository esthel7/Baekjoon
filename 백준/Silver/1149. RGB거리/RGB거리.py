import sys
input=sys.stdin.readline

def find(T):
  for i in range(3*T):
    x=i//3
    y=i%3
    if i<3:
      num[i]=l[x][y]
      continue
    if y==0: # R
      small=min(num[i-1]+l[x][y],num[i-2]+l[x][y])
      num[i]=small
    elif y==1: # G
      small=min(num[i-2]+l[x][y],num[i-4]+l[x][y])
      num[i]=small
    else:
      small=min(num[i-4]+l[x][y],num[i-5]+l[x][y])
      num[i]=small


T=int(input())
l=[]
for i in range(T):
  l.append(list(map(int,input().split())))

num=[-1 for i in range(3*T)]
find(T)
print(min(num[3*T-1],num[3*T-2],num[3*T-3]))
