# dp는 해당 위치까지 도달하는 경우의 수 출력

import sys
input=sys.stdin.readline

def find(num):
    for i in range(1,4):
        for j in range(i,num):
            dp[j]=dp[j-i]+dp[j]
    
    for i in l:
        print(dp[i])

T=int(input())
l=[0 for i in range(T)]
for i in range(T):
    l[i]=int(input())

dp=[0 for i in range(max(l)+1)] # 최댓값만큼 설정
dp[0]=1
find(max(l)+1)
