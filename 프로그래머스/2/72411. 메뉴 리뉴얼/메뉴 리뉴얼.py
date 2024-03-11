def solution(orders, course):
    def find(total,Len,idx,start,now):
        if Len<total:
            return
        if len(now)==total:
            now=''.join(now)
            if now in info:
                info[now]+=1
            else:
                info[now]=1
            return
        for i in range(start,Len):
            now.append(orders[idx][i])
            find(total,Len,idx,i+1,list(now))
            now.pop()
        
    answer = []
    info={}
    for total in course:
        for i in range(len(orders)):
            sortOrder=list(orders[i])
            sortOrder.sort()
            orders[i]=''.join(sortOrder)
            find(total,len(orders[i]),i,0,[])
    
    courselist={}
    for idx in course:
        courselist[idx]=[0,[]]

    for keys in info.keys():
        if info[keys]>=2:
            Len=len(keys)
            if courselist[Len][0]<info[keys]:
                courselist[Len][0]=info[keys]
                courselist[Len][1]=[keys]
            elif courselist[Len][0]==info[keys]:
                courselist[Len][1].append(keys)

    for idx in course:
        answer+=courselist[idx][1]
    answer.sort()
        
    return answer