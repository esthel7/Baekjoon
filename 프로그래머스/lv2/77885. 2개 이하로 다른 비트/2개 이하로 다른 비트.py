import math

def find(num):
    l=list(format(num,'b')) # 2진수
    flag=False
    
    for i in range(len(l)-1,-1,-1):
        if l[i]=='0':
            num+=math.pow(2,len(l)-1-i)
            for j in range(i+1,len(l)):
                if l[j]=='1':
                    num-=math.pow(2,len(l)-1-j)
                    break
            flag=True
            break
    
    if flag==False:
        num-=math.pow(2,len(l)-1)
        num+=math.pow(2,len(l))
            
    return num

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(find(numbers[i]))
    return answer