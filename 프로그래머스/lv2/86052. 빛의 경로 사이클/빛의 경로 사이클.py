def solution(grid):
    
    def find(X,Y):
        while len(q):
            x,y,num,di=q.pop(0)
            if x==X:
                x=0
            elif x<0:
                x=X-1
            if y==Y:
                y=0
            elif y<0:
                y=Y-1
            if l[x][y][di]==1:
                answer.append(num)
                break
            l[x][y][di]=1
            if di==0: # top
                if grid[x][y]=='S':
                    newX=x-1
                    newY=y
                    newDi=0
                elif grid[x][y]=='R':
                    newX=x
                    newY=y+1
                    newDi=3
                else:
                    newX=x
                    newY=y-1
                    newDi=2
            elif di==1: # bottom
                if grid[x][y]=='S':
                    newX=x+1
                    newY=y
                    newDi=1
                elif grid[x][y]=='R':
                    newX=x
                    newY=y-1
                    newDi=2
                else:
                    newX=x
                    newY=y+1
                    newDi=3
            elif di==2: # left
                if grid[x][y]=='S':
                    newX=x
                    newY=y-1
                    newDi=2
                elif grid[x][y]=='R':
                    newX=x-1
                    newY=y
                    newDi=0
                else:
                    newX=x+1
                    newY=y
                    newDi=1
            else: # right
                if grid[x][y]=='S':
                    newX=x
                    newY=y+1
                    newDi=3
                elif grid[x][y]=='R':
                    newX=x+1
                    newY=y
                    newDi=1
                else:
                    newX=x-1
                    newY=y
                    newDi=0
            q.append([newX,newY,num+1,newDi])

                
    answer = []
    X=len(grid) 
    Y=len(grid[0])
    for i in range(len(grid)):
        grid[i]=list(grid[i])
    
    l=[[[0,0,0,0]for i in range(Y)]for i in range(X)] # 상하좌우 유무
    q=[]
    
    for i in range(X):
        for j in range(Y):
            for k in range(4):
                if l[i][j][k]==0:
                    q.append([i,j,0,k])
                    find(X,Y)
    
    answer=sorted(answer)
    return answer