def calculate(l,n,m,users,emoticons):
    price=[0,0]
    for i in range(n):
        priceI=0
        for j in range(m):
            if priceI>=users[i][1]:
                break
            if l[j]>=users[i][0]:
                priceI+=int(emoticons[j]*(100-l[j])/100)
        if priceI>=users[i][1]:
            priceI=0
            price[0]+=1
        else:
            price[1]+=priceI
    if total[0]<price[0]:
        total[0]=price[0]
        total[1]=price[1]
    elif total[0]==price[0] and total[1]<price[1]:
        total[0]=price[0]
        total[1]=price[1]
                

def make(l,n,m,now,users,emoticons):
    if now==m:
        calculate(l,n,m,users,emoticons)
        return
    for i in range(4):
        l.append(sales[i])
        make(l,n,m,now+1,users,emoticons)
        l.pop()

sales=[10,20,30,40]
total=[0,0]
def solution(users, emoticons):
    n=len(users)
    m=len(emoticons)
    l=[]
    make(l,n,m,0,users,emoticons)
    return total