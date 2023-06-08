def solution(n):
    answer = []
    l=[[]for i in range(n)]
    
    c=1 # 숫자
    now=1 # 삼각변 위치
    index=0 # 삼각변 두께(안,밖)
    num=n # 변 길이
    
    while c<=n*(n+1)/2:
        if now==1:
            now=2
            for i in range(num):
                l[index*2+i].insert(index,c)
                c+=1
            num-=1
        elif now==2:
            now=3
            Index=index+1
            for i in range(num):
                l[n-index-1].insert(Index,c)
                Index+=1
                c+=1
            num-=1
        else:
            now=1
            for i in range(num):
                l[n-i-2-index].insert(len(l[n-i-2-index])-index,c)
                c+=1
            num-=1
            index+=1
    
    for i in range(n):
        for j in range(len(l[i])):
            answer.append(l[i][j])
            
    return answer
