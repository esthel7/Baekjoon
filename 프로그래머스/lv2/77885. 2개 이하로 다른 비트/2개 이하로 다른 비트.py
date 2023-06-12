def solution(numbers):
    
    # def change(num):
    #     l=[]
    #     n=1
    #     cnt=0
    #     while num!=0:
    #         if num>n:
    #             n*=2
    #             cnt+=1
    #         elif num==n:
    #             if len(l)==0:
    #                 l=[0 for i in range(cnt+2)]
    #             l[cnt]=1
    #             break
    #         else: # num<n
    #             if len(l)==0:
    #                 l=[0 for i in range(cnt+1)]
    #             l[cnt-1]=1
    #             num-=n/2
    #             n=1
    #             cnt=0
    #     return l
    
    def find(l,num):
        n=len(l)
        for i in range(n-1):
            if l[n-1-i]=='0':
                l[n-1-i]='1'
                if i!=0: 
                    l[n-i]='0'
                return l
        
        # 다 1로 구성된 경우
        l[0]='1'
        l[1]='0'
        return l
    
    
    def change10(l):
        num=0
        L=len(l)
        for i in range(L):
            num+=pow(2,i)*int(l[L-1-i])
        return num
    
                    
    n=len(numbers)
    answer=[0 for i in range(n)]
    l=[0 for i in range(n)]
    for i in range(n):
        l[i]=list(format(numbers[i],'b')) # 2진수 변환
        l[i]=['0']+l[i]
        l[i]=find(l[i],numbers[i]) # 1,2자리 변환
        answer[i]=change10(l[i]) # 10진수 변환
    return answer