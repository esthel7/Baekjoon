import sys
input=sys.stdin.readline

n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))

dp=[10001 for i in range(k+1)]
dp[0]=0

for i in range(n):
    for j in range(k+1-l[i]):
        if dp[j+l[i]]>dp[j]+1:
            dp[j+l[i]]=dp[j]+1

if dp[-1]==10001:
    print(-1)
else:
    print(dp[-1])
