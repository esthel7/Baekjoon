import sys
import heapq
input=sys.stdin.readline

N,L=map(int,input().split())
q=[]
for i in range(N):
  start,end=map(int,input().split())
  heapq.heappush(q,[start,end])

answer=0
last=0
while q:
  start,end=heapq.heappop(q)
  if end<last:
    continue
  if start<last:
    if (end-last)%L==0:
      plus=(end-last)//L
      answer+=plus
      last+=L*plus
    else:
      plus=(end-last)//L+1
      answer+=plus
      last+=L*plus
  else:
    if (end-start)%L==0:
      plus=(end-start)//L
      answer+=plus
      last=start+L*plus
    else:
      plus=(end-start)//L+1
      answer+=plus
      last=start+L*plus

print(answer)
