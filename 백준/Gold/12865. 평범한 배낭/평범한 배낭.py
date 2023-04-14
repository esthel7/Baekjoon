import sys
input=sys.stdin.readline

def find():
    for i in range(1,N+1):
        w,v=l[i-1]
        for j in range(1,K+1):
            if j<w: # 아직 안들어감
                dp[i][j]=dp[i-1][j] # 전 물건들의 가치 그대로 가져오기

            else: # 물건이 들어올 수 있음
                dp[i][j]=max(dp[i-1][j],v+dp[i-1][j-w])
                # 물건을 넣지 않거나, 물건을 넣거나(=다른 물건을 빼거나) 선택
                # 다른 물건을 뺄 때는 해당 무게만큼의 물건을 빼야함


N,K=map(int,input().split()) # 물건 N개, 가치 K
l=[]
for i in range(N):
    w,v=map(int,input().split())
    l.append([w,v])

# 들어갈 물건 별로 하나의 열이 생성됨
# 하나의 물건만 있을 경우, 해당 무게 이상의 경우는 일정 가치 보장됨
# 두 개 이상일 경우 해당 물건을 넣을지(다른 물건을 빼서), 해당 물건을 안넣을지 결정 필요

dp=[[0 for i in range(K+1)] for i in range(N+1)] # 물건별로 K 가치까지 배열 생성
find()
print(dp[N][K])
