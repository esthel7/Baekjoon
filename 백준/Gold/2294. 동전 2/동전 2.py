import sys
input=sys.stdin.readline

def find():
    for i in range(len(l)):
        j=l[i]
        if j<k+1:
            if dp[j]==-1 or dp[j]>1:
                dp[j]=1
            for j in range(l[i]+1,k+1):
                if j%l[i]==0:
                    if dp[j]>dp[j-l[i]]+1 or dp[j]==-1:
                        dp[j]=dp[j-l[i]]+1
                elif dp[j-l[i]]!=-1:
                    if dp[j]>dp[j-l[i]]+1 or dp[j]==-1:
                        dp[j]=dp[j-l[i]]+1
            # print(dp)

n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))

l=list(set(l))

dp=[-1 for i in range(k+1)]
dp[0]=1
find()
print(dp[k])
