import sys
input=sys.stdin.readline

def find():
    if len(s)==M:
        for i in range(len(s)):
            print(s[i],end=' ')
        print()
    if len(s)!=0:
        for i in range(s[-1],N):
            if visited[i]==1:
                continue
            visited[i]=1
            s.append(i+1)
            find()
            s.pop()
            visited[i]=0
    else:
        for i in range(N):
            if visited[i]==1:
                continue
            visited[i]=1
            s.append(i+1)
            find()
            s.pop()
            visited[i]=0

N,M=map(int,input().split())

s=[]
visited=[0]*(N)
find()
