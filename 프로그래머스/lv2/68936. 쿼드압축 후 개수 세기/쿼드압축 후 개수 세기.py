def solution(arr):
    def check4(i,j,num,c0,c1):
        if arr[i][j]!=-1 and arr[i][j]==arr[i][j+num//2]==arr[i+num//2][j]==arr[i+num//2][j+num//2]:
            arr[i][j+num//2]=-1
            arr[i+num//2][j]=-1
            arr[i+num//2][j+num//2]=-1
            return arr[i][j],c0,c1
        if arr[i][j]==0:
            c0+=1
        elif arr[i][j]==1:
            c1+=1
        return -1,c0,c1
    
    def find(n,num,c0,c1):
        for i in range(0,n,num):
            for j in range(0,n,num):
                arr[i][j],c0,c1=check4(i,j,num,c0,c1)
        return c0,c1

    
    answer = []
    n=len(arr)
    num=2
    c0=0
    c1=0
    while num<=n:
        c0,c1=find(n,num,c0,c1)
        num*=2
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                c0+=1
            elif arr[i][j]==1:
                c1+=1
    answer.append(c0)
    answer.append(c1)
    return answer