from collections import deque

def solution(info, edges):
    many=len(info)
    graph=[[]for i in range(many)] # 자식들 보관
    for [a,b] in edges:
        graph[a].append(b)
        
    answer=[0]
    q=deque([0]) # 방문 가능 노드 관리
    
    def find(q,sheep,wolf):
        while q:
            node=q[0]
            if info[node]==0: # sheep
                q.popleft()
                sheep+=1
                for nextnode in graph[node]:
                    if info[nextnode]==0:
                        q.appendleft(nextnode)
                    else:
                        q.append(nextnode)
            else: # wolf
                if wolf+1<sheep:
                    wolf+=1
                    firstQ=deque(q)
                    for i in range(len(firstQ)):
                        q=list(firstQ)
                        node=q.pop(i)
                        q=deque(q)
                        for nextnode in graph[node]:
                            if info[nextnode]==0:
                                q.appendleft(nextnode)
                            else:
                                q.append(nextnode)
                        find(deque(q),sheep,wolf)
                break
                    
        if answer[0]<sheep:
            answer[0]=sheep
    
    find(q,0,0)

    return answer[0]