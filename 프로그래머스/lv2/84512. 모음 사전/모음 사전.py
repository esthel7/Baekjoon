def go(l):
    if len(l)==5:
        return True

def makeWord(l,wordList):
    if go(l):
        return
    for i in range(len(wordList)):
        l.append(wordList[i])
        total.append(''.join(l))
        makeWord(l,wordList)
        l.pop()

total=[]
def solution(word):
    answer = 0
    wordList=['A','E','I','O','U']
    makeWord([],wordList)
    for i in range(len(total)):
        if total[i]==word:
            return i+1
    return answer