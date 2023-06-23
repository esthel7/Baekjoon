cnt=0
def solution(word):
    def make(WORD,l):
        global cnt
        if WORD==l:
            final.append(cnt)
            return
        if len(l)!=5:
            for i in ['A','E','I','O','U']:
                l.append(i)
                cnt+=1
                make(WORD,l)
                l.pop(-1)
    
    answer = 0
    # global cnt=0
    WORD=list(word)
    final=[]
    make(WORD,[])
    answer=final[0]
    return answer