from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

def get_maxbranch(tree, root):
    if root not in tree : return 0

    maxbranch = 0
    for node, w in tree[root].items():
        del tree[node][root]
        branch = w + get_maxbranch(tree, node)
        if branch > maxbranch :
            maxbranch = branch
    return maxbranch

# 변수초기화
N, R = map(int, stdin.readline().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, w = map(int, stdin.readline().split())
    tree[a][b] = w
    tree[b][a] = w

# 기가노드까지의 기둥 길이 찾기
giganode = R
gigalen = 0
while len(tree[giganode])==1:
    node, w = list(tree[giganode].items())[0]
    del tree[node][giganode]
    gigalen += w
    giganode = node

# 가장 긴 가지 길이 찾기
maxbranch = get_maxbranch(tree, giganode)

print('{} {}'.format(gigalen, maxbranch))