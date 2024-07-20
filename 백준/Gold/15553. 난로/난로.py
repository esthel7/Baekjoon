import sys
import heapq
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())

l=deque([])
diff=[]
l.append(int(input()))
for i in range(1,N):
  l.append(int(input()))
  heapq.heappush(diff,-(l[i]-l[i-1]-1))

answer=l[-1]-l[0]+1
K-=1
for i in range(K):
  answer+=heapq.heappop(diff)

print(answer)
# 3 ~ 6

# 12 34 67
