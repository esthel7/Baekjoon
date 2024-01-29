import heapq

n,m=map(int,input().split())
l=list(map(int,input().split()))
heapq.heapify(l)
for i in range(m):
  a=heapq.heappop(l)
  b=heapq.heappop(l)
  heapq.heappush(l,a+b)
  heapq.heappush(l,a+b)
print(sum(l))
