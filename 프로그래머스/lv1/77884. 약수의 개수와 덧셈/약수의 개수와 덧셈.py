def solution(left, right):
    answer = 0
    l=[0 for i in range(right-left+1)]
    for i in range(left,right+1):
        if i==1:
            l[0]=1
        else:
            for j in range(1,i//2+1,1):
                if i%j==0 and i//j>=j:
                    if i//j==j:
                        l[i-left]+=1
                    else:
                        l[i-left]+=2
                    
    for i in range(len(l)):
        if l[i]%2==0:
            answer+=i+left
        else:
            answer-=i+left
    return answer