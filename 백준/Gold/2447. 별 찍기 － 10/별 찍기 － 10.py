def star(l):
    m=[]
    for i in range(len(l)*3):
        if i//len(l)==1:
            m.append(l[i%len(l)]+' '*len(l)+l[i%len(l)])
        else:
            m.append(l[i%len(l)]*3)
    return m
    

n=int(input())
l=['***','* *','***']
cnt=3
for i in range(8):
    if cnt==n:
        break
    cnt=cnt*3
for j in range(i):
    l=star(l)
for i in l:
    print(i)
