def solution(line):
    
    def check(a,b):
        if a==0:
            return 0
        if b==0:
            return 0.1
        if a//b==a/b:
            return a//b
        return 0.1
    
    def cal(x,y,maxX,minX,maxY,minY):
        if maxX==0.1 or x>maxX:
            maxX=x
        if minX==0.1 or x<minX:
            minX=x
        if maxY==0.1 or y>maxY:
            maxY=y
        if minY==0.1 or y<minY:
            minY=y
        return maxX,minX,maxY,minY
    
    def star(maxX,minX,maxY,minY):
        X=maxX-minX+1
        Y=maxY-minY+1
        dots=[['.' for i in range(X)]for i in range(Y)]
        while len(dot):
            x,y=dot.pop(0)
            dots[maxY-y][x-minX]='*'

        answer=[[]for i in range(Y)]
        for i in range(Y):
            answer[i]=''.join(dots[i])
        return answer

    answer = []
    n=len(line)
    dot=[]
    maxX,minX,maxY,minY=0.1,0.1,0.1,0.1
    for i in range(n):
        for j in range(i+1,n):
            A=line[i][0]
            B=line[i][1]
            E=line[i][2]
            C=line[j][0]
            D=line[j][1]
            F=line[j][2]
            x=check(B*F-E*D,A*D-B*C)
            if x==0.1:
                continue
            y=check(E*C-A*F,A*D-B*C)
            if y==0.1:
                continue
            dot.append([x,y])
            maxX,minX,maxY,minY=cal(x,y,maxX,minX,maxY,minY)

    answer=star(maxX,minX,maxY,minY)
    return answer