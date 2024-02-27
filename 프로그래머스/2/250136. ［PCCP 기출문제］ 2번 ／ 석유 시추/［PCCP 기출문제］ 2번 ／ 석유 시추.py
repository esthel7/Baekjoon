def solution(land):
    n=len(land)
    m=len(land[0])
    total=[0 for i in range(m)]
    
    visited=[[False for i in range(m)]for j in range(n)]
    xbox=[-1,1,0,0]
    ybox=[0,0,-1,1]
    
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            visited[i][j]=True
            cnt=0
            plus=[]
            if land[i][j]==1:
                q=[[i,j]]
                while q:
                    x,y=q.pop()
                    if y not in plus:
                        plus.append(y)
                    cnt+=1
                    for k in range(4):
                        newX=x+xbox[k]
                        newY=y+ybox[k]
                        if 0<=newX<n and 0<=newY<m and not visited[newX][newY]:
                            visited[newX][newY]=True
                            if land[newX][newY]==1:
                                q.append([newX,newY])

                for idx in plus:
                    total[idx]+=cnt

    print(total)
    return max(total)