def check(num):
    if num in values:
        return False
    values.append(num)
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

def go(l,numbers):
    if len(l)==0:
        return
    if numbers[l[0]]=='0':
        return
    num=''
    for i in range(len(l)):
        num+=numbers[l[i]]
    num=int(num)
    if check(num):
        total[0]+=1

def make(l,numbers):
    go(l,numbers)
    for i in range(len(numbers)):
        if i not in l:
            l.append(i)
            make(l,numbers)
            l.pop(-1)
            
total=[0]
values=[]
def solution(numbers):
    l=[]
    numbers=list(numbers)
    make(l,numbers)
    # return values
    return total[0]    