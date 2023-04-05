import sys
input=sys.stdin.readline

def find():
    count=-1
    while len(q)>0:
        node=q.pop(0)
        count=count+1
        while len(graph[node])>0:
            new=graph[node].pop(0)
            if visited[new]==0:
                q.append(new)
                visited[new]=1
    
    print(count)


N=int(input())
M=int(input())
graph=[[]for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b) # 각자 다 연결해줘야 그래프 순회 가능
    graph[b].append(a)

visited=[0 for i in range(N+1)]
q=[]
q.append(1)
visited[1]=1
find()
