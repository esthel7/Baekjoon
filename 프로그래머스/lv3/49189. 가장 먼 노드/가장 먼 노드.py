def makeEdge(n,edge):
    graph=[[]for i in range(n+1)]
    for i in range(len(edge)):
        a,b=edge[i]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def find(graph,visited):
    # for i in range(len(graph[num])):
    #     next=graph[num][i]
    #     if visited[next]==-1 or visited[next]>count:
    #         visited[next]=count
    #         find(graph,next,count+1,visited)
    q=[]
    q.append([1,0])
    while len(q)>0:
        now,count=q.pop(0)
        for i in range(len(graph[now])):
            next=graph[now][i]
            if visited[next]==-1:
                visited[next]=count+1
                q.append([next,count+1])

    
def solution(n, edge):
    graph=makeEdge(n,edge)
    visited=[-1 for i in range(n+1)]
    visited[1]=0
    find(graph,visited)
    num=max(visited)
    answer=0
    if num!=0:
        for i in range(n+1):
            if visited[i]==num:
                answer+=1
    return answer
