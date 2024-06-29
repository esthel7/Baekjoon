import sys
input=sys.stdin.readline

N=int(input())
lose=list(map(int,input().split()))
gain=list(map(int,input().split()))

total=[[0 for i in range(101)]for j in range(2)]
answer=0

for i in range(N):
  for j in range(100-lose[i],-1,-1):
    total[i+1][j]=max(total[i][j],total[i][j+lose[i]]+gain[i])

  if i==N-1:
    break
  total.append(list(total[i+1]))

# print(total)
print(total[N][1])
