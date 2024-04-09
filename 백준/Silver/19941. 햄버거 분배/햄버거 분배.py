import sys
from collections import deque
input=sys.stdin.readline

# 자신의 위치에서 거리가 K 이하인 햄버거


N,K=map(int,input().split())
l=list(input().rstrip())

P=deque([])
H=deque([])
for i in range(len(l)):
  if l[i]=='H':
    H.append(i)
  else:
    P.append(i)

answer=0
while P and H:
  if P[0]-K<=H[0] and P[0]+K>=H[0]:
    H.popleft()
    P.popleft()
    answer+=1
  elif P[0]+K<H[0]:
    P.popleft()
  else: # P[0]-K>H[0]
    H.popleft()

print(answer)
