def solution(n):
    answer = [[]for i in range(n)]
    start=0
    end=n
    cnt=0
    value=1
    while True:
        if(start>end):
            break
        for i in range(start,end):
            answer[i].insert(cnt,value)
            value+=1

        if(start+1>end):
            break
        for i in range(start+1,end):
            answer[n-1-cnt].insert(cnt+1+i-start-1,value)
            value+=1
        
        if(start+1>end-1):
            break
        for i in range(end-2,start,-1):
            answer[i].insert(len(answer[i])-cnt,value)
            value+=1
        start+=2
        end-=1
        cnt+=1
    
    result=[]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            result.append(answer[i][j])
    
    # return answer
    return result