import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=deque([])
right=False
for i in range(N):
  now=input().rstrip()
  if now=='KBS1':
    l.append(0)
  elif now=='KBS2':
    if 0 in l:
      right=True
    l.append(1)
  else:
    l.append(2)

answer=''
now=0
while l[now]!=0:
    now+=1
    answer+='1'
for i in range(now,0,-1):
  answer+='4'

if not right:
  l.appendleft(2)

now=0
while l[now]!=1:
    now+=1
    answer+='1'
for i in range(now,1,-1):
  answer+='4'

print(answer)
