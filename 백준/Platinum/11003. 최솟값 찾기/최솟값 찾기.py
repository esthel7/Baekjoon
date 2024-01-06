import sys
from collections import deque
input=sys.stdin.readline

N,L=map(int,input().split())
d=list(map(int,input().split()))

value=deque([])

for i in range(N):
  now=d[i]

  if len(value) and value[0][1]<i-L+1:
    value.popleft()

  while len(value):
    if value[-1][0]>=now:
      value.pop()
    else:
      break

  value.append((now,i))
  print(value[0][0],end=' ')
