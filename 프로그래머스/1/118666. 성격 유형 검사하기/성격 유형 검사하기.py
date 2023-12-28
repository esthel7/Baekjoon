def plus(answer,point,now):
    for i in range(4):
        if name[i][0]==now:
            answer[i][0]+=point
            break
        elif name[i][1]==now:
            answer[i][1]+=point
            break
    return answer
    
    
def make(answer):
    title=[]
    for i in range(4):
        if answer[i][0]>answer[i][1]:
            title.append(name[i][0])
        elif answer[i][0]<answer[i][1]:
            title.append(name[i][1])
        else:
            title.append(min(name[i][0],name[i][1]))
    return ''.join(title)


name=[['R','T'],['C','F'],['J','M'],['A','N']]
def solution(survey, choices):
    answer = [[0,0] for i in range(4)] 
    n=len(choices)
    for i in range(n):
        if choices[i]==4:
            continue
        elif choices[i]<4:
            point=4-choices[i]
            now=survey[i][0]
        else:
            point=choices[i]-4
            now=survey[i][1]
        answer=plus(answer,point,now)
    answer=make(answer)
    return answer