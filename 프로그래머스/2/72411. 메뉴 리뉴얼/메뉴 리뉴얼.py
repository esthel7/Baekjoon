def make(l,idx,order,course):
    if len(l)==course:
        name=''.join(l)
        if name in total:
            total[name]+=1
        else:
            total[name]=1
        if total[name]>cnt[course]:
            cnt[course]=total[name]
        return
    
    for i in range(idx,len(order)):
        l.append(order[i])
        make(l,i+1,order,course)
        l.pop()
    

total={}
cnt={}
def solution(orders, course):
    answer = []
    for i in range(len(course)):
        cnt[course[i]]=-1
    for i in range(len(orders)):
        order=sorted(list(orders[i]))
        for j in range(len(course)):
            if len(order)>=course[j]:
                make([],0,order,course[j])
    
    for key in total.keys():
        L=len(key)
        if total[key]>=2 and total[key]==cnt[L]:
            answer.append(key)
    answer.sort()
    return answer