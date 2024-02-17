import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
l=list(map(int,input().split()))
s=deque([deque([])for i in range(K+1)])

for i in range(K):
  s[l[i]].append(i)

answer=0
h=[0 for i in range(N)]
for i in range(K):
  now=l[i]
  s[now].popleft()
  if now in h:
    continue
  else:
    if 0 in h:
      for j in range(N):
        if h[j]==0:
          h[j]=now
          break
      continue

    Max=0
    off=0
    for j in range(N):
      if not s[h[j]]:
        off=j
        break
      hole=s[h[j]][0]
      if Max<hole:
        Max=hole
        off=j
    h[off]=now
    answer+=1

print(answer)
