def find(brown,yellow):
    total=brown+yellow
    for i in range(3,total):
        if total%i==0:
            j=total//i
            if (i-2)*(j-2)==yellow:
                return [i,j]

def solution(brown, yellow):
    # yx*yy=yellow
    # bx*by-yellow=brown
    # bx=yx+2
    # by=yy+2
    value=find(brown, yellow)
    return [value[1],value[0]]