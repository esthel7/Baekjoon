def calculate(now,prev):
    if now[1]>=prev[1]:
        return (now[0]-prev[0])*60+now[1]-prev[1]
    return (now[0]-1-prev[0])*60+now[1]+60-prev[1]

def solution(fees, records):
    answer = []
    exist={}
    total=[]
    inTime=[]
    carsnumber=[]
    cars=0
    for i in range(len(records)):
        [timeData,num,flag]=records[i].split(' ')
        [h,m]=timeData.split(':')
        h=int(h)
        m=int(m)
        if flag=='IN':
            if num in exist:
                inTime[exist[num]]=[h,m]
            else:
                exist[num]=cars
                cars+=1
                total.append(0)
                inTime.append(0)
                carsnumber.append(num)
                inTime[exist[num]]=[h,m]
        else:
            long=calculate([h,m],inTime[exist[num]])
            inTime[exist[num]]=[-1,-1]
            total[exist[num]]+=long

    for i in range(cars):
        if inTime[i]!=[-1,-1]:
            long=calculate([23,59],inTime[i])
            total[i]+=long

    for i in range(cars):
        fee=fees[1]
        unit=0
        if total[i]>fees[0]:
            if (total[i]-fees[0])%fees[2]==0:
                unit=(total[i]-fees[0])//fees[2]
            else:
                unit=(total[i]-fees[0])//fees[2]+1
        fee+=unit*fees[3]
        answer.append(fee)
    
    
    final=[]
    carsnumber.sort()
    for i in range(cars):
        final.append(answer[exist[carsnumber[i]]])
    return final