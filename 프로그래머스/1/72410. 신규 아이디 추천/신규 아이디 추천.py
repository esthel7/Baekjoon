def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    rem=['~','!','@','#','$','%','^','&','*','(',')','=','+','[',']','{','}',':','?',',','<','>','/']
    new_id=list(new_id)
    change=[]
    for i in range(len(new_id)):
        if new_id[i] in rem:
            continue
        change.append(new_id[i])
    new_id=[change[0]]
    for i in range(1,len(change)):
        if new_id[-1]=='.' and change[i]=='.':
            continue
        new_id.append(change[i])
    if new_id[0]=='.':
        new_id.pop(0)
    if not len(new_id):
        new_id.append('a')
    if len(new_id)>=16:
        new_id=new_id[:15]
    if new_id[-1]=='.':
        new_id=new_id[:len(new_id)-1]
    if len(new_id)<=2:
        last=new_id[-1]
        while len(new_id)!=3:
            new_id.append(last)
    answer=''.join(new_id)
    return answer