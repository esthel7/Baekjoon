import sys
sys.setrecursionlimit(10**6)

def count(cap,idx,l,num,Max):
    nextIdx=-1
    for i in range(idx,-1,-1):
        if l[i]==0:
            continue
        if num+l[i]<cap:
            num+=l[i]
            if Max==-1:
                Max=i+1
            continue
        elif num+l[i]>cap:
            remain=cap-num
            num=cap
            l[i]-=remain
            if Max==-1:
                Max=i+1
            nextIdx=i
            break
        else:
            num=cap
            if Max==-1:
                Max=i+1
            nextIdx=i-1
            break
    return [Max,l,nextIdx]

def find(cap,n,d,p,D,P):
    while D>=0 or P>=0:
        dnum=0
        dmax=-1
        i=D
        [dmax,d,D]=count(cap,i,d,dnum,dmax)

        pnum=0
        pmax=-1
        i=P
        [pmax,p,P]=count(cap,i,p,pnum,pmax)

        # print(dmax,pmax,d,p,D,P)
        if pmax!=-1 or dmax!=-1:
            total[0]+=max(pmax,dmax)*2
    

total=[0]
def solution(cap, n, deliveries, pickups):
    find(cap,n,deliveries,pickups,n-1,n-1)
    return total[0]