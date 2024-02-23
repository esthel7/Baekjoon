import sys
import heapq
input=sys.stdin.readline

N=int(input())
remove=[0 for i in range(100001)] # 0 or level
Max=[]
Min=[]
heapq.heapify(Max)
heapq.heapify(Min)
for i in range(N):
  P,L=map(int,input().split())
  remove[P]=L
  heapq.heappush(Max,[-L,-P])
  heapq.heappush(Min,[L,P])

M=int(input())
for i in range(M):
  order=input().rstrip().split()

  if order[0]=='add':
    P=int(order[1])
    L=int(order[2])
    heapq.heappush(Max,[-L,-P])
    heapq.heappush(Min,[L,P])
    remove[P]=L
  elif order[0]=='recommend':
    if order[1]=='1':
      while True:
        level=Max[0][0]*(-1)
        now=Max[0][1]*(-1)
        if remove[now]==level:
          print(now)
          break
        else:
          heapq.heappop(Max)
    else:
      while True:
        level=Min[0][0]
        now=Min[0][1]
        if remove[now]==level:
          print(now)
          break
        else:
          heapq.heappop(Min)
  else: # solved
    P=int(order[1])
    remove[P]=0
