def initTree(total, prev, new, lenWires):
    for i in range(lenWires+1):
        if total[i]==prev:
            total[i]=new
    return total

def makeTree(idx,wires,lenWires,total):
    for i in range(lenWires):
        if i==idx:
            continue
        f=wires[i][0]-1
        s=wires[i][1]-1
        if total[f]==-1:
            if total[s]==-1: # new new
                total[f]=f
                total[s]=f
            else: # new old
                total=initTree(total,total[s],f,lenWires)
                total[f]=f
        else:
            if total[s]==-1: # old new
                total[s]=total[f]
            else: # old old
                if total[f]==total[s]:
                    continue
                elif total[f]<total[s]:
                    total=initTree(total,total[s],total[f],lenWires)
                else:
                    total=initTree(total,total[f],total[s],lenWires)
    minTree=1
    maxTree=0
    f=total[0]
    for i in range(1,lenWires+1):
        if total[i]==f:
            minTree+=1
        else:
            maxTree+=1
    return abs(minTree-maxTree)

def solution(n, wires):
    answer = 101
    lenWires=len(wires)
    wires.sort(key=lambda x:x[0])
    for i in range(lenWires):
        total=[-1 for j in range(lenWires+1)]
        new=makeTree(i,wires,lenWires,total)
        if new<answer:
            answer=new
    return answer