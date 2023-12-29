def make(n,k):
    l=''
    while n!=0:
        sub=n%k
        n//=k
        l=str(sub)+l
    return l

def check(m):
    if m<2:
        return False
    for i in range(2,int(m**(1/2))+1):
        if m%i==0:
            return False
    return True

def count(n):
    num=0
    cnt=0
    n=''.join(n)
    l=n.split('0')
    for i in range(len(l)):
        if l[i]=='':
            continue
        m=int(l[i])
        if check(m):
            cnt+=1
            
    return cnt

def solution(n, k):
    n=make(n,k)
    answer=count(n)
    return answer