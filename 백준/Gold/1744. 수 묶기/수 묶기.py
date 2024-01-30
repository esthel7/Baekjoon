import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(int(input()))
l.sort()
l=deque(l)

newL=[]
for i in range(N-1,0,-2):
  if i-1<0:
    break
  if l[i-1]<=0:
    break
  a=l.pop()
  b=l.pop()
  if b==1:
    newL.append(a+b)
    continue
  newL.append(a*b)

while True:
  if len(l)<=1:
    break
  if l[1]>0:
    break
  a=l.popleft()
  b=l.popleft()
  newL.append(a*b)

print(sum(l)+sum(newL))
