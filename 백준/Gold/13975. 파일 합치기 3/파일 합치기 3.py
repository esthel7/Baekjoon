import sys
import heapq
input=sys.stdin.readline

def find(K):
  answer=0
  while K>1:
    if K==2:
      left=l.pop()
      l[0]+=left
      break
    K-=1
    first=heapq.heappop(l)
    second=heapq.heappop(l)
    third=heapq.heappop(l)
    if first+second<second+third:
      heapq.heappush(l,first+second)
      heapq.heappush(l,third)
      answer+=first+second
    else:
      answer+=second+third
      heapq.heappush(l,second+third)
      heapq.heappush(l,first)

  print(answer+l[0])

T=int(input())
for _ in range(T):
  K=int(input())
  l=list(map(int,input().split()))
  l.sort()
  find(K)
