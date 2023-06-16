def solution(numbers):
    answer = ''
    n=len(numbers)
    for i in range(n):
        numbers[i]=list(str(numbers[i]))
    numbers=sorted(numbers, key=lambda x:x*3, reverse=True)

    new=[]
    for i in range(n):
        new+=numbers[i]
    answer=''.join(new)
    answer=str(int(answer)) # 0000 방지 위함
    return answer