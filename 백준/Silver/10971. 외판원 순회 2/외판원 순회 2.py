import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

q=[]
visited=[False for i in range(N)]
visited[0]=True
for i in range(1,N):
  if l[0][i]==0:
    continue
  visited[i]=True
  heapq.heappush(q,[l[0][i],i,1,list(visited)])
  visited[i]=False

while q:
  value,now,cnt,visited=heapq.heappop(q)
  # print(value,now,cnt,visited,q)
  if cnt==N:
    print(value)
    exit(0)

  if cnt==N-1:
    if l[now][0]!=0:
      heapq.heappush(q,[value+l[now][0],0,cnt+1,list(visited)])
    continue

  for i in range(1,N):
    if visited[i] or l[now][i]==0:
      continue
    visited[i]=True
    heapq.heappush(q,[value+l[now][i],i,cnt+1,list(visited)])
    visited[i]=False


# 0 1 100 100
# 100 0 1 100
# 100 100 0 1
# 1 0 100 100

# 3
# 0 10 15
# 5 0 9
# 6 13 0
