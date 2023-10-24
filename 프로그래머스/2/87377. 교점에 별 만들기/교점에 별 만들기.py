def solution(line):
    lineLen=len(line)
    w=[]
    maxX=0
    maxY=0
    minX=0
    minY=0
    for i in range(lineLen):
        for j in range(i+1,lineLen):
            a=line[i][0]
            b=line[i][1]
            e=line[i][2]
            c=line[j][0]
            d=line[j][1]
            f=line[j][2]
            if (a*d-b*c)!=0 and (b*f-e*d)/(a*d-b*c) == (b*f-e*d)//(a*d-b*c):
                if (a*d-b*c)!=0 and (e*c-a*f)/(a*d-b*c)==(e*c-a*f)//(a*d-b*c):
                    w.append([(b*f-e*d)//(a*d-b*c),(e*c-a*f)//(a*d-b*c)])
                    if len(w)==1:
                        maxX=(b*f-e*d)//(a*d-b*c)
                        minX=(b*f-e*d)//(a*d-b*c)
                        maxY=(e*c-a*f)//(a*d-b*c)
                        minY=(e*c-a*f)//(a*d-b*c)
                    else:
                        maxX=max(maxX,(b*f-e*d)//(a*d-b*c))
                        minX=min(minX,(b*f-e*d)//(a*d-b*c))
                        maxY=max(maxY,(e*c-a*f)//(a*d-b*c))
                        minY=min(minY,(e*c-a*f)//(a*d-b*c))
    w.sort(key=lambda x:(-x[1],x[0]))
    answer=[]
    for i in range(maxY,minY-1,-1):
        answers=''
        for j in range(minX,maxX+1):
            if len(w)>0 and w[0]==[j,i]:
                for k in range(len(w)):
                    if w[0]==[j,i]:
                        w.pop(0)
                answers+='*'
            else:
                answers+='.'
        answers=''.join(answers)
        answer.append(answers)
    return answer