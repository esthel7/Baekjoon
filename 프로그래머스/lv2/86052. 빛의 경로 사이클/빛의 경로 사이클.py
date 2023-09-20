import sys
sys.setrecursionlimit(10 ** 6)

def U(l,di,i,j,num):
    if i-1>=0:
        return find(l,di,'U',i-1,j,num+1)
    else:
        return find(l,di,'U',len(l)-1,j,num+1)

def D(l,di,i,j,num):
    if i+1<len(l):
        return find(l,di,'D',i+1,j,num+1)
    else:
        return find(l,di,'D',0,j,num+1)
            
def R(l,di,i,j,num):
    if j+1<len(l[i]):
        return find(l,di,'R',i,j+1,num+1)
    else:
        return find(l,di,'R',i,0,num+1)
    
def L(l,di,i,j,num):
    if j-1>=0:
        return find(l,di,'L',i,j-1,num+1)
    else:
        return find(l,di,'L',i,len(l[i])-1,num+1)

def find(l,di,direction,i,j,num):
    if direction=='U':
        if 'U' in di[i][j]:
            di[i][j].remove('U')
        else:
            return num
    elif direction=='D':
        if 'D' in di[i][j]:
            di[i][j].remove('D')
        else:
            return num
    elif direction=='R':
        if 'R' in di[i][j]:
            di[i][j].remove('R')
        else:
            return num
    else:
        if 'L' in di[i][j]:
            di[i][j].remove('L')
        else:
            return num
    
    if l[i][j]=='S':
        if direction=='U':
            return U(l,di,i,j,num)
        elif direction=='D':
            return D(l,di,i,j,num)
        elif direction=='R':
            return R(l,di,i,j,num)
        else:
            return L(l,di,i,j,num)
            
    elif l[i][j]=='L':
        if direction=='U':
            return L(l,di,i,j,num)
        elif direction=='D':
            return R(l,di,i,j,num)
        elif direction=='R':
            return U(l,di,i,j,num)
        else:
            return D(l,di,i,j,num)
    
    else: # R
        if direction=='U':
            return R(l,di,i,j,num)
        elif direction=='D':
            return L(l,di,i,j,num)
        elif direction=='R':
            return D(l,di,i,j,num)
        else:
            return U(l,di,i,j,num)

answer=[]
def solution(grid):
    l=[0 for i in range(len(grid))] # [[s,l],[l,s]]
    di=[0 for i in range(len(grid))] # [[[UDRL],[UDRL]],[[UDRL],[UDRL]]]
    for i in range(len(grid)):
        l[i]=list(grid[i])
        di[i]=[[]for j in range(len(l[i]))]
        for j in range(len(l[i])):
            di[i][j]=['U','D','R','L']
    
    while True:
        flag=False
        for i in range(len(di)):
            for j in range(len(di[i])):
                if len(di[i][j])!=0:
                    num=0
                    answer.append(find(l,di,di[i][j][0],i,j,num))
                    flag=True
                    
        if flag==False:
            break

    answer.sort()
    return answer