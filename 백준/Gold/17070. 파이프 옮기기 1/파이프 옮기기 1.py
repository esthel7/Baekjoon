import sys
input=sys.stdin.readline

def find():
    if l[0][2]==0:
        dp[0][2][0]=1
        if l[1][1]==0 and l[1][2]==0:
            dp[1][2][2]=1
    for i in range(N):
        for j in range(N):
            for k in range(3):
                if k==0 and dp[i][j][k]!=0: # 가로
                    if j+1<N and l[i][j+1]==0:
                        dp[i][j+1][0]+=dp[i][j][k] # 가로
                        if i+1<N and l[i+1][j]==0 and l[i+1][j+1]==0:
                            dp[i+1][j+1][2]+=dp[i][j][k] # 대각선

                elif k==1 and dp[i][j][k]!=0: #세로
                    if i+1<N and l[i+1][j]==0:
                        dp[i+1][j][1]+=dp[i][j][k] # 세로
                        if j+1<N and l[i][j+1]==0 and l[i+1][j+1]==0:
                            dp[i+1][j+1][2]+=dp[i][j][k] # 대각선

                elif k==2 and dp[i][j][k]!=0: # 대각선
                    if j+1<N and l[i][j+1]==0:
                        dp[i][j+1][0]+=dp[i][j][k] # 가로
                    if i+1<N and l[i+1][j]==0:
                        dp[i+1][j][1]+=dp[i][j][k] # 세로
                        if j+1<N and l[i][j+1]==0 and l[i+1][j+1]==0:
                            dp[i+1][j+1][2]+=dp[i][j][k] # 대각선

N=int(input())
l=[]

for i in range(N):
    l.append(list(map(int,input().split())))

dp=[[[0,0,0]for i in range(N)]for i in range(N)]
find()
print(dp[N-1][N-1][0]+dp[N-1][N-1][1]+dp[N-1][N-1][2])
