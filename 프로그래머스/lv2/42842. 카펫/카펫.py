def solution(brown, yellow):
    answer = []
    # a*b=yellow, (a+2)*(b+2)-a*b=brown -> (a+2)*(b+2)=brown+yellow
    total=brown+yellow
    for i in range(3,brown):
        if total%i==0:
            wall=total//i
            if (i-2)*(wall-2)==yellow:
                if i>=wall:
                    answer=[i,wall]
                else:
                    answer=[wall,i]
                break
    return answer