def solution(clothes):
    clothes.sort(key=lambda x:x[1])
    lists=[]
    lists.append([clothes[0][0]])
    for i in range(1,len(clothes)):
        if clothes[i-1][1]==clothes[i][1]:
            lists[len(lists)-1].append(clothes[i][0])
        else:
            lists.append([clothes[i][0]])

    # 해당 종류의 옷을 (여러개) 입거나 안입거나
    # 모든 종류들의 갯수 + 1 을 다 곱한 후 아무것도 안입는 경우 하나 빼기
    total=1
    for i in range(len(lists)):
        total*=len(lists[i])+1
    return total-1
    
    # return total