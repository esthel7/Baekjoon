import sys
input=sys.stdin.readline

# 네모는 순서, 동그라미는 노드 번호
# 들어오는 강 중 가장 큰 값의 개수가 한개면 그 값 그대로, 여러개면 그 값+1

def find():
    q=[]
    for i in range(1,M+1):
        if indegree[i][0]==0:
            indegree[i][1]=1 # 최대레벨 지정
            q.append(i)
    
    while len(q)>0:
        now=q.pop(0)
        for i in range(len(graph[now])):
            next=graph[now][i]
            indegree[next][0]-=1
            if indegree[now][1]>indegree[next][1]:
                indegree[next][1]=indegree[now][1] # 최대레벨 갱신
                indegree[next][2]=1
            elif indegree[now][1]==indegree[next][1]:
                indegree[next][2]+=1 # 최대레벨 개수 갱신
            
            if indegree[next][0]==0:
                q.append(next)
                if indegree[next][2]>1: # 최대레벨 여러개
                    indegree[next][1]+=1
    
    return indegree[M][1]


T=int(input())
for i in range(T):
    K,M,P=map(int,input().split()) # 테스트 번호, 노드, 간선
    graph=[[]for i in range(M+1)]
    indegree=[[0,0,0]for i in range(M+1)] # 진입차수, 최대레벨, 최대레벨개수
    for j in range(P):
        a,b=map(int,input().split())
        graph[a].append(b) # 도착 노드 저장
        indegree[b][0]+=1 # 강의 시작 가려내기 위함

    print(K,find())
