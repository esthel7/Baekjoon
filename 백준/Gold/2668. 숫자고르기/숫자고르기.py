import sys
import heapq
from collections import deque
input=sys.stdin.readline

N=int(input())
l=[[0,0]]
for i in range(N):
  l.append([i+1])
  l[i+1].append(int(input()))

visited=[False for i in range(N+1)]
answer=[]
for i in range(1,N+1):
  if visited[i]:
    continue

  if l[i][0]==l[i][1]:
    visited[i]=True
    answer.append(l[i][1])
    continue

  temp=[False for j in range(N+1)]
  possible=[[l[i][0],l[i][1]]]
  temp[i]=True
  q=deque([[l[i][0],l[i][1]]])
  breakFlag=False
  while q:
    idx,now=q.popleft()
    if visited[idx]:
      breakFlag=True
      break
    if idx==now:
      visited[idx]=True
      answer.append(l[now][1])
      breakFlag=True
      break
    if not temp[now]:
      temp[now]=True
      possible.append([now,l[now][1]])
      q.append([l[now][0],l[now][1]])
    elif now==i:
      break
    else:
      breakFlag=True
      break
  
  visited[i]=True
  if not breakFlag:
    for [idx,item] in possible:
      visited[idx]=True
      answer.append(item)

heapq.heapify(answer)
print(len(answer))
while answer:
  print(heapq.heappop(answer))
