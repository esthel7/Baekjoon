import sys
input=sys.stdin.readline

N,M=map(int,input().split())

l=[0 for i in range(N)]
total=[[0 for i in range(N)]for i in range(N)]
for i in range(N):
    l[i]=list(map(int,input().split()))
    if i==0:
        total[i][0]=l[i][0]
        for j in range(1,N):
            total[i][j]=l[i][j]+total[i][j-1]
    else:
        total[i][0]=total[i-1][0]+l[i][0]
        for j in range(1,N):
            total[i][j]=l[i][j]-total[i-1][j-1]+total[i][j-1]+total[i-1][j]

v=[0 for i in range(M)]
for i in range(M):
    v[i]=list(map(int,input().split()))
    # 세로 처음부터 1까지 빠지고, 가로 처음부터 2까지 빠지고, (1,2) 대각선 위 더하기
    x1=v[i][0]-1
    y1=v[i][1]-1
    x2=v[i][2]-1
    y2=v[i][3]-1
    if x1!=0 and y1!=0:
        print(total[x2][y2]-total[x2][y1-1]-total[x1-1][y2]+total[x1-1][y1-1])
    elif x1==0 and y1!=0:
        print(total[x2][y2]-total[x2][y1-1])
    elif x1!=0 and y1==0:
        print(total[x2][y2]-total[x1-1][y2])
    else:
        print(total[x2][y2])