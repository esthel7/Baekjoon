import sys
import heapq
input=sys.stdin.readline

N=int(input())
graph=[[] for i in range(N+1)] # 해당 건물 완성되면 지을 수 있는 건물 리스트트
cnt=[0 for i in range(N+1)] # 0 되면 지을 수 있음
time=[0 for i in range(N+1)]
q=[]
for i in range(1,N+1):
  now=list(map(int,input().split()))
  time[i]=now[0]
  for j in range(1,len(now)-1):
    cnt[i]+=1
    graph[now[j]].append(i)
  if cnt[i]==0:
    heapq.heappush(q,[time[i],i])

answer=[0 for i in range(N+1)]
while q:
  t,idx=heapq.heappop(q)
  answer[idx]=t
  for node in graph[idx]:
    cnt[node]-=1
    if cnt[node]==0:
      heapq.heappush(q,[t+time[node],node])

for i in range(1,N+1):
  print(answer[i])
