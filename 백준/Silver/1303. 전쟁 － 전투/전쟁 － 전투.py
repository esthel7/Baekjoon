import sys
input=sys.stdin.readline

def find(i,j,color):
    q.append([i,j])
    count=0
    while len(q)>0:
        i,j=q.pop(0)
        if visited[i][j]==0:
            visited[i][j]=1
            if l[i][j]==color:
                count=count+1
                if j+1<N and l[i][j+1]==color:
                    q.append([i,j+1])
                if j-1>=0 and l[i][j-1]==color:
                    q.append([i,j-1])
                if i-1>=0 and l[i-1][j]==color:
                    q.append([i-1,j])
                if i+1<M and l[i+1][j]==color:
                    q.append([i+1,j])
    return count


N,M=map(int,input().split())
l=[[] for i in range(M)]
for i in range(M):
    l[i]=list(input().rstrip())


# for 문으로 모든 공간 방문하도록
q=[]
white=0
blue=0
visited=[[0 for i in range(N)]for i in range(M)]
for i in range(M):
    for j in range(N):
        if l[i][j]=='W' and visited[i][j]!=1:
            white=white+find(i,j,'W')**2
        elif l[i][j]=='B' and visited[i][j]!=1:
            blue=blue+find(i,j,'B')**2

print(white, blue)
