def find(g,n):
    for k in range(n):
        g[k][k]=0
        for i in range(n):
            for j in range(n):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])
    
    return g
   
    
def calculate(g,s,a,b,n):
    answer[0]=100000*n
    for i in range(n):
        now=g[s][i]+g[i][a]+g[i][b]
        if now<answer[0]:
            answer[0]=now
    

answer=[-1]
def solution(n, s, a, b, fares):
    maximum=100000*n
    g=[[maximum for i in range(n)]for i in range(n)]
    for [c,d,fee] in fares:
        g[c-1][d-1]=fee
        g[d-1][c-1]=fee

    g=find(g,n)
    calculate(g,s-1,a-1,b-1,n)
        
    return answer[0]