import sys
input=sys.stdin.readline

def find():
    for i in l:
        # i는 동전 가치
        for j in range(i,k+1):
            dp[j]=dp[j]+dp[j-i]
    print(dp[k])

# dp는 최적화 문제 해결 알고리즘 // 배열 한 개를 사용
n,k=map(int,input().split())
l=[0]*n
for i in range(n):
    l[i]=int(input())

dp=[0]*(k+1)
dp[0]=1
find()



#       0,1,2,3,4,5,6,7,8,9,10
# 1원만 [1,1,1,1,1,1,1,1,1,1,1]
# 2원만 [1,0,1,0,1,0,1,0,1,0,1]
# 5원만 [1,0,0,0,0,1,0,0,0,0,1]
# 1+2는 1원이 이미 추가된 상태이고, 2원 추가하는 경우, 2부터 시작임
# 1+2   [1,1,2,2,3,3,4,4,5,5,6] 이런 식으로 됨
