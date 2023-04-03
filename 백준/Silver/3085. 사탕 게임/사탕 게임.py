import sys
input=sys.stdin.readline

def check():
    Max=0
    for i in range(N):
        count=1
        for j in range(N-1):
            if color[i][j]==color[i][j+1]:
                count=count+1
            else:
                count=1

            if Max<count:
                Max=count
    
    for i in range(N):
        count=1
        for j in range(N-1):
            if color[j][i]==color[j+1][i]:
                count=count+1
            else:
                count=1

            if Max<count:
                Max=count
    
    return Max

N=int(input())
color=[[]for i in range(N)]
for i in range(N):
    color[i]=list(input().rstrip())

# 한 번 바꾼 상태에서 최대값 뽑아내기

total=0
for i in range(N):
    for j in range(N-1):
        # 가로 바꾸기
        change=color[i][j]
        color[i][j]=color[i][j+1]
        color[i][j+1]=change

        value=check()
        if value>total:
            total=value

        change=color[i][j]
        color[i][j]=color[i][j+1]
        color[i][j+1]=change

for i in range(N):
    for j in range(N-1):
        # 세로 바꾸기
        change=color[j+1][i]
        color[j+1][i]=color[j][i]
        color[j][i]=change

        value=check()
        if value>total:
            total=value

        change=color[j+1][i]
        color[j+1][i]=color[j][i]
        color[j][i]=change

print(total)
