def check(p,x,y):
    if x-1>=0 and y+1<5 and p[x-1][y+1]=='P':
        if p[x-1][y]!='X' or p[x][y+1]!='X':
            return True
    if x+1<5 and y-1>=0 and p[x+1][y-1]=='P':
        if p[x][y-1]!='X' or p[x+1][y]!='X':
            return True
    if y+1<5 and p[x][y+1]=='P':
        return True
    if x+1<5 and y+1<5 and p[x+1][y+1]=='P':
        if p[x][y+1]!='X' or p[x+1][y]!='X':
            return True
    if x+1<5 and p[x+1][y]=='P':
        return True
    if x+2<5 and p[x+2][y]=='P':
        if p[x+1][y]!='X':
            return True
    if y+2<5 and p[x][y+2]=='P':
        if p[x][y+1]!='X':
            return True
    return False

def find(p):
    for i in range(5):
        for j in range(5):
            if p[i][j]=='P':
                if check(p,i,j):
                    return 0
    return 1
            

def solution(places):
    answer = []
    for i in range(len(places)):
        for j in range(5):
            places[i][j]=list(places[i][j])
        answer.append(find(places[i]))
    return answer