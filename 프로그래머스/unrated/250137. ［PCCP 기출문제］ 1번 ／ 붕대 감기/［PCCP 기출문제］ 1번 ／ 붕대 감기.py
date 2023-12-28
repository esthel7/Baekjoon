def solution(bandage, health, attacks):
    maxhealth=health
    time=attacks[len(attacks)-1][0]
    [attacktime,attack]=attacks.pop(0)
    t=0
    for i in range(time+1):
        if i==attacktime:
            t=0
            health-=attack
            if health<=0:
                health=-1
                break
            if i!=time:
                [attacktime,attack]=attacks.pop(0)
            continue
        t+=1
        health+=bandage[1]
        if t==bandage[0]:
            health+=bandage[2]
            t=0
        if health>maxhealth:
            health=maxhealth

    return health