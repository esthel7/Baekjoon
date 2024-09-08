import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))
l.sort(reverse=True)
l=deque(l)

answer=0
while K:
  if l[0]<=K:
    plus=K//l[0]
    answer+=plus
    K-=l[0]*plus
  l.popleft()

print(answer)
