def find(node,info,child,parent,possible,sheep,wolf):
    if info[node]==0:
        sheep+=1
        if answer[0]<sheep:
            answer[0]=sheep
    else:
        if sheep<=wolf+1:
            return
        wolf+=1
    
    for nextnode in child[node]:
        possible.append(nextnode)
    
    for i in range(len(possible)):
        new=list(possible)
        nextnode=new.pop(i)
        find(nextnode,info,child,parent,new,sheep,wolf)
    
        
        

answer=[1]
def solution(info, edges):
    child=[[]for i in range(len(info))]
    parent=[0 for i in range(len(info))]
    
    for i in range(len(edges)):
        [p,c]=edges[i]
        child[p].append(c)
        parent[c]=p

    find(0,info,child,parent,[],0,0)
    return answer[0]