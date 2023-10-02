total=[0]

def go(k,dungeons,l):
    for i in range(len(l)):
        if k>=dungeons[l[i]][0]:
            k-=dungeons[l[i]][1]
        else:
            return -1
    return len(l)

def find(k,dungeons,l):
    value=go(k,dungeons,l)
    if value!=-1:
        total[0]=max(total[0],value)
    if len(l)==len(dungeons):
        return
    for i in range(len(dungeons)):
        if i in l:
            continue
        l.append(i)
        find(k,dungeons,l)
        l.pop()

def solution(k, dungeons):
    find(k,dungeons,[])
    return total[0]