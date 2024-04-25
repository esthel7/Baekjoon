import sys
input=sys.stdin.readline

# 음수사이클 -> -1
# 각 노드별로 최솟값 출력

def find():
  for i in range(N):
    for start in range(1,N+1):
      for node in cost[start]:
        if final[start]!=last and final[node]>cost[start][node]+final[start]:
          final[node]=cost[start][node]+final[start]
          if i==N-1: # infinite
            print(-1)
            exit(0)

N,M=map(int,input().split())

last=20000*N
cost={}
for i in range(1,N+1):
  cost[i]={}

for i in range(M):
  a,b,c=map(int,input().split())
  if a in cost:
    if b in cost[a]:
      if cost[a][b]>c:
        cost[a][b]=c
    else:
      cost[a][b]=c
  else:
    cost[a]={b:c}

final=[last for i in range(N+1)]
final[1]=0
find()

for i in range(2,N+1):
  if final[i]==last:
    print(-1)
  else:
    print(final[i])
