def solution(progresses, speeds):
    # 개발순서 별개, 차례로 배포됨
    answer = []
    n=len(progresses)
    l=[]
    for i in range(n):
        cnt=0
        while True:
            progresses[i]+=speeds[i]
            cnt+=1
            if progresses[i]>=100:
                l.append(cnt)
                break
    i=0
    while i!=n:
        a=0
        flag=0
        for j in range(i,n):
            if l[i]>=l[j]:
                a+=1
            else:
                answer.append(a)
                i=j
                flag=1
                break
        if flag==0:
            answer.append(a)
            break
    return answer