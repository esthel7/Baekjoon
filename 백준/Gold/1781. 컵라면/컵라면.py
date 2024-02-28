import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  dead,cup=map(int,input().split())
  l.append([dead,cup])

l.sort(key=lambda x:[x[0],-x[1]])

dp=[0 for i in range(N)]
info=[]
heapq.heapify(info)
now=0
for i in range(N):
  if now<l[i][0]:
    dp[now]=l[i][1]
    heapq.heappush(info,[l[i][1],now])
    now+=1
  else:
    Min=info[0][0]
    if Min<l[i][1]:
      idx=info[0][1]
      dp[idx]=l[i][1]
      heapq.heappop(info)
      heapq.heappush(info,[l[i][1],idx])

print(sum(dp))
