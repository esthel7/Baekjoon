import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
edges=[]
for i in range(M):
  a,b,w=map(int,input().split())
  if a<b:
    edges.append([w,a,b])
  elif a>b:
    edges.append([w,b,a])

heapq.heapify(edges)
answer=0
rootcnt=N
root=[200000 for i in range(N+1)]
info={}

while edges:
  [w,a,b]=heapq.heappop(edges)
  if rootcnt==2:
    print(answer)
    break
  answer+=w
  rootcnt-=1
  if root[a]==root[b]:
    if root[a]!=200000:
      answer-=w
      rootcnt+=1
      continue
    root[a]=a
    root[b]=a
    info[a]=[a,b]
  else:
    if root[a]<root[b]:
      change=root[b]
      save=root[a]
      if root[b]==200000:
        root[b]=root[a]
        info[save].append(b)
        change=-1
    else:
      change=root[a]
      save=root[b]
      if root[a]==200000:
        root[a]=root[b]
        info[save].append(a)
        change=-1

    if change!=-1:
      for node in info[change]:
        info[save].append(node)
        root[node]=save
      info[change]=[]

