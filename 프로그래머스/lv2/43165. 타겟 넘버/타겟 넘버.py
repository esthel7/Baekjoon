def go(l,numbers,target):
    total=0
    for i in range(len(numbers)):
        if l[i]<0:
            total-=numbers[i]
        else:
            total+=numbers[i]
    if total==target:
        result[0]+=1

def make(l,index,numbers,target):
    if index==len(numbers)+1:
        go(l,numbers,target)
    else:
        l.append(index)
        make(l,index+1,numbers,target)
        l.pop(-1)
        l.append((-1)*index)
        make(l,index+1,numbers,target)
        l.pop(-1)

result=[0]
def solution(numbers, target):
    l=[]
    make(l,1,numbers,target)
    return result[0]