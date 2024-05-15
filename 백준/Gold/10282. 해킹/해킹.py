import sys
import heapq
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  n,d,c=map(int,input().split())
  c-=1
  l=[-1 for i in range(n)]
  l[c]=0
  info={}
  for i in range(d):
    a,b,s=map(int,input().split())
    a-=1
    b-=1
    if b in info:
      info[b][a]=s
    else:
      info[b]={a:s}
  q=[]
  heapq.heappush(q,[0,c])
  answer=[0,0]
  while q:
    time,item=heapq.heappop(q)
    if l[item]!=time:
      continue
    answer[0]+=1
    answer[1]=time
    if item in info:
      for nextItem in info[item]:
        nextTime=info[item][nextItem]
        if l[nextItem]==-1 or l[nextItem]>time+nextTime:
          l[nextItem]=time+nextTime
          heapq.heappush(q,[time+nextTime,nextItem])
  print(answer[0],answer[1])
