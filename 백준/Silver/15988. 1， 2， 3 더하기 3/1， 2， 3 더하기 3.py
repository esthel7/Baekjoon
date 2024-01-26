import sys
from collections import deque
input=sys.stdin.readline

def find(T):
  l=deque([0 for i in range(4)])
  l[0]=1
  l[1]=2
  l[2]=4
  now=0

  for i in range(1,4):
    if i in num:
      now+=1
      num[i]=l[i-1]
      if now==T:
        return

  for i in range(4,1000010):
    l[3]=(l[0]+l[1]+l[2])%1000000009

    if i in num:
      now+=1
      num[i]=l[3]
      if now==T:
        return

    l.popleft()
    l.append(0)


T=int(input())
num={}
for i in range(T):
  n=int(input())
  num[n]=0

find(T)
for keys in num.keys():
  print(num[keys])


