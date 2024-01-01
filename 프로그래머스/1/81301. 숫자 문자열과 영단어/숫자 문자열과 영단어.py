def solution(s):
    answer = []
    num=['zero','one','two','three','four','five','six','seven','eight','nine']
    S=len(s)
    i=0
    while i!=S:
        if s[i]>='0' and s[i]<='9':
            answer.append(s[i])
            i+=1
        else:
            if s[i]=='z':
                i+=4
                answer.append('0')
                continue
            elif s[i]=='o':
                i+=3
                answer.append('1')
                continue
            elif s[i]=='t':
                if s[i+1]=='w':
                    i+=3
                    answer.append('2')
                    continue
                else:
                    i+=5
                    answer.append('3')
                    continue
            elif s[i]=='f':
                if s[i+1]=='o':
                    i+=4
                    answer.append('4')
                    continue
                else:
                    i+=4
                    answer.append('5')
                    continue
            elif s[i]=='s':
                if s[i+1]=='i':
                    i+=3
                    answer.append('6')
                    continue
                else:
                    i+=5
                    answer.append('7')
                    continue
            elif s[i]=='e':
                i+=5
                answer.append('8')
                continue
            else:
                i+=4
                answer.append('9')
                continue
    answer=int(''.join(answer))
    return answer