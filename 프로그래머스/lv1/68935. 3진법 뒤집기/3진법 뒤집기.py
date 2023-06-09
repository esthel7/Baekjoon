def solution(n):
    answer = 0
    v=1
    cnt=0
    l=[]
    while n!=0:
        if n==v:
            if len(l)==0:
                l=[0 for i in range(cnt+1)]
            l[cnt]=1
            n=0
        elif n<v:
            if len(l)==0:
                l=[0 for i in range(cnt)]
            if n//(v/3)==2:
                l[cnt-1]=2
                n=n-v/3*2
            else:
                l[cnt-1]=1
                n=n-v/3
            v=1
            cnt=0
        else:
            v*=3
            cnt+=1
    
    L=len(l)
    for i in range(L):
        answer+=pow(3,i)*l[L-1-i]
    return answer
