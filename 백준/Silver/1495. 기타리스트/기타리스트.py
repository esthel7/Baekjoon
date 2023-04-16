import sys
input=sys.stdin.readline

def find():
    global final
    for i in range(N):
        for j in range(M+1):
            if dp[i][j]==1:
                if j+V[i]<=M:
                    dp[i+1][j+V[i]]=1
                    if i==N-1 and final<j+V[i]:
                        final=j+V[i]

                if j-V[i]>=0:
                    dp[i+1][j-V[i]]=1
                    if i==N-1 and final<j-V[i]:
                        final=j-V[i]

N,S,M=map(int,input().split()) # 곡 수, 시작 볼륨, 최대 볼륨
V=list(map(int,input().split())) # 리스트 형식으로 받기

final=-1
dp=[[0 for i in range(M+1)]for i in range(N+1)] # 가능한 볼륨에 1 표시하기(곡별로)
dp[0][S]=1
find()
print(final)
