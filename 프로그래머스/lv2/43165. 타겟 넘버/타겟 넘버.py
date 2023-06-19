def solution(numbers, target):
    def find(i,now,n):
        if i==n:
            if now==target:
                l.append(1)
        else:
            find(i+1,now+numbers[i],n)
            find(i+1,now-numbers[i],n)
    answer = 0
    n=len(numbers)
    l=[]
    find(0,0,n)
    answer=len(l)
    return answer