import sys
import heapq
input=sys.stdin.readline

N,K=map(int,input().split())
l=[[] for i in range(N)]
q=[]
for i in range(N):
  name,gold,silver,bronze=map(int,input().split())
  heapq.heappush(q,[-gold,-silver,-bronze,name])

rank=1
num=1
pg,ps,pb,name=heapq.heappop(q)
if name==K:
  print(1)
  exit(0)

while q:
  g,s,b,name=heapq.heappop(q)
  if pg==g and ps==s and pb==b:
    num+=1
  else:
    rank+=num
    num=1
  pg=g
  ps=s
  pb=b
  if name==K:
    print(rank)
    break
