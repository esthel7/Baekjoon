def calculate(l,board,n,m):
    now=0
    for i in range(n):
        for j in range(m):
            if board[i][j]+l[i][j]<=0:
                now+=1
    return now
            

def solution(board, skill):
    n=len(board)
    m=len(board[0])
    answer = n*m
    
    l=[[0 for i in range(m)]for j in range(n)]
    s=len(skill)
    for i in range(s):
        [t, r1, c1, r2, c2, degree]=skill[i]
        if t==1: # attack
            degree*=(-1)
        l[r1][c1]+=degree
        if c2+1<m:
            l[r1][c2+1]-=degree
        if r2+1<n:
            l[r2+1][c1]-=degree
            if c2+1<m:
                l[r2+1][c2+1]+=degree
    
    for j in range(1,m):
        l[0][j]+=l[0][j-1]
    
    for i in range(1,n):
        for j in range(1,m):
            l[i][j]+=l[i][j-1]
        for j in range(m):
            l[i][j]+=l[i-1][j]  
    
    answer-=calculate(l,board,n,m)
    return answer