def solution(k, dungeons):
    def find(visited, now, cnt, n):
        for i in range(n):
            if visited[i]==0 and now>=dungeons[i][0]:
                visited[i]=1
                find(visited,now-dungeons[i][1],cnt+1,n)
                visited[i]=0
        tour.append(cnt)
            
        
            
    answer = -1
    dungeons=sorted(dungeons, reverse=True)
    n=len(dungeons)
    visited=[0 for i in range(n)]
    tour=[]
    answer=find(visited,k,0,n)
    if answer!=n:
        answer=max(tour)
    return answer