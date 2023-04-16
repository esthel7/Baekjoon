import sys
input=sys.stdin.readline

def find():
    for i in range(N):
        if i!=0 and dp[i]==0: # 안지나왔음
            continue
        
        if l[i]=='B':
            next='O'
        elif l[i]=='O':
            next='J'
        else:
            next='B'
        
        count=1
        for j in range(i+1,N):
            if l[j]==next:
                num=dp[i]+count*count
                if dp[j]==0 or dp[j]>num:
                    dp[j]=num
            count+=1

N=int(input())
l=list(input().rstrip())

dp=[0]*N
find()
if dp[N-1]==0:
    print(-1)
else:
    print(dp[N-1])
