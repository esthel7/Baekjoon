def make(now,idx,numbers,target,lenNumbers):
    if idx==lenNumbers:
        if now==target:
            total[0]+=1
        return
    make(now+numbers[idx],idx+1,numbers,target,lenNumbers)
    make(now-numbers[idx],idx+1,numbers,target,lenNumbers)

total=[0]
def solution(numbers, target):
    make(0,0,numbers,target,len(numbers))
    return total[0]