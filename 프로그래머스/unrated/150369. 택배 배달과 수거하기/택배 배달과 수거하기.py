def delivery(cap,n,deliveries):
    i=n
    now=cap
    while i>=0:
        if now==0:
            return i # 현재 위치부터 배달
        if deliveries[i]==0:
            i=i-1
            continue
        
        if deliveries[i]<=now:
            now=now-deliveries[i]
            deliveries[i]=0
        else:
            deliveries[i]=deliveries[i]-now
            now=0
            return i # 현재 위치부터 배달
        
        i=i-1
    return i
        

def pickup(cap,n,pickups):
    i=n
    now=0
    while i>=0:
        if now==cap:
            return i # 현재 위치부터 픽업
        if pickups[i]==0:
            i=i-1
            continue
        if pickups[i]<=cap-now:
            now=now+pickups[i]
            pickups[i]=0
        else:
            pickups[i]=pickups[i]-(cap-now)
            now=cap
            return i # 현재 위치부터 픽업
        
        i=i-1
    return i
    
        

def solution(cap, n, deliveries, pickups):
    i=n-1
    answer=0
    d=i
    p=i
    while i>=0:
        if deliveries[i]==0 and pickups[i]==0:
            i=i-1
            continue
        answer=answer+(i+1)*2
        
        d=delivery(cap,d,deliveries)
        p=pickup(cap,p,pickups)
                
    return answer