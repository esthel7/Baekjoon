import sys
import heapq
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  def find(start):
    q=[]
    heapq.heappush(q,[0,start])
    visited=[False for i in range(n+1)]
    last=[]
    cnt=0
    while q:
      time,num=heapq.heappop(q)
      if visited[num]:
        continue
      visited[num]=True
      cnt+=1
      last=[cnt,time]
      if num in graph:
        for node in graph[num]:
          if visited[node]:
            continue
          heapq.heappush(q,[time+graph[num][node],node])
    print(last[0],last[1])


  n,d,c=map(int,input().split())
  graph={}
  for i in range(d):
    a,b,s=map(int,input().split())
    if b in graph:
      graph[b][a]=s
    else:
      graph[b]={a:s}
  find(c)
