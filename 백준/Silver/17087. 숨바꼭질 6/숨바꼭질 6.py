import sys
from collections import deque
input=sys.stdin.readline

N,S=map(int,input().split())
first=list(map(int,input().split()))

l=[]
for i in range(N):
  l.append(abs(S-first[i]))
l.sort()

answer=l[0]
for i in range(1,N):
  if l[i]%answer==0:
    continue
  else:
    left=deque([])
    right=[]
    for j in range(1,int(answer**0.5)+1):
      if answer%j==0:
        left.appendleft(j)
        right.append(answer//j)

    possible=right+list(left)
    for item in possible:
      if l[i]%item==0:
        answer=item
        break

print(answer)
