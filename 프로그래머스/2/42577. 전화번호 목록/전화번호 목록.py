def solution(phone_book):
    answer = True
    phone_book.sort()
    # print(phone_book)
    lenPhone=len(phone_book)
    lenBox=[]
    for i in range(lenPhone):
        lenBox.append(len(phone_book[i]))
    for i in range(lenPhone-1):
        minLen=min(lenBox[i],lenBox[i+1])
        A=phone_book[i][:minLen]
        B=phone_book[i+1][:minLen]
        if A==B:
            return False
    return answer