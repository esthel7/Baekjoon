def solution(numbers):
    answer = []
    num=len(numbers)
    for i in range(num):
        for j in range(i+1,num):
            answer.append(numbers[i]+numbers[j])
    answer=sorted(list(set(answer)))
    return answer