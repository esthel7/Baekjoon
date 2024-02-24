import sys
import heapq
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  k=int(input())
  info={}
  maxQ=[]
  minQ=[]
  heapq.heapify(maxQ)
  heapq.heapify(minQ)
  for i in range(k):
    order=input().rstrip().split()
    if order[0]=='D':
      if not maxQ:
        continue
      if order[1]=='1': # 최댓값 삭제
        while maxQ:
          now=maxQ[0]*(-1)
          if info[now]!=0:
            info[now]-=1
            break
          else:
            heapq.heappop(maxQ)
      else: # 최솟값 삭제
        while minQ:
          now=minQ[0]
          if info[now]!=0:
            info[now]-=1
            break
          else:
            heapq.heappop(minQ)
    else:
      n=int(order[1])
      if n in info:
        info[n]+=1
      else:
        info[n]=1
      heapq.heappush(maxQ,n*(-1))
      heapq.heappush(minQ,n)

  answer=[]
  while maxQ:
    now=maxQ[0]*(-1)
    if info[now]!=0:
      answer.append(now)
      break
    else:
      heapq.heappop(maxQ)

  if not answer:
    print('EMPTY')
    continue

  while minQ:
    now=minQ[0]
    if info[now]!=0:
      answer.append(now)
      break
    else:
      heapq.heappop(minQ)

  for now in answer:
    print(now,end=' ')
