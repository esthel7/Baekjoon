def solution(n, wires):
    def find(x,y):
        root=[0 for i in range(n+1)]
        num=[0 for i in range(n+1)]
        final=[]
        for i in range(m):
            a,b=wires[i]
            if [a,b]==[x,y]:
                continue
            if root[a]==0:
                if root[b]==0: # new new
                    root[a]=a
                    root[b]=a
                    final.append(a)
                    num[a]=2
                else: # new old
                    root[a]=root[b]
                    num[root[b]]+=1
            else:
                if root[b]==0: # old new
                    root[b]=root[a]
                    num[root[a]]+=1
                else: # old old
                    change=root[b]
                    final.remove(change)
                    num[root[a]]+=num[root[b]]
                    num[root[b]]=0
                    for j in range(1,n+1):
                        if root[j]==change:
                            root[j]=root[a]
        if len(final)==2:
            return abs(num[final[0]]-num[final[1]])
        else:
            for i in range(1,n+1):
                if root[i]==0:
                    return num[final[0]]-1 # 아무것도 연결되지 않은 노드 존재
            return -1
            
    def cut(m):
        for i in range(m):
            a,b=wires[i]
            num=find(a,b)
            if num!=-1:
                diff.append(num)
    
    answer = -1
    m=len(wires)
    diff=[]
    cut(m)
    answer=min(diff)
    return answer