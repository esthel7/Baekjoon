def find(l,users,emoticons):
    global list
    total=0
    count=0
    for i in range(len(users)):
        percentage,flag=users[i]
        cost=0
        for j in range(len(emoticons)):
            if l[j]>=percentage:
                cost+=emoticons[j]*(100-l[j])//100 # // 두개는 몫만 계산됨
            if cost>=flag: # 시간초과 방지
                count+=1
                cost=-1
                break
        if cost!=-1:
            total+=cost
    if list[0]<count: # 시간초과 방지
        list=[count,total]
    elif list[0]==count:
        if list[1]<total:
            list=[count,total]

def makeList(users,cut,emoticons):
    if len(l)==len(emoticons):
        find(l,users,emoticons)
        return
    for i in range(len(cut)):
        # while 문 없어도 가능
        l.append(cut[i])
        makeList(users,cut,emoticons)
        l.pop(-1)

def solution(users, emoticons):
    cut=[10,20,30,40] # 할인율
    makeList(users,cut,emoticons)
    answer = list
    return answer

l=[]
list=[0,0]