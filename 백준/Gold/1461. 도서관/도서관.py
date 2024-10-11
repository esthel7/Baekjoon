import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))

l.sort()
l=deque(l)

if abs(l[0])<abs(l[-1]): # -+,++
  answer=l[-1]
  for i in range(M):
    if l and l[-1]>0:
      l.pop()
    else:
      break
elif abs(l[0])==abs(l[-1]): # --, ++, -+
  if l[0]>0:
    answer=l[0]
    for i in range(M):
      if l and l[0]>0:
        l.popleft()
      else:
        break
  else:
    answer=-l[0]
    for i in range(M):
      if l and l[0]<0:
        l.popleft()
      else:
        break
else: # -+, --
  answer=-l[0]
  for i in range(M):
    if l and l[0]<0:
      l.popleft()
    else:
      break

while l:
  if abs(l[0])<abs(l[-1]): # -+,++
    answer+=l[-1]*2
    for i in range(M):
      if l and l[-1]>0:
        l.pop()
      else:
        break
  elif abs(l[0])==abs(l[-1]): # --, ++, -+
    if l[0]>0:
      answer+=l[0]*2
      for i in range(M):
        if l and l[0]>0:
          l.popleft()
        else:
          break
    else:
      answer+=-(l[0])*2
      for i in range(M):
        if l and l[0]<0:
          l.popleft()
        else:
          break
  else: # -+, --
    answer+=(-l[0])*2
    for i in range(M):
      if l and l[0]<0:
        l.popleft()
      else:
        break

print(answer)

# -1 3 4 5 6 11
# 11 5*2 6 2
