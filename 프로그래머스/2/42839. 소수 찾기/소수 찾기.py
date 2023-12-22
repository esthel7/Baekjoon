def check(num):
    if num in totalNum:
        return False
    totalNum.append(num)
    if num==1 or num==0:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

def make(now, nowNumbers, numbers, lenNumbers):
    if len(nowNumbers)>0 and check(int(''.join(nowNumbers))):
        total[0]+=1
    for i in range(lenNumbers):
        if i not in now:
            now.append(i)
            nowNumbers.append(numbers[i])
            make(now,nowNumbers,numbers,lenNumbers)
            now.pop()
            nowNumbers.pop()
    

totalNum=[]
total=[0]
def solution(numbers):
    numbers=list(numbers)
    now=[]
    nowNumbers=[]
    lenNumbers=len(numbers)
    make(now, nowNumbers, numbers, lenNumbers)
    return total[0]