def solution(numbers):
    numbers.sort(key=lambda x:list(str(x))*3,reverse=True)
    answer=''
    for i in range(len(numbers)):
        answer+=''.join(list(str(numbers[i])))
    return str(int(answer))