import sys
input=sys.stdin.readline

def get():
    count=0
    q=[]
    made=[]
    for i in range(N):
        for j in range(M):
            if l[i][j]=='o':
                made.append([i,j])
                count+=1
                if count==2:
                    made.append(0)
                    q.append(made)
                    return q

def find():
    global flag
    while len(q)>0:
        f,s,count=q.pop(0)
        if count==10:
            flag=1
            print(-1)
            return
        if (f[0]==N-1 and s[0]!=N-1) or (s[0]==N-1 and f[0]!=N-1) or (f[0]==0 and s[0]!=0) or (s[0]==0 and f[0]!=0) or (f[1]==M-1 and s[1]!=M-1) or (s[1]==M-1 and f[1]!=M-1) or (f[1]==0 and s[1]!=0) or (s[1]==0 and f[1]!=0):
            flag=1
            print(count+1)
            return
        
        # 상
        if f[0]!=0 and s[0]!=0 and (l[f[0]-1][f[1]]!='#' or l[s[0]-1][s[1]]!='#'):
            if l[f[0]-1][f[1]]=='#':
                if f[0]!=s[0]-1 or f[1]!=s[1]:
                    q.append([[f[0],f[1]],[s[0]-1,s[1]],count+1])
            elif l[s[0]-1][s[1]]=='#':
                if f[0]-1!=s[0] or f[1]!=s[1]:
                    q.append([[f[0]-1,f[1]],[s[0],s[1]],count+1])
            else:
                q.append([[f[0]-1,f[1]],[s[0]-1,s[1]],count+1])
        # 하
        if f[0]!=N-1 and s[0]!=N-1 and (l[f[0]+1][f[1]]!='#' or l[s[0]+1][s[1]]!='#'):
            if l[f[0]+1][f[1]]=='#':
                if f[0]!=s[0]+1 or f[1]!=s[1]:
                    q.append([[f[0],f[1]],[s[0]+1,s[1]],count+1])
            elif l[s[0]+1][s[1]]=='#':
                if f[0]+1!=s[0] or f[1]!=s[1]:
                    q.append([[f[0]+1,f[1]],[s[0],s[1]],count+1])
            else:
                q.append([[f[0]+1,f[1]],[s[0]+1,s[1]],count+1])
        # 좌
        if f[1]!=0 and s[1]!=0 and (l[f[0]][f[1]-1]!='#' or l[s[0]][s[1]-1]!='#'):
            if l[f[0]][f[1]-1]=='#':
                if f[1]!=s[1]-1 or f[0]!=s[0]:
                    q.append([[f[0],f[1]],[s[0],s[1]-1],count+1])
            elif l[s[0]][s[1]-1]=='#':
                if f[1]-1!=s[1] or f[0]!=s[0]:
                    q.append([[f[0],f[1]-1],[s[0],s[1]],count+1])
            else:
                q.append([[f[0],f[1]-1],[s[0],s[1]-1],count+1])
        # 우
        if f[1]!=M-1 and s[1]!=M-1 and (l[f[0]][f[1]+1]!='#' or l[s[0]][s[1]+1]!='#'):
            if l[f[0]][f[1]+1]=='#':
                if f[1]!=s[1]+1 or f[0]!=s[0]:
                    q.append([[f[0],f[1]],[s[0],s[1]+1],count+1])
            elif l[s[0]][s[1]+1]=='#':
                if f[1]+1!=s[1] or f[0]!=s[0]:
                    q.append([[f[0],f[1]+1],[s[0],s[1]],count+1])
            else:
                q.append([[f[0],f[1]+1],[s[0],s[1]+1],count+1])


N,M=map(int,input().split())
l=[]
for i in range(N):
    board=list(input().rstrip())
    l.append(board)
q=get()
flag=0
find()
if flag==0:
    print(-1)
