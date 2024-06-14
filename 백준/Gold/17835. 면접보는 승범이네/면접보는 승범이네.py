import sys
import heapq
input=sys.stdin.readline

# 출발 노드를 설정
# 각 노드의 최소비용을 저장
# 방문하지않은 노드 중 비용 적은 노드 선택
# 해당 노드 거쳐 특정 노드로 가는 경우 고려

N,M,K=map(int,input().split())
graph={}
for i in range(M):
  U,V,C=map(int,input().split())
  if V in graph:
    if U in graph[V]:
      if C<graph[V][U]:
        graph[V][U]=C
    else:
      graph[V][U]=C
  else:
    graph[V]={U:C}

q=[]
placeList=list(map(int,input().split()))
for p in placeList:
  heapq.heappush(q,[0,p])

final=[-1 for i in range(N+1)]
while q:
  cnt,node=heapq.heappop(q)
  if final[node]==-1 or final[node]>cnt:
    final[node]=cnt
    if node in graph:
      for end in graph[node]:
        heapq.heappush(q,[graph[node][end]+cnt,end])

answer=[final[1],1]
for i in range(2,N+1):
  if answer[0]<final[i]:
    answer[0]=final[i]
    answer[1]=i

print(answer[1])
print(answer[0])
