def solution(numbers):
    newNumbers=[]
    for i in range(len(numbers)):
        newNumbers.append(str(numbers[i]))
    numbers=newNumbers
    numbers=sorted(numbers,key=lambda x:x*3,reverse=True)
    answer=str(int(''.join(numbers)))
    return answer