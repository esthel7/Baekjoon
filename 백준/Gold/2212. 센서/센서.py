import sys
import heapq
input=sys.stdin.readline

N=int(input())
K=int(input())
l=list(map(int,input().split()))
l=list(set(l))
l.sort()
N=len(l)

if K>=N:
  print(0)
  exit(0)

answer=2000000
diff=[]
for i in range(1,N):
  heapq.heappush(diff,[l[i-1]-l[i],i-1])

cut=[]
for _ in range(K-1):
  value,idx=heapq.heappop(diff)
  heapq.heappush(cut,idx)

answer=0
start=-1
while cut:
  item=heapq.heappop(cut)
  answer+=l[item]-l[start+1]
  start=item
answer+=l[N-1]-l[start+1]
print(answer)

# 3 // 6, 7, 8 // 10, 12 // 14, 15 // 18, 20

# 3 // 6, 7, 8 // 10 // 12, 14, 15 // 18, 20
