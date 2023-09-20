def solution(n, left, right):
    answer = []
    
    leftF=left//n
    leftL=left%n
    rightF=right//n
    rightL=right%n
    if leftF==rightF:
        for i in range(leftL,rightL+1):
            answer.append(max(leftF+1,i+1))
        return answer
    for i in range(leftL,n):
        answer.append(max(leftF+1,i+1))
    for i in range(leftF+1,rightF+1):
        for j in range(n):
            if i==rightF and j>rightL:
                break
            answer.append(max(i+1,j+1))
    return answer