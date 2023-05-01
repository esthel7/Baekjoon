import sys
input=sys.stdin.readline

# 문자는 문자열에서 사라지고, 남은 문자열은 합쳐짐

l=input().rstrip()
word=list(input().rstrip())
Word=len(word)
stack=[]
for i in range(len(l)):
    stack.append(l[i])
    if stack[-Word:]==word: # 음수로 접근 시 뒤에서부터 계산
        # stack=stack[:-Word]
        for j in range(Word): # 시간 줄어?
            stack.pop()
        # print('after',stack)

if len(stack):
    print(''.join(stack)) # 연달아 출력하기
else:
    print('FRULA')

