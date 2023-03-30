import sys
import heapq
input=sys.stdin.readline

#음이 아닌 가중치이므로 다익스트라 사용
def find(begin):
    q=[]
    visited[begin]=0
    heapq.heappush(q,(0,begin)) # q에 가격이랑 출발점 넣기
    while len(q)>0:
        cost,begin=heapq.heappop(q)

        if visited[begin]<cost:
            continue # 시간 절약 포인트

        for i in range(len(f[begin])):
            depart,appendCost=f[begin][i]
            if visited[depart]>cost+appendCost:
                visited[depart]=cost+appendCost
                heapq.heappush(q,[cost+appendCost,depart])

N=int(input())
M=int(input())
f=[[]for i in range(N+1)] # 도착점, 가격 들어있음
for i in range(M):
    A,B,cost=map(int,input().split())
    f[A].append([B,cost])
start,end=map(int,input().split())

if start==end:
    print(cost)
else:
    s=[]
    visited=[100000000]*1001 # costs
    find(start)
    print(visited[end])
