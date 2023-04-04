import sys
input=sys.stdin.readline

def find():
    q.append([0,0,0])
    while len(q)>0:
        i,j,count=q.pop(0)
        if visited[i][j]>count+1:
            count=count+1
            visited[i][j]=count
            if i==N-1 and j==M-1:
                print(count)
                return # 함수 나가기
            if i+1<N and l[i+1][j]=='1':
                q.append([i+1,j,count])
            if j+1<M and l[i][j+1]=='1':
                q.append([i,j+1,count])
            if i-1>=0 and l[i-1][j]=='1':
                q.append([i-1,j,count])
            if j-1>=0 and l[i][j-1]=='1':
                q.append([i,j-1,count])

N,M=map(int,input().split())
l=[[]for i in range(N)]
for i in range(N):
    l[i]=list(input().rstrip())

q=[]
total=[]
visited=[[10001 for i in range(M)] for i in range(N)]
find()
