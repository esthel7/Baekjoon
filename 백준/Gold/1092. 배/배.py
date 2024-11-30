import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)

M=int(input())
w=list(map(int,input().split()))
w.sort(reverse=True)

time=0
while w:
  time+=1
  remove=[]
  idx=0
  for i in range(len(w)):
    if idx==N:
      break
    if w[i]<=l[idx]:
      remove.append(i)
      idx+=1
  if not remove:
    print(-1)
    exit()
  for i in range(len(remove)-1,-1,-1):
    w=w[:remove[i]]+w[remove[i]+1:]

print(time)

# 30, 27, 27, 27, 19, 10, 5, 4, 3, 2
