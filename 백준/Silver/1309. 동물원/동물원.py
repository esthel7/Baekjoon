import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=deque([0 for i in range(2)])
answer=3
l[0]=1

if N==1:
  print(answer)
  exit(0)

answer+=4
l[1]=2
for i in range(2,N):
  l.append(l.popleft()+l[0]*2)
  answer+=l[-1]*2

print(answer%9901)
