import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))

info={}
for i in range(M):
  a,b,t=map(int,input().split())
  if l[a]!=1 and a!=N-1 and (l[b]!=1 or b==N-1):
    if a in info:
      info[a][b]=t
    else:
      info[a]={b:t}
  if l[b]!=1 and b!=N-1 and (l[a]!=1 or a==N-1):
    if b in info:
      info[b][a]=t
    else:
      info[b]={a:t}

dp=[-1 for i in range(N)]
dp[0]=0
q=[]
heapq.heappush(q,[0,0])
while q:
  cnt,start=heapq.heappop(q)
  if dp[start]!=cnt:
    continue
  if start in info:
    for end in info[start]:
      if dp[end]==-1 or dp[end]>info[start][end]+dp[start]:
        dp[end]=info[start][end]+dp[start]
        heapq.heappush(q,[dp[end],end])

# print(dp)
print(dp[N-1])
