def solution(s):
    
    def remove(n):
        c=list(n)
        num=0 # 0 개수
        u=0
        for i in range(len(c)):
            if c[i]=='0':
                num+=1
            else:
                u=u*10+1
        return (num,str(u))
        
        
    def change(n):
        cnt=0
        now=1
        l=[]
        while n!=0:
            if n==now:
                if len(l)==0:
                    l=[0 for i in range(cnt+1)]
                l[cnt]=1
                n=0
            elif n<now:
                if len(l)==0:
                    l=[0 for i in range(cnt)]
                l[cnt-1]=1
                n-=now/2
                now=1
                cnt=0
            else:
                now*=2
                cnt+=1
        
        r=''
        for i in range(len(l)):
            r=str(l[i])+r
        return str(r)
        
    answer = []
    num=0 # 0 개수
    cnt=0 # 변환횟수
    
    while True:
        newNum,s=remove(s) # 0 제거
        num+=newNum
        cnt+=1
        if s=='1':
            answer.append(cnt)
            answer.append(num)
            break
        n=len(s)
        s=change(n) # 2진법

    return answer