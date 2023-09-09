def n3(n):
    a=1
    num=0
    l=[]
    while True:
        if n==0:
            break
        if a>n:
            if len(l)==0:
                l=[0 for i in range(num)]
            l[num-1]+=1
            n=n-a/3
            a=1
            num=0
        else:
            a*=3
            num+=1
    return l

def n10(l):
    num=0
    for i in range(len(l)):
        num+=pow(3,i)*l[len(l)-i-1]
    return num

def solution(n):
    newN=n3(n)
    answer=n10(newN)
    return answer