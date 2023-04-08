import sys
input=sys.stdin.readline

def find():
    for i in range(N):
        for j in range(N):
            if i==N-1 and j==N-1: # l[i][j]=0이므로 break 필수
                print(dp[i][j])
                break

            if l[i][j]+j<N: # 오른쪽
                next=l[i][j]+j
                dp[i][next]+=dp[i][j] # 그냥 1 더하지 말고 이전에 도달가능했던 방법 수에 1개 더하기
            if l[i][j]+i<N: # 아래
                next=l[i][j]+i
                dp[next][j]+=dp[i][j]


# dp는 해당 위치까지 도달할 수 있는 경우의 수 출력!
N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))

dp=[[0 for i in range(N)] for i in range(N)]
dp[0][0]=1
find()
