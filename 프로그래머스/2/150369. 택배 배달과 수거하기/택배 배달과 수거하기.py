# 가장 멀리 배달 후 수거 많이

def solution(cap, n, deliveries, pickups):
    answer = 0
    delfar=n-1
    while delfar>=0:
        if deliveries[delfar]==0:
            delfar-=1
        else:
            break
    pckfar=n-1
    while pckfar>=0:
        if pickups[pckfar]==0:
            pckfar-=1
        else:
            break
    last=max(delfar,pckfar)
    prevdelfar=delfar
    prevpckfar=pckfar

    while last!=-1:
        delcnt=0
        delfar=-1
        for i in range(prevdelfar,-1,-1):
            if delcnt+deliveries[i]<=cap:
                delcnt+=deliveries[i]
                deliveries[i]=0
            else:
                deliveries[i]-=cap-delcnt
                delcnt=cap
                delfar=i
                break
        pckcnt=0
        pckfar=-1
        for i in range(prevpckfar,-1,-1):
            if pckcnt+pickups[i]<=cap:
                pckcnt+=pickups[i]
                pickups[i]=0
            else:
                pickups[i]-=cap-pckcnt
                pckcnt=cap
                pckfar=i
                break
        answer+=(last+1)*2
        last=max(delfar,pckfar)
        prevdelfar=delfar
        prevpckfar=pckfar
    return answer