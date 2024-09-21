import sys
input=sys.stdin.readline

N=int(input())
dis=list(map(int,input().split()))
price=list(map(int,input().split()))

answer=0
target=price[0]
start=0
for i in range(1,N):
  if price[i]<target:
    answer+=sum(dis[start:i])*target
    target=price[i]
    start=i

answer+=sum(dis[start:N])*target

print(answer)
