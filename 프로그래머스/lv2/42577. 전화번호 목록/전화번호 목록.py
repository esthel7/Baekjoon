def solution(phone_book):
    # 있으면 false
    answer = True
    n=len(phone_book)
    phone_book=sorted(phone_book)
    for i in range(n-1):
        I=min(len(phone_book[i]),len(phone_book[i+1]))
        if phone_book[i][:I]==phone_book[i+1][:I]:
            answer=False
            return answer
    return answer