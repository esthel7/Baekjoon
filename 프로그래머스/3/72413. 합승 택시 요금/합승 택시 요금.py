import heapq

def solution(n, s, a, b, fares):
    graph=[[]for i in range(n+1)]
    for [start,end,cost] in fares:
        graph[start].append([cost,end])
        graph[end].append([cost,start])

    q=[[0,s]]
    heapq.heapify(q)
    visitedC=[0 for i in range(n+1)]
    for [cost,nextnode] in graph[s]:
        heapq.heappush(q,[cost,nextnode])
    while q:
        cnt,node=heapq.heappop(q)
        if node==s:
            continue
        if visitedC[node]==0 or visitedC[node]>cnt:
            visitedC[node]=cnt
            for [cost,nextnode] in graph[node]:
                heapq.heappush(q,[cnt+cost,nextnode])
    
    q=[[0,a]]
    heapq.heapify(q)
    visitedA=[0 for i in range(n+1)]
    for [cost,nextnode] in graph[a]:
        heapq.heappush(q,[cost,nextnode])
    while q:
        cnt,node=heapq.heappop(q)
        if node==a:
            continue
        if visitedA[node]==0 or visitedA[node]>cnt:
            visitedA[node]=cnt
            for [cost,nextnode] in graph[node]:
                heapq.heappush(q,[cnt+cost,nextnode])
    
    q=[[0,b]]
    heapq.heapify(q)
    visitedB=[0 for i in range(n+1)]
    for [cost,nextnode] in graph[b]:
        heapq.heappush(q,[cost,nextnode])
    while q:
        cnt,node=heapq.heappop(q)
        if node==b:
            continue
        if visitedB[node]==0 or visitedB[node]>cnt:
            visitedB[node]=cnt
            for [cost,nextnode] in graph[node]:
                heapq.heappush(q,[cnt+cost,nextnode])
    
    # print(visitedC)
    # print(visitedA)
    # print(visitedB)
    answer=-1
    for i in range(1,n+1):
        now=visitedC[i]+visitedA[i]+visitedB[i]
        if now==0:
            continue
        if answer==-1 or answer>now:
            answer=now
        
    return answer