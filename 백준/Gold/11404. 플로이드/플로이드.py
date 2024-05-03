import sys
from collections import deque
input=sys.stdin.readline

def find(start):
  q=deque([])
  for i in range(n):
    if track[start][i]!=-1:
      q.append([i,track[start][i]])

  while q:
    end,c=q.popleft()
    for i in range(n):
      if i==start:
        continue
      if track[end][i]!=-1:
        if track[start][i]==-1 or (track[start][i]!=-1 and c+track[end][i]<track[start][i]):
          track[start][i]=c+track[end][i]
          q.append([i,c+track[end][i]])

  for i in range(n):
    if track[start][i]==-1:
      print(0,end=' ')
      continue
    print(track[start][i],end=' ')
  print()




n=int(input())
m=int(input())
track=[[-1 for i in range(n)]for j in range(n)]
for _ in range(m):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  if track[a][b]==-1 or track[a][b]>c:
    track[a][b]=c

visited=[[False for i in range(n)]for j in range(n)]
for start in range(n):
  find(start)
