import  sys
from collections import deque
input=sys.stdin.readline

N=int(input())
q=deque([])
for i in range(N):
  now=input().rstrip().split()
  if len(now)==2:
    q.append(now[1])
    continue
  if now[0]=='pop':
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif now[0]=='size':
    print(len(q))
  elif now[0]=='empty':
    if not q:
      print(1)
    else:
      print(0)
  elif now[0]=='front':
    if not q:
      print(-1)
    else:
      print(q[0])
  else:
    if not q:
      print(-1)
    else:
      print(q[-1])

