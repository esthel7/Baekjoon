def solution(numbers):

    def check(a):
        if a in nums:
            return -1
        nums.append(a)
        if a==1 or a==0:
            return -1
        for i in range(2,a):
            if a%i==0:
                return -1
        return 1
    
    def make(a,n,cnt):
        global answer
        if cnt!=n:
            for i in range(n):
                if i in l:
                    continue
                l.append(i)
                if check(int(a+numbers[i]))==1:
                    answers.append(1)
                make(a+numbers[i],n,cnt+1)
                l.pop(-1)
            
    answer = 0
    numbers=list(numbers)
    n=len(numbers)
    l=[]
    answers=[]
    nums=[]
    make('',n,0)
    # for i in range(n):
    #     a=numbers[i]
    #     l.append(i)
    #     if check(int(a))==1:
    #         answer+=1
    #     make('',n)
    #     for j in range(n):
    #         if j==i:
    #             continue
    #         a=a+numbers[j]
    #         if check(int(a))==1:
    #             answer+=1
    answer=len(answers)
    return answer