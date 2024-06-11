import sys

# 백준 https://www.acmicpc.net/problem/1991

N = int(input())
data = sys.stdin.read().split()

def preDFS(root):
    prelist.append(root)
    if tree[root][0] != '.': preDFS(tree[root][0])
    inlist.append(root)
    if tree[root][1] != '.': preDFS(tree[root][1])
    postlist.append(root)

tree = dict()
prelist = []
inlist = []
postlist = []

for i in range(N):
    tree[data[3 * i]] = (data[3 * i + 1], data[3 * i + 2])
# '.' 이면 continue인거, 해당값이 

preDFS('A')

print(''.join(prelist) + '\n' + ''.join(inlist) + '\n' + ''.join(postlist) + '\n' )