def solution(line):
    answer = []
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            A=line[i][0]
            B=line[i][1]
            E=line[i][2]
            C=line[j][0]
            D=line[j][1]
            F=line[j][2]
            if A*D-B*C==0:
                continue
            if (B*F-E*D)%(A*D-B*C)==0:
                x=(B*F-E*D)//(A*D-B*C)
                if (E*C-A*F)%(A*D-B*C)==0:
                    y=(E*C-A*F)//(A*D-B*C)
                    answer.append([x,y])
            continue

    answer.sort() # x 작은값~큰값
    minX=answer[0][0]
    maxX=answer[len(answer)-1][0]
    answer.sort(key=lambda x:x[1]) # y 작은값~큰값
    minY=answer[0][1]
    maxY=answer[len(answer)-1][1]
    result=[['.' for i in range(maxX-minX+1)] for i in range(maxY-minY+1)]
    for i in range(len(answer)):
        x=answer[i][0]-minX
        y=maxY-answer[i][1]
        result[y][x]='*'
    for i in range(len(result)):
        result[i]=''.join(result[i])
    return result