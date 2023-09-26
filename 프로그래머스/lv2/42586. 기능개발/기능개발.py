def check(last,n,progresses):
    today=0
    for i in range(last,n):
        if progresses[i]>=100:
            today+=1
            last=i
        else: # 미완료 존재
            break
    return [today,last]

def solution(progresses, speeds):
    answer = []
    n=len(progresses)
    last=0
    while True:
        if last==n:
            break
        today=0
        flag=False
        for i in range(last,n):
            progresses[i]+=speeds[i]
            if progresses[i]>=100:
                flag=True
        if flag:
            value=check(last,n,progresses)
            if value[0]!=0:
                answer.append(value[0])
                last=value[1]+1
    return answer