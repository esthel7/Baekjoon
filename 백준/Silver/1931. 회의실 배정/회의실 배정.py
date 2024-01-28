import sys
input=sys.stdin.readline

def find(N):
  for i in range(1,N):
    start=l[i][0]
    end=l[i][1]
    if start>=num[-1]:
      num.append(end)
  print(len(num)-1)


N=int(input())
l=[[-1,-1]]
Last=0
for i in range(N):
  now=list(map(int,input().split()))
  l.append(now)
  Last=max(Last,now[1])

l.sort(key=lambda x:(x[1],x[0]))

num=[0] # 가능한 회의 수
find(N+1)
