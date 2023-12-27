def make(land,num,n,m,visit):
    while len(visit):
        [i,j]=visit.pop()
        if i-1>=0 and land[i-1][j]==1:
            cnt[0]+=1
            land[i-1][j]=num
            visit.append([i-1,j])
        if i+1<n and land[i+1][j]==1:
            cnt[0]+=1
            land[i+1][j]=num
            visit.append([i+1,j])
        if j-1>=0 and land[i][j-1]==1:
            cnt[0]+=1
            land[i][j-1]=num
            visit.append([i,j-1])
        if j+1<m and land[i][j+1]==1:
            cnt[0]+=1
            land[i][j+1]=num
            visit.append([i,j+1])

def find(n,m,land):
    for i in range(n):
        for j in range(m):
            if land[i][j]==1:
                cnt[0]=1
                visit=[[i,j]]
                num=(-1)*len(exist)
                land[i][j]=num
                make(land,num,n,m,visit)
                exist.append(cnt[0])
                
exist=[0]
cnt=[0]
def solution(land):
    answer = 0
    n=len(land) # 세로
    m=len(land[0]) # 가로

    find(n,m,land)
    for i in range(m):
        check=[]
        now=0
        for j in range(n):
            num=(-1)*land[j][i]
            if num not in check:
                check.append(num)
                now+=exist[num]
        if answer<now:
            answer=now
            
    return answer