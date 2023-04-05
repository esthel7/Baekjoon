import sys
input=sys.stdin.readline

def find():
    if len(stack)==M:
        for i in range(M):
            print(stack[i],end=' ')
        print()
    
    for i in range(N):
        if visited[i]==1:
            continue
        visited[i]=1
        stack.append(i+1)
        find()
        stack.pop()
        visited[i]=0

N,M=map(int,input().split())

stack=[]
visited=[0]*(N) # visited=[0 for i in range(N)] 대신 사용
find()
